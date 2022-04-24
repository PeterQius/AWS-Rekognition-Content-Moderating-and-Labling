from PIL import Image

filename = '1.jpg'
img = Image.open(filename)
size = img.size
#print(size)

weight = int(size[0] // 2)
height = int(size[1])
#print(weight, height)

for j in range(1):
    for i in range(2):
        box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
        region = img.crop(box)
        region.save('{}{}.png'.format(j, i))