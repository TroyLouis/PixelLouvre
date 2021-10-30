from PIL import Image
import os


def main():
    filePath = '/Users/troy/Desktop/LouvreImages2 copy'
    outPath = '/Users/troy/Desktop/PixelizedImages_32x32'
    for image in os.listdir(filePath):
        try:
            img = Image.open(filePath + '/'+ image)
        except:
            print(image)
            pass
        imgSmall = img.resize((32,32))
        left = 1
        top = 1
        right = 31
        bottom = 31
        cropImgSmall = imgSmall.crop((left, top, right, bottom))
        result = cropImgSmall.resize(img.size, Image.NEAREST)
        try:
            result.save(outPath+'/'+image)
        except:
            print(image)
            pass

if __name__ == '__main__':
    main()