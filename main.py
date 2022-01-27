from PIL import Image
import os
import cv2

bgColour = input("Enter background colour (b/w):    ").lower()
pictureOrVideo = input("Picture or video? (p/v):    ").lower()

#                Darkest                                                         Lighest  (On black background)
characterString = ".'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"
ASCIIChars = []

for i in characterString:
    ASCIIChars.append(i)

if bgColour == "w":
    ASCIIChars.reverse()

def convertImageToASCII(image, width, height):

    colourValues = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions of image
    ASCIIText = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions of image

    for y in range(height):
        for x in range(width):
            colourValues[y][x] = sum(image.getpixel((x,y))) #Adds R, G, and B values 
            ASCIIText[y][x] = ASCIIChars[colourValues[y][x]//69]*2
    
    return ASCIIText


def printASCIIArray(array):
    for column in array:
        print("".join(column))
        


if pictureOrVideo == "p":
    image = Image.open("picture.png")
    image = image.convert("RGB")
    width, height = image.size

    ASCIIImage = convertImageToASCII(image, width, height)

    file = open("ASCII.txt", "w")

    printASCIIArray(ASCIIImage)
    for column in ASCIIImage:
        file.writelines("".join(column) + "\n")

    file.close()


elif pictureOrVideo == "v":
    cap = cv2.VideoCapture("testVideo.mp4")
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #Number of frames in video
    frameCount = 0
    os.mkdir("videoFrames") #Creates new folder for all frames
    
    while frameCount < frames:
        success,image = cap.read()
        image = cv2.resize(image, (int(213/image.shape[1]*100), int(120/image.shape[0]*100)), interpolation = cv2.INTER_AREA)
        cv2.imwrite("videoFrames/videoFrame" + str(frameCount) + ".png", image)

        frameCount += 1


    for i in range(frameCount): #Prints each image from frame folder
        image = Image.open("videoFrames/videoFrame" + str(i) + ".png")
        width, height = image.size
        ASCIIFrame = convertImageToASCII(image, width, height)

        os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS

        printASCIIArray(ASCIIFrame)

    for i in range(frameCount): #Deletes all images in frame folder
        os.remove("videoFrames/videoFrame" + str(i) +".png")
    
    os.rmdir("videoFrames") #deletes videoFrames folder


else:
    print("Error: Invalid option. Please enter v or p")




