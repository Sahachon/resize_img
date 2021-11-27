# python resize.py --input=img --output=output/

import cv2,os
import argparse
import fnmatch
img_num = 1
img_numout = 1

nameList = []

def addlist(input):
    try:
        listOfFiles = os.listdir(input)
        # os.system("dir")
        pattern = "*.jpg"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                # print (entry)
                nameList.append(entry)
        print(nameList)
    except:
        print("File not found!")

def main(input,output):   
    # img_num = len(nameList)
    for i in nameList:
        img_num=len(nameList)-1

        img = cv2.imread(input+"/"+i, cv2.IMREAD_UNCHANGED)

        print("img input "+str(img_num))
        print('Original Dimensions : ', img.shape)

        resized = cv2.resize(img, None, fx=0.25, fy=0.25)

        # #resize image
        # width = 1280
        # height = 720
        # dim = (width, height)
        # resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(output+"/resize_"+i, resized)

        print("img output "+i+'_'+str(img_num)+'.jpg')
        print('Resized Dimensions : ', resized.shape)

      
        print("----------------------------------")

        print('\n')
        # cv2.destroyAllWindows()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="set path to the input image")
ap.add_argument("-o", "--output",  required=True,
                help="set path to the output image")
args = vars(ap.parse_args())

# image = cv2.imread(args["image"])
imput = (args["input"])
output = (args["output"])
print("\n")
print((args["input"]))
print((args["output"]))
print("\n")

if __name__ == "__main__":

    addlist((args["input"]))
    main( (args["input"]),(args["output"]))
