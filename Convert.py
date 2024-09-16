from PIL import Image

image = Image.open("Images/2024_09_10_08_45_IMG_6273.JPG")

gray_image = image.convert('L')

gray_image.save('Images/Convertis/my_pictureL.jpg')

gray_image.show()