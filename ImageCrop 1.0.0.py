from PIL import Image
import os

def check_black_pixel(px):
    return px[0] <= 10 and px[1] <= 10 and px[2] <= 10

def find_crop_cords(Image):
    px = Image.load()
    x,y = 0,0
    px_cords = 0,0
    size = Image.size
    while check_black_pixel(px[px_cords]) == True:
        x+=1
        px_cords = x,y
    top_corner_px_cords = x-1,y

    x, y = Image.size[0]-1,Image.size[1]-1
    px_cords = x,y
    while check_black_pixel(px[px_cords]) == True:
        x-=1
        px_cords = x,y
    bottom_corner_corner_px_cords = x+1,y

    cords = (top_corner_px_cords[0], top_corner_px_cords[1], bottom_corner_corner_px_cords[0] , bottom_corner_corner_px_cords[1])
    return cords


path = input("enter the path: ")
os.chdir(path)

image_amount = 0
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.png'):
        image_amount += 1
print(str(image_amount) + 'images found')

if input("continue? ").startswith("y"): print("continueing")
else: quit( )

done_amount = 0
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.png'):
        try:
            image = Image.open(f)
            ImageCropped = image.crop(find_crop_cords(image))
            ImageCropped.save(str(f))
            done_amount += 1
            print('edited ' + str(done_amount) + '/' + str(image_amount))
        except:
            done_amount += 1
            print('failed ' + str(done_amount) + '/' + str(image_amount))