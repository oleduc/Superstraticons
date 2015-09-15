from PIL import Image, ImageDraw
from hashlib import sha224


class Identicon(object):
    def __init__(self, background='#fff', grid_size=9, cell_size=10, border_size=10):
        """
        Parameters
        ----------
        background : Color of the background of the identicon.
        grid_size : Size (pixels) of one side of the grid of the identicon excluding the border.
        cell_size : Size (pixels) of a cell inside the grid.
        border_size : Size (pixels) of the padding around the identicon grid.
        """
        self.background = background
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.border_size = border_size
        self.height = self.width = self.border_size * 2 + self.cell_size * self.grid_size

    @staticmethod
    def digest(substrate):
        return int(sha224(substrate.encode('utf-8')).hexdigest(), 16)

    def calculate(self, sha256sum):
        """
        Calculates and draws the identicon.

        First three bytes of the sha256sum are used to generate the color of the cells.
        Subsequent bytes of the sha256sum are used to place the cells on one half of the cell.
        Identicon is then mirrored (No swasticas whoohoo!).

        Parameters
        ----------
        sha256sum : Shasum of the substrate used to generate the identicon
        """
        # Create the PIL image
        image = Image.new('RGBA', (self.width, self.height), self.background)
        drawing = ImageDraw.Draw(image)

        # Compute the color from the three first bytes of the "sha256sum"
        color = (sha256sum & 0xff, sha256sum >> 8 & 0xff, sha256sum >> 16 & 0xff)

        # Skip the first three bytes
        sha256sum >>= 24
        # init cell position
        square_x = square_y = 0

        for x in range(self.grid_size * (self.grid_size + 1) // 2):
            if sha256sum & 1:
                # Place a cell
                x = self.border_size + square_x * self.cell_size
                y = self.border_size + square_y * self.cell_size
                drawing.rectangle(
                    (x, y, x + self.cell_size, y + self.cell_size),
                    fill=color,
                    outline=color
                )

                # Mirror the cell
                x = self.border_size + (self.grid_size - 1 - square_x) * self.cell_size
                drawing.rectangle(
                    (x, y, x + self.cell_size, y + self.cell_size),
                    fill=color,
                    outline=color
                )

            sha256sum >>= 1
            square_y += 1

            # Done with first column
            if square_y == self.grid_size:
                square_y = 0
                square_x += 1

        return image

    def generate(self, substrate):
        return self.calculate(sha256sum=self.digest(substrate))
