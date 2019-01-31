import os
import string


morningDir = '/media/songftptodb/morning'
dayDir = '/media/songftptodb/day'

def videoFileRenamer(location):
    for fileName in os.listdir(location):
        newFileName = ''.join(c for c in fileName if c in string.printable)
        os.rename(os.path.join(location,fileName), os.path.join(src_dir, newFileName))



videoFileRenamer(morningDir)
videoFileRenamer(dayDir)