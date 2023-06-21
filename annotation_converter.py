import os
import xml
import xml.etree.ElementTree as ET


mytree = ET.parse('SceneTrialTrain/locations_simple.xml')
myroot = mytree.getroot()

# for image in myroot.findall("image/imageName"):
     
#      image.text = image.text.split("/")[1]

# mytree.write("test.xml")


for r, d, f in os.walk("SceneTrialTrain/"):
        for file in f:
            if file.endswith(".jpg"):
                try:
                    image = myroot.findall(f"image[imageName='{file}']")[0]

                    resolution = image.find("resolution")
                    totalWidth = int(resolution.attrib["x"])
                    totalHeight = int(resolution.attrib["y"])

                    coordinates = image.find("taggedRectangles/taggedRectangle")

                    x = int(coordinates.attrib["x"].split(".")[0])/totalWidth
                    y = int(coordinates.attrib["y"].split(".")[0])/totalHeight
                    width = int(coordinates.attrib["width"].split(".")[0])/totalWidth
                    height = int(coordinates.attrib["height"].split(".")[0])/totalHeight

                    with open(f"SceneTrialTrain/{file[0:-4]}" + ".txt", "w") as textFile:

                        textFile.write(f"{x} {y} {width} {height}")

                    print(file)
                except Exception as err:
                    print("error")