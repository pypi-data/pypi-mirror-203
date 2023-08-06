import functools
import glob
import os.path
import pathlib
import tempfile
import time
import uuid

import cv2
import numpy as np

import dito.utils


def load(filename, color=None):
    """
    Load image from file given by `filename` and return NumPy array.

    If `color` is `None`, the image is loaded as-is. If `color` is `False`, a
    grayscale image is returned. If `color` is `True`, then a color image is
    returned, even if the original image is grayscale.

    The bit-depth (8 or 16 bit) of the image file will be preserved.
    """

    if isinstance(filename, pathlib.Path):
        filename = str(filename)

    # check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError("Image file '{}' does not exist".format(filename))

    # load image
    if filename.endswith(".npy"):
        # use NumPy
        image = np.load(file=filename)
    elif filename.endswith(".npz"):
        # use NumPy
        with np.load(file=filename) as npz_file:
            npz_keys = tuple(npz_file.keys())
            if len(npz_keys) != 1:
                raise ValueError("Expected exactly one image in '{}', but got {} (keys: {})".format(filename, len(npz_keys), npz_keys))
            image = npz_file[npz_keys[0]]
    else:
        # use OpenCV
        if color is None:
            # load the image as it is
            flags = cv2.IMREAD_ANYDEPTH | cv2.IMREAD_UNCHANGED
        else:
            # force gray/color mode
            flags = cv2.IMREAD_ANYDEPTH | (cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE)
        image = cv2.imread(filename=filename, flags=flags)

    # check if loading was successful
    if image is None:
        raise RuntimeError("Image file '{}' exists, but could not be loaded".format(filename))
    if not isinstance(image, np.ndarray):
        raise TypeError("Image file '{}' exists, but has wrong type (expected object of type 'np.ndarray', but got '{}'".format(filename, type(image)))

    return image


def load_multiple_iter(*args, color=None):
    filename_pattern = os.path.join(*args)
    filenames = sorted(glob.glob(filename_pattern))
    for filename in filenames:
        image = load(filename=filename, color=color)
        yield image


def load_multiple(*args, color=None):
    return list(load_multiple_iter(*args, color=color))


def save(filename, image, mkdir=True):
    """
    Save image `image` to file `filename`.

    If `mkdir` is `True`, the parent dir of the given filename is created
    before saving the image.
    """

    if isinstance(filename, pathlib.Path):
        filename = str(filename)

    if not isinstance(image, np.ndarray):
        raise RuntimeError("Invalid image (type '{}')".format(type(image).__name__))

    # create parent dir
    if mkdir:
        dito.utils.mkdir(dirname=os.path.dirname(filename))

    if filename.endswith(".npy"):
        # use NumPy
        np.save(file=filename, arr=image)
    elif filename.endswith(".npz"):
        # use NumPy
        np.savez_compressed(file=filename, arr_0=image)
    else:
        # use OpenCV
        cv2.imwrite(filename=filename, img=image)


def save_tmp(image):
    filename = os.path.join(tempfile.gettempdir(), "dito.save_tmp", "{}__{}.png".format(dito.utils.now_str(mode="readable"), str(uuid.uuid4()).split("-")[0]))
    save(filename=filename, image=image, mkdir=True)
    return filename


def decode(b, color=None):
    """
    Load image from the byte array `b` containing the *encoded* image and
    return NumPy array.

    If `color` is `None`, the image is loaded as-is. If `color` is `False`, a
    grayscale image is returned. If `color` is `True`, then a color image is
    returned, even if the original image is grayscale.

    The bit-depth (8 or 16 bit) of the image file will be preserved.
    """

    # byte array -> NumPy array
    buf = np.frombuffer(b, dtype=np.uint8)

    # flags - select grayscale or color mode
    if color is None:
        flags = cv2.IMREAD_UNCHANGED
    else:
        flags = cv2.IMREAD_ANYDEPTH | (cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE)

    # read image
    image = cv2.imdecode(buf=buf, flags=flags)

    return image


def encode(image, extension="png", params=None):
    """
    Encode the given `image` into a byte array which contains the same bytes
    as if the image would have been saved to a file.
    """

    # allow extensions to be specified with or without leading dot
    if not extension.startswith("."):
        extension = "." + extension

    # use empty tuple if no params are given
    if params is None:
        params = tuple()

    (_, array) = cv2.imencode(ext=extension, img=image, params=params)

    return array.tobytes()


class CachedImageLoader():
    def __init__(self, max_count=128):
        # decorate here, because maxsize can be specified by the user
        self.load = functools.lru_cache(maxsize=max_count, typed=True)(self.load)

    def load(self, filename, color=None):
        return load(filename=filename, color=color)

    def get_cache_info(self):
        return self.load.cache_info()

    def clear_cache(self):
        self.load.cache_clear()


class VideoSaver():
    """
    Convenience wrapper for `cv2.VideoWriter`.

    Main differences compared to `cv2.VideoWriter`:
    * the parent dir of the output file is created automatically
    * the codec can be given as a string
    * the frame size is taken from the first provided image
    * the sizes of all following images are checked - if they do not match the size of the first image, an exception is
      raised
    * images are converted to gray/color mode automatically
    """

    def __init__(self, filename, codec="MJPG", fps=30.0, color=True):
        self.filename = filename
        self.codec = codec
        self.fps = fps
        self.color = color

        if isinstance(self.filename, pathlib.Path):
            self.filename = str(self.filename)

        if (not isinstance(self.codec, str)) or (len(self.codec) != 4):
            raise ValueError("Argument 'codec' must be a string of length 4")

        self.frame_count = 0
        self.image_size = None
        self.writer = None

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.save()

    def get_fourcc(self):
        return cv2.VideoWriter_fourcc(*self.codec)

    def init_writer(self, image_size):
        self.image_size = image_size
        dito.utils.mkdir(os.path.dirname(self.filename))
        self.writer = cv2.VideoWriter(
            filename=self.filename,
            fourcc=self.get_fourcc(),
            fps=self.fps,
            frameSize=self.image_size,
            isColor=self.color,
        )

    def append(self, image):
        """
        Add frame `image` to the video.
        """
        image_size = dito.core.size(image=image)

        # create writer if this is the first frame
        if self.writer is None:
            self.init_writer(image_size=image_size)

        # check if the image size is consistent with the previous frames
        if image_size != self.image_size:
            raise ValueError("Image size '{}' differs from previous image size '{}'".format(image_size, self.image_size))

        # apply correct color mode
        if self.color:
            image = dito.core.as_color(image=image)
        else:
            image = dito.core.as_gray(image=image)

        self.writer.write(image=image)
        self.frame_count += 1

    def save(self):
        """
        This finishes the video.

        If `VideoSaver` is used via context manager, this is called automatically. Otherwise, it must be called
        manually.
        """
        if self.writer is not None:
            self.writer.release()

    def file_exists(self):
        return os.path.exists(path=self.filename)

    def get_file_size(self):
        return os.path.getsize(filename=self.filename)

    def print_summary(self, file=None):
        file_exists = self.file_exists()
        rows = [
            ["Output", ""],
            ["..Codec", self.codec],
            ["..Filename", self.filename],
            ["..Exists", file_exists],
            ["..Size", dito.utils.human_bytes(byte_count=self.get_file_size()) if file_exists else "n/a"],
            ["..Modified", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(filename=self.filename))) if file_exists else "n/a"],
            ["Frames", ""],
            ["..Size", self.image_size],
            ["..Color", self.color],
            ["..Count", self.frame_count],
        ]
        dito.utils.ptable(rows=rows, print_kwargs={"file": file})
