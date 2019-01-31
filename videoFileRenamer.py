import os
import string
from apscheduler.schedulers.blocking import BlockingScheduler

morningDir = '/videos/morning'
dayDir = '/videos/day'

def videoFileRenamer(location):
    for fileName in os.listdir(location):
        newFileName = ''.join(c for c in fileName if c in string.printable)
        os.rename(os.path.join(location,fileName), os.path.join(src_dir, newFileName))



scheduler = BlockingScheduler()
scheduler.add_job(dlVideo, trigger='interval', hours=1, max_instances=1)
scheduler.start()