import collections
import pathlib

import cv2
import numpy as np

import dito.core
import dito.utils


def info(image, extended=False, minimal=False):
    """
    Returns an ordered dictionary containing info about the given image.
    """

    if not isinstance(image, np.ndarray):
        raise ValueError("Argument 'image' must be of type 'numpy.ndimage', but is '{}'".format(type(image)))

    if extended and minimal:
        raise ValueError("Both arguments 'extended' and 'minimal' must not be true at the same time")

    result = collections.OrderedDict()
    if extended:
        result["size"] = dito.utils.human_bytes(byte_count=image.size * image.itemsize)

    # these are the only stats shown when 'minimal' is true
    result["shape"] = image.shape
    result["dtype"] = image.dtype

    if not minimal:
        result["mean"] = np.mean(image) if image.size > 0 else np.nan
        result["std"] = np.std(image) if image.size > 0 else np.nan
        result["min"] = np.min(image) if image.size > 0 else np.nan
    if extended:
        result["1st quartile"] = np.percentile(image, 25.0) if image.size > 0 else np.nan
        result["median"] = np.median(image) if image.size > 0 else np.nan
        result["3rd quartile"] = np.percentile(image, 75.0) if image.size > 0 else np.nan
    if not minimal:
        result["max"] = np.max(image) if image.size > 0 else np.nan
    return result


def pinfo(*args, extended_=False, minimal_=False, file_=None, **kwargs):
    """
    Prints info about the given images.
    """

    # merge args and kwargs into one dictionary
    all_kwargs = collections.OrderedDict()
    for (n_image, image) in enumerate(args):
        if isinstance(image, str) or isinstance(image, pathlib.Path):
            # if `image` is a filename (str or pathlib.Path), use the filename as key
            all_kwargs[str(image)] = image
        else:
            # otherwise, use the position of the image in the argument list as key
            all_kwargs["{}".format(n_image)] = image
    all_kwargs.update(kwargs)

    header = None
    rows = []
    for (image_name, image) in all_kwargs.items():
        if isinstance(image, str):
            # `image` is a filename -> load it first
            image = dito.io.load(filename=image)
        image_info = info(image=image, extended=extended_, minimal=minimal_)
        if header is None:
            header = ("Image",) + tuple(image_info.keys())
            rows.append(header)
        row = [image_name] + list(image_info.values())

        # round float values to keep the table columns from exploding
        for (n_col, col) in enumerate(row):
            if isinstance(col, float):
                row[n_col] = dito.utils.adaptive_round(number=col, digit_count=8)

        rows.append(row)

    dito.utils.ptable(rows=rows, ftable_kwargs={"first_row_is_header": True}, print_kwargs={"file": file_})


def hist(image, bin_count=256):
    """
    Return the histogram of the specified image.
    """
    
    # determine which channels to use
    if dito.core.is_gray(image):
        channels = [0]
    elif dito.core.is_color(image):
        channels = [0, 1, 2]
    else:
        raise ValueError("The given image must be a valid gray scale or color image")
    
    # accumulate histogram over all channels
    hist = sum(cv2.calcHist([image], [channel], mask=None, histSize=[bin_count], ranges=(0, 256)) for channel in channels)
    hist = np.squeeze(hist)
    
    return hist
    

def phist(image, bin_count=25, height=8, bar_symbol="#", background_symbol=" ", col_sep="."):
    """
    Print the histogram of the given image.
    """
    
    h = hist(image=image, bin_count=bin_count)
    h = h / np.max(h)
    
    print("^")
    for n_row in range(height):
        col_strs = []
        for n_bin in range(bin_count):
            if h[n_bin] > (1.0 - (n_row + 1) / height):
                col_str = bar_symbol
            else:
                col_str = background_symbol
            col_strs.append(col_str)
        print("|" + col_sep.join(col_strs))
    print("+" + "-" * ((bin_count - 1) * (1 + len(col_sep)) + 1) + ">")
