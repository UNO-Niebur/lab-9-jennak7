# Lab 9 – Image Processing
# Name:Jenna Kramer
# Date:04/01/26
# Assignment:Lab 9

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    #values must stay between 0 and 255
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            pixels[x, y] = red, blue, green, alpha 
    
    # TODO: Loop through every pixel and swap green and blue values

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            red = max(0, red - amount)
            red = min(255, red)
            green = max(0, green - amount)
            green = min(255, green)
            blue = max(0, blue - amount)
            blue = min(255, blue)
            pixels[x, y] = red, green, blue, alpha

    # TODO: Loop through every pixel and reduce RGB values by amount
    # Make sure values do not go below 0

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    # swapGreenBlue(myImg)
    darken(myImg, 75)


if __name__ == "__main__":
    main()
