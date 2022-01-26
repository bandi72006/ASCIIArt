from PIL import Image

bgColour = input("Enter background colour (b/w):    ").lower()

#                Darkest                                                         Lighest  (On black background)
characterString = ".'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"
ASCIIChars = []
for i in characterString:
    ASCIIChars.append(i)
if bgColour == "w":
    ASCIIChars.reverse()

image = Image.open("picture.png")
image = image.convert("RGB")
width, height = image.size



colourValues = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions ofimage
ASCIIText = [[[None] for i in range(width)] for j in range(height)] #Creates empty 2D array with dimensions ofimage

for y in range(height):
    for x in range(width):
        colourValues[y][x] = sum(image.getpixel((x,y))) #Adds R, G, and B values 
        ASCIIText[y][x] = ASCIIChars[colourValues[y][x]//69]*2

file = open("ASCII.txt", "w")

for column in ASCIIText:
    print("".join(column))
    file.writelines("".join(column) + "\n")


file.close()




