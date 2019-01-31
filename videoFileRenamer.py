import os
import string


morningDir = '/media/songftptodb/morning'
dayDir = '/media/songftptodb/day'

def videoFileRenamer(directory):
    for fileName in os.listdir(directory):
        newFileName = ''.join(c for c in fileName if c in string.printable)
        os.rename(os.path.join(directory,fileName), os.path.join(src_dir, newFileName))

videoFileRenamer(morningDir)
videoFileRenamer(dayDir)