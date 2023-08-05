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

Here are some available functions in this package:

```py
import pyautogui_simplified_edition.screen as screen

# Wait until an image is found on the screen
pyse.wait_until_found('example.png')

# Find an image in a specific region
location = pyse.find_in('example.png', region=(100, 100, 500, 500))

# Find any of a list of images on the screen
image, location = pyse.find_any(['example1.png', 'example2.png'])

# Take a screenshot and save it to a file
pyse.take('screenshot.png')
```

For detailed information on the usage of each function, please refer to the docstrings in the code.

## Acknowledgements

This package is based on the PyAutoGUI library, which can be found at https://pypi.org/project/PyAutoGUI/.

## License

...