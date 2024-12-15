import pandas as pd
import numpy as np
import os
from PIL import Image


def getFileList(imgFolderPath,currentDir):
    '''When passed the path of the folder containing all the images it will return a list of the files within
    alongside a list of the digits (as integers) that the files correspond to\n
    
    This assumes a naming convention of (digit)_filename\n
    
    Requires the currend directory as well so as to return to it'''

    labels = []                                         # Initialises list of labels
    pathlist = []

    os.chdir(imgFolderPath)                             # Changes current working directory to the path specified
    filelist = os.listdir()                             # Generates list of filenames as strings

    
    for file in filelist:                               # Appends the first digit of the filenames to labels
        labels.append(file[0])
        pathlist.append(currentDir+"/"+imgFolderPath+"/"+file)

    os.chdir(currentDir)

    return filelist, pathlist, labels


def imgToDataframe(filename=str):

    '''takes a bitmap filename as a string and converts it to a dataframe of
    1s and 0s corresponding to black or white pixels'''

    img = Image.open(filename).convert('L')             # Uses PIL to open filename (needs to be bitmap) and convert it from RGB to greyscale
    imgArr = np.array(img)                              # Makes numpy arrag of bitmap
    bwArr = np.where(imgArr == 255, 0,1)                # Where black pixel give value of 1 else 0
    df = pd.DataFrame(bwArr)                            # Makes dataframe of 1 and zero array which is returned

    return df