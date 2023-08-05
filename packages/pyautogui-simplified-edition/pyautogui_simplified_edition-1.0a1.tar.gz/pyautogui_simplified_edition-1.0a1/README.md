# PyAutoGUI Simplified Edition

This is a simplified edition of the PyAutoGUI library that provides easy-to-use functions for screen automation.

PyAutoGUI is a cross-platform GUI automation Python module that can perform many functions, including mouse and keyboard control, taking screenshots, and locating images on the screen.

However, the library can be complex and difficult to use for beginners. The PyAutoGUI Simplified Edition provides simpler functions that are easier to use, but can still accomplish many of the same tasks as the original library.

## Installation

The package can be installed using pip:

```bash
pip install pyautogui_simplified_edition
```

## Usage

Here are the available functions in this package:

- `wait_until_found(image: str, timeout: float = 10.0, interval: float = 0.5, **kwargs) -> None`: waits until an image is found on the screen.
- `wait_until_not_found(image: str, timeout: float = 10.0, interval: float = 0.5, **kwargs) -> None`: waits until an image is not found on the screen.
- `find_in(image: str, region: Box | None = None, grayscale: bool = False, confidence: float = 0.9, **kwargs) -> Tuple[int, int]`: finds an image in a given region on the screen.
- `easy_find(image: str, grayscale: bool = True, confidence: float = 0.75, **kwargs) -> Box | None`: finds an image on the screen using easier parameters.
- `hard_find(image: str, grayscale: bool = False, confidence: float = 0.93, **kwargs) -> Box | None`: finds an image on the screen using harder parameters.
- `find_any(images: List[str], grayscale: bool = False, confidence: float = 0.9, **kwargs) -> Tuple[str, Box]`: finds any of the given images on the screen.
- `find_any_center(images: List[str], grayscale: bool = False, confidence: float = 0.9, **kwargs) -> Tuple[str, Tuple[int, int]]`: finds the center of any of the given images on the screen.
- `take(image: str, region: Box | None = None, **kwargs) -> None`: takes a screenshot of a given region on the screen.

For detailed information on the usage of each function, please refer to the docstrings in the code.

## Acknowledgements

This package is based on the PyAutoGUI library, which can be found at https://pypi.org/project/PyAutoGUI/.

## License

This package is licensed under the MIT License. Please see the LICENSE file for more information.