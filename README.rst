Pillow Identicons
=======================

Github style identicons made easy.

Installation:


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

