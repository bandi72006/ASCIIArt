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


if pictureOrVideo == "p":
    image = Image.open("picture.png")
    image = image.convert("RGB")
    width, height = image.size

    ASCIIImage = convertImageToASCII(image, width, height)

    file = open("ASCII.txt", "w")

    for column in ASCIIImage:
        print("".join(column))
        file.writelines("".join(column) + "\n")

    file.close()


elif pictureOrVideo == "v":
    cap = cv2.VideoCapture("video.mp4")
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameCount = 0
    while frameCount < frames:
        success,image = cap.read()
        cv2.imwrite("videoFrame.png", image)
        image = Image.open("videoFrame.png")
        image = image.resize((213, 120))

        width, height = image.size
        
        ASCIIFrame = convertImageToASCII(image, width, height)

        os.system("cls" if os.name == "nt" else "clear") #Clears terminal based on OS

        for column in ASCIIFrame:
            print("".join(column))

        frameCount += 1

else:
    print("Error: Invalid option. Please enter v or p")




