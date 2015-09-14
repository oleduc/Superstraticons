Pillow Identicons
=======================

Github style identicons made easy.

Options:
- background : Color of the background of the identicon.
- grid_size : Size (pixels) of one side of the grid of the identicon excluding the border.
- cell_size : Size (pixels) of a cell inside the grid.
- border_size : Size (pixels) of the padding around the identicon grid.


Usage:

```python
from Identicon import Identicon

def main():
    i = Identicon()
    image = i.generate('foobar')

    # Do anything you want with the image instance.

    # Save it to the filesystem or something!
    with open('identicon.png', 'wb') as out:
        image.save(out, 'PNG')
```

This is just a cleaned, commented, python 3.4 and packaged version of [this open source project](https://github.com/evuez/identicons).

