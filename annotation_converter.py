import os
import xml
import xml.etree.ElementTree as ET


mytree = ET.parse('ICDAR_2003/SceneTrialTrain/locations.xml')
myroot = mytree.getroot()

for r, d, f in os.walk("ICDAR_2003/SceneTrialTrain/apanar_06.08.2002/"):
        for file in f:
            try:
                image = myroot.findall(f"image[imageName='apanar_06.08.2002/{file}']")[0]

                resolution = image.find("resolution")
                totalWidth = int(resolution.attrib["x"])
                totalHeight = int(resolution.attrib["y"])

                coordinates = image.find("taggedRectangles/taggedRectangle")

                x = int(coordinates.attrib["x"].split(".")[0])/totalWidth
                y = int(coordinates.attrib["y"].split(".")[0])/totalHeight
                width = int(coordinates.attrib["width"].split(".")[0])/totalWidth
                height = int(coordinates.attrib["height"].split(".")[0])/totalHeight

                with open(file[0:-4] + ".txt", "w") as textFile:

                    textFile.write(f"{x} {y} {width} {height}")

                print(file)
            except Exception as err:
                 print("error")