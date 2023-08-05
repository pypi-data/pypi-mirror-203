# A Python program that generates ePSF. Copyright 02/20/2022 by HuangZhen. All Rights Reserved.

import argparse
import matplotlib.pyplot as plt
from astropy.visualization import simple_norm
from astropy.io import fits
from photutils.detection import DAOStarFinder
from astropy.table import Table
from astropy.stats import sigma_clipped_stats
from astropy.nddata import NDData
from astropy.nddata import Cutout2D
from photutils.psf import extract_stars
from photutils.psf import EPSFBuilder
from photutils.segmentation import make_source_mask


def main():

    # Command-line argument parser
    parser = argparse.ArgumentParser(
        prog='epsf_generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
        More details in README.md.
        https://github.com/ZhenHuangLab/epsf_generator
        Feel free to contact me if you have any other questions.
        --------------------------
        Copyright: Zhen Huang. 
        Email: hzvictor@zju.edu.cn
        --------------------------
        ''',
        description='Generate an ePSF from a FITS image')
    parser.add_argument('-i', '--image', required=True, help='path to FITS image')
    parser.add_argument('-n', '--number', type=int, default=100, help='maximum number of stars to use for ePSF model')
    parser.add_argument('-f', '--fwhm', type=float, default=5.0, help='FWHM of stars in pixels')
    parser.add_argument('-s', '--size', type=int, default=25, help='size of cutout in pixels around detected stars')
    parser.add_argument('-o', '--output', required=True, help='path to output ePSF FITS file')
    args = parser.parse_args()

    #load image
    hdu = fits.open(args.image)
    data=hdu[0].data

    #find stars
    image = data
    mean, median, std = sigma_clipped_stats(image, sigma=3.0)
    daofind = DAOStarFinder(fwhm=args.fwhm, threshold=7 * std,peakmax=0.99,brightest=args.number)
    sources = daofind(image - median)

    #print the information of stars
    for col in sources.colnames:
        sources[col].info.format = '%.8g'
    print(sources)

    #exclude stars that are too close to the image boundaries
    size = args.size
    hsize = (size - 1) / 2
    x = sources['xcentroid']  
    y = sources['ycentroid']
    mask = ((x > hsize) & (x < (image.shape[1] -1 - hsize)) &  (y > hsize) & (y < (image.shape[0] -1 - hsize)))

    #create the table of good star positions
    stars_tbl = Table()
    stars_tbl['x'] = x[mask]
    stars_tbl['y'] = y[mask]
    print(stars_tbl)

    #subtract the background from the image
    b_mask = make_source_mask(image, nsigma=3, npixels=5, dilate_size=11)
    mean, median, std = sigma_clipped_stats(image, sigma=3.0, mask=b_mask)
    image -= median
    '''
    #another background estimation

    sigma_clip = SigmaClip(sigma=3.)
    bkg_estimator = MedianBackground()
    bkg = Background2D(image, (50, 50), filter_size=(3, 3), sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
    image -= bkg.background
    '''

    #create an NDData object
    nddata = NDData(data=image)

    #extract cutouts of our first selected stars
    stars = extract_stars(nddata, stars_tbl, size=size)

    #exclude stars due to crowding
    stars_tbl_s=Table(names=('xcentroid', 'ycentroid'))
    stars_l=[]
    for i in range(len(stars_tbl)):
        s_image = stars[i]
        mean, median, std = sigma_clipped_stats(s_image, sigma=3.0)
        s_daofind = DAOStarFinder(fwhm=2, threshold=5 * std,peakmax=0.95)
        peaks = s_daofind(s_image - median)
        if not peaks is None:
            if len(peaks)==1:
                stars_tbl_s.add_row([peaks[0]['xcentroid'],peaks[0]['ycentroid']])
                stars_l.append(i)
    stars_tbl_new=Table(names=('x', 'y'))
    for i in stars_l:
        stars_tbl_new.add_row([stars_tbl[i]['x'],stars_tbl[i]['y']])
    print(stars_tbl_new)

    #extract cutouts of our selected stars
    stars = extract_stars(nddata, stars_tbl_new, size=size)

    #show part of them
    nrows = 10
    ncols = 10
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 20), squeeze=True)
    ax = ax.ravel()
    for i in range(nrows * ncols):
        norm = simple_norm(stars[i], 'log', percent=99.)
        ax[i].imshow(stars[i], norm=norm, origin='lower', cmap='viridis')
    plt.show()

    #create the ePSF
    epsf_builder = EPSFBuilder(oversampling=1, maxiters=10, progress_bar=False)
    epsf, fitted_stars = epsf_builder(stars)

    #show the constructed ePSF
    norm = simple_norm(epsf.data, 'log', percent=99.)
    plt.figure()
    plt.imshow(epsf.data, norm=norm, origin='lower', cmap='viridis')
    plt.colorbar()
    plt.show()

    #save as fit
    cent = (size+1) // 2
    cutout = Cutout2D(epsf.data, (cent,cent), size=size)
    hdu=fits.PrimaryHDU(data=cutout.data)
    hdu.writeto(args.output,overwrite=True)

    # Copyright 02/20/2022 by HuangZhen. All Rights Reserved.