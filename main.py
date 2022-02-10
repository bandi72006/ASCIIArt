from turtle import bgcolor
from PIL import Image
import os
import cv2
import time

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
    vid = cv2.VideoCapture("video.mp4")

    frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) #Number of frames in video
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    frameCount = 0
    videoDuration = frames/fps

    os.mkdir("videoFrames") #Creates new folder for all frames
    
    print("Rendering...")

    print("Splitting video into frames...")
    while frameCount < frames:
        success,image = vid.read()
        image = cv2.resize(image, (int(640/image.shape[1]*100), int(360/image.shape[0]*100)), interpolation = cv2.INTER_AREA)
        cv2.imwrite("videoFrames/videoFrame" + str(frameCount) + ".png", image)

        frameCount += 1

        """print("Rendering frame " + str(frameCount+1) + " of " + str(frames))

        success,image = vid.read()
        image = Image.fromarray(image) #converts CV2 image to Pillow image
        image = image.convert("RGB")
        image = image.resize((426, 240))

        ASCIIFrame = convertImageToASCII(image, image.size[0], image.size[1])

        frame = open("videoFrames/videoFrame" + str(frameCount) + ".txt", "w")
        for column in ASCIIFrame:
            frame.writelines("".join(column) + "\n")

        frame.close()

        frameCount += 1"""

    print("Converting frames into ASCII...")

    frames = []
    for i in range(frameCount):
        image = Image.open("videoFrames/videoFrame" + str(i) + ".png")
        width, height = image.size
        ASCIIFrame = convertImageToASCII(image, width, height)
        frames.append(ASCIIFrame)

    startTime = time.time() 

    for i in range(frameCount): #Prints each image from frame folder
        
        """ASCIIFrame = open("videoFrames/videoFrame" + str(i) +".txt", "r")

        os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS

        printASCIIArray(ASCIIFrame)"""
        """image = Image.open("videoFrames/videoFrame" + str(i) + ".png")
        width, height = image.size
        ASCIIFrame = convertImageToASCII(image, width, height)"""

        os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS

        printASCIIArray(frames[i])
        
        time.sleep(1/60)


    finishTime = time.time() - startTime #calculates time to display all frames

    print("Duration of video: " + str(videoDuration))
    print("Duration of display: " + str(finishTime))

    for i in range(frameCount): #Deletes all images in frame folder
        os.remove("videoFrames/videoFrame" + str(i) +".png")
    
    os.rmdir("videoFrames") #deletes videoFrames folder

    os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS


else:
    print("Error: Invalid option. Please enter v or p")




