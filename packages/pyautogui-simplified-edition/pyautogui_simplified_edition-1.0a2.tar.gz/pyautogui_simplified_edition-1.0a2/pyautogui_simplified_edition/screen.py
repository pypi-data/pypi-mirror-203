import time
from typing import List, Tuple

import pyautogui as py

Box = Tuple[int, int, int, int]


def wait_until_found(image: str,
                     timeout: float = 10.0,
                     interval: float = 0.5,
                     **kwargs) -> None:
    """
    Wait until the image is found on the screen.
    :param image: Image to be found.
    :param timeout: Time to wait before giving up.
    :param interval: Time interval between each search.
    :return: None
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if py.locateOnScreen(image, **kwargs):
            return
        time.sleep(interval)
    raise TimeoutError(f"Image {image} not found in {timeout} seconds.")


def wait_until_not_found(image: str,
                         timeout: float = 10.0,
                         interval: float = 0.5,
                         **kwargs) -> None:
    """
    Wait until the image is not found on the screen.
    :param image: Image to be found.
    :param timeout: Time to wait before giving up.
    :param interval: Time interval between each search.
    :return: None
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not py.locateOnScreen(image, **kwargs):
            return
        time.sleep(interval)
    raise TimeoutError(f"Image {image} still found in {timeout} seconds.")


def find_in(image: str,
            region: Box | None = None,
            grayscale: bool = False,
            confidence: float = 0.9,
            **kwargs) -> Tuple[int, int]:
    """
    Find the image in the region.
    :param image: Image to be found.
    :param region: Region to search in.
    :param grayscale: Whether to search in grayscale.
    :param confidence: Confidence of the search.
    :return: Center of the image.
    """
    location = py.locateCenterOnScreen(image,
                                       region=region,
                                       grayscale=grayscale,
                                       confidence=confidence,
                                       **kwargs)
    if not location:
        raise ValueError(f"Image {image} not found.")
    return location


def easy_find(image: str,
              grayscale: bool = True,
              confidence: float = 0.75,
              **kwargs) -> Box | None:
    """
    Find the image in the whole screen but with easy parameters.
    :param image: Image to be found.
    :param grayscale: Whether to search in grayscale.
    :param confidence: Confidence of the search.
    :return: Center of the image.
    """
    return py.locateOnScreen(image,
                             grayscale=grayscale,
                             confidence=confidence,
                             **kwargs)


def hard_find(image: str,
              grayscale: bool = False,
              confidence: float = 0.93,
              **kwargs) -> Box | None:
    """
    Find the image in the whole screen but with hard parameters.
    :param image: Image to be found.
    :param grayscale: Whether to search in grayscale.
    :param confidence: Confidence of the search.
    :return: Center of the image.
    """
    return py.locateOnScreen(image,
                             grayscale=grayscale,
                             confidence=confidence,
                             **kwargs)


def find_any(images: List[str],
             grayscale: bool = False,
             confidence: float = 0.9,
             **kwargs) -> Tuple[str, Box]:
    """
    Find any of the images in the whole screen.
    :param images: List of images to be found.
    :param grayscale: Whether to search in grayscale.
    :param confidence: Confidence of the search.
    :return: Tuple containing the name of the found image and its center location.
    """
    for image in images:
        location = py.locateOnScreen(image,
                                     grayscale=grayscale,
                                     confidence=confidence,
                                     **kwargs)
        if location:
            return (image, location)
    raise ValueError(f"None of the images {images} found.")


def find_any_center(images: List[str],
                    grayscale: bool = False,
                    confidence: float = 0.9,
                    **kwargs) -> Tuple[str, Tuple[int, int]]:
    """
    Find any of the images centers in the whole screen.
    :param images: List of images to be found.
    :param grayscale: Whether to search in grayscale.
    :param confidence: Confidence of the search.
    :return: Tuple containing the name of the found image and its center location.
    """
    for image in images:
        location = py.locateCenterOnScreen(image,
                                           grayscale=grayscale,
                                           confidence=confidence,
                                           **kwargs)
        if location:
            return (image, location)
    raise ValueError(f"None of the images {images} found.")


def take(image: str, region: Box | None = None, **kwargs) -> None:
    """
    Take a screenshot of the region.
    :param image: Image to be saved.
    :param region: Region to take screenshot from.
    :return: None
    """
    py.screenshot(image, region=region, **kwargs)
