import os
from apscheduler.schedulers.blocking import BlockingScheduler


dirname = os.path.dirname(__file__)
path = (dirname + '/videos')
bad_chars = [ '$', '#', '!', '"', '%', ')', '(', '[', ']', '@', '=', '☃', '', '', '', '♥', '»', '', '◐', 'ネ',
            'マ', 'ノ', 'ッ', 'ト', '・', ' ', '☾', '☀', '/', '|']

def videoFileRenamer():
    for dir, subdir, files in os.walk(path):
        for file in files:
            os.rename(os.path.join(dir,file), os.path.join(dir, "".join(filter(lambda x:x not in bad_chars, file))))


scheduler = BlockingScheduler()
scheduler.add_job(videoFileRenamer, trigger='interval', hours=1, max_instances=1)
scheduler.start()