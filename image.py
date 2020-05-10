from PIL import Image, ImageFilter

im = Image.open("./pokedex/bulbasaur.jpg")

print(im.format, im.size, im.mode)

filtered_im = im.filter(ImageFilter.BLUR)


im.show()
filtered_im.show()