# CS50P 2022 - PSET 6
# CS50 P-Shirt

"""
After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

    • in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    • in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per
pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with
Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

    • if the user does not specify exactly two command-line arguments,
    • if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    • if the input’s name does not have the same extension as the output’s name, or
    • if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py.
No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!
"""
from PIL import Image, ImageOps
import sys


def main():
    """
    Main function checks that command-line arguments meet requirements, then pastes an image of a CS50 t-shirt onto the user provided portrait,
    saving the result as a new image file
    """

    # Check that exactly 3 command-line arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python  shirt.py  before.jpg  after.jpg")

    # Check that the 2nd and 3rd command-line arguments have both have file extensions of either ".jpg", ".jpeg", or ".png"
    elif not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")) or not ((sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png"))):
        sys.exit("Only .jpg, .jpeg, or .png files may be used")

    # Check that the 2nd and 3rd command-line arguments have matching file extensions
    elif sys.argv[1].strip().split(".")[1] != sys.argv[2].strip().split(".")[1]:
        sys.exit("Input and output files have different extensions")

    # Begin process of pasting t-shirt onto portrait image
    else:
        try:
            user_img = Image.open(sys.argv[1]) # Read user-provided image into memory
            user_img_copy = ImageOps.fit(user_img, (600, 600)) # Re-size user-provided image and assign to variable

            shirt_img = Image.open("shirt.png") # Read t-shirt image into memory
            shirt_img_copy = ImageOps.fit(shirt_img, (600, 600)) # Re-size t-shirt image to match dimensions of user's image

            user_img_copy.paste(shirt_img_copy, mask=shirt_img_copy) # Paste t-shirt image onto user-provided image and mask out transparent background of t-shirt image

            user_img_copy.save(sys.argv[2]) # Save final image

        # Check that command-line argument files exist
        except FileNotFoundError:
            sys.exit("File does not exist.")

if __name__ == "__main__":
    main()