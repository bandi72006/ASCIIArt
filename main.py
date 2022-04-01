#Bandar Al Aish - bandi72006

from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import time
import numpy as np
import pyvirtualcam #Credits: https://github.com/letmaik/pyvirtualcam

bgColour = input("Enter background colour (b/w):    ").lower()
pictureOrVideo = input("Picture or video or camera? (p/v/c):    ").lower()


#                Darkest                                                         Lighest  (On black background)
characterString = ".'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"
ASCIIChars = []

for i in characterString:
    ASCIIChars.append(i)

if bgColour == "w":
    ASCIIChars.reverse()

#                                              How much times a letter repeats
def convertImageToASCII(image, width, height, letterDensity):

    colourValues = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions of image
    ASCIIText = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions of image

    for y in range(height):
        for x in range(width):
            colourValues[y][x] = sum(image.getpixel((x,y))) #Adds R, G, and B values 
            ASCIIText[y][x] = ASCIIChars[colourValues[y][x]//69]*letterDensity
    
    return ASCIIText


def printASCIIArray(array):
    for column in array:
        print("".join(column))
        


if pictureOrVideo == "p":
    image = Image.open("picture.png")
    image = image.convert("RGB")
    image = image.resize((300,300))
    width, height = image.size
    

    ASCIIImage = convertImageToASCII(image, width, height, 2)

    file = open("ASCII.txt", "w")

    printASCIIArray(ASCIIImage)
    for column in ASCIIImage:
        file.writelines("".join(column) + "\n")

    file.close()


elif pictureOrVideo == "v":
    vid = cv2.VideoCapture("videoJDSO.mp4")

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
        ASCIIFrame = convertImageToASCII(image, width, height, 2)
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

    for i in range(frameCount): #Deletes all images in frame folder
        os.remove("videoFrames/videoFrame" + str(i) +".png")
    
    os.rmdir("videoFrames") #deletes videoFrames folder

    os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS

    print("Duration of video: " + str(videoDuration))
    print("Duration of display: " + str(finishTime))

elif pictureOrVideo == "c":
    quality = 1 #standard = 1
    outputHeight = int(400*quality)
    outputWidth = int(600*quality)
    
    font = ImageFont.truetype('FreeMono.ttf', 1)
    with pyvirtualcam.Camera(width=outputWidth, height=outputHeight, fps=20) as cam:
        vid = cv2.VideoCapture(0)
        #vid = cv2.VideoCapture("videoJDSO.mp4")
        #print(f'Using virtual camera: {cam.device}')
        while True:
            ret, image = vid.read()
            #cv2.imshow('my webcam', image)
            #if cv2.waitKey(1) == 27: 
            #    break  # esc to quit

            image = Image.fromarray(image) #converts CV2 image to Pillow image
            image = image.convert("RGB")

            #image = image.resize((426, 240)) #240p
            image = image.resize((int(100*quality), int(100*quality)))

            width, height = image.size
            ASCIIFrame = convertImageToASCII(image, width, height, 1)
            print(ASCIIFrame)
            
            imagePNG = Image.new('RGB', (outputWidth, outputHeight))

            imageGraphics = ImageDraw.Draw(imagePNG)

            for i in range(len(ASCIIFrame)):
                imageGraphics.text((0, i*4), "".join(ASCIIFrame[i]), fill=(255, 255, 255))
            
            
            #imagePNG.show()

            imagePNG.save("imagePNG.png")

            

            """os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS
            printASCIIArray(ASCIIFrame)
            time.sleep(1/60)"""
            
            #success, frame = vid.read("imagePNG.png")
            frame = Image.open("imagePNG.png")
            frame = np.asarray(frame)
            frame = frame.astype(np.uint8)
            
            cam.send(frame)
            cam.sleep_until_next_frame()


else:
    print("Error: Invalid option. Please enter v, p or c")
