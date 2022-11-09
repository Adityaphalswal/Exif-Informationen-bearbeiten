import pandas as pd
from iptcinfo3 import IPTCInfo
import os
filenames = []
header = ['Filename', 'Description', 'Keywords', 'Categories',
          'Editorial', 'Mature Content', 'illustration']
Allkeywords = []
folder_dir = "E:\\Christmas\\wallpaper backgrounds"
for images in os.listdir(folder_dir):
    if (images.endswith(".jpeg")):
        imagekeywords = []
        a = []
        keywords = IPTCInfo(images)
        imagekeywords.append(keywords['keywords'])
        for j in range(len(imagekeywords[0])):
            y = imagekeywords[0][j].decode()
            a.append(y)
        Allkeywords.append(a)
        filenames.append(images)

finalfile = []
finalfile.append(header)
for x in range(len(filenames)):
    finalfile2 = []
    finalfile2.append(filenames[x])
    finalfile2.append(Allkeywords[x])
    finalfile.append(finalfile2)

df = pd.DataFrame(finalfile)
df.to_csv('wallpaer.csv')
