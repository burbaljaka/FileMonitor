from celery import shared_task
from django.conf import settings

import os
from fmonitor.celery import app
from django.core.cache import cache
from .signals import reload_dir

# import time
# from datetime import datetime, timedelta
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
# path_to_watch = '.'
#
#
# class MyHandler(FileSystemEventHandler):
#     def __init__(self):
#         self.last_modified = datetime.now()
#
#     def on_modified(self, event):
#         if datetime.now() - self.last_modified < timedelta(seconds=1):
#             return
#         else:
#             self.last_modified = datetime.now()
#         print(f'event type: {event.event_type}  path : {event.src_path}')
#         reload_dir.send(path=path_to_watch, sender=self)
#
# @shared_task
# def file_monitor():
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path=path_to_watch, recursive=False)
#     observer.start()
#
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

path_to_watch = '.'

@shared_task
def file_monitor():
    with os.scandir(path_to_watch) as dir_entries:
        result = {}
        for entry in dir_entries:
            info = entry.name
            result[info] = {}
            result[info]['size'] = entry.stat().st_size
            result[info]['modified at'] = entry.stat().st_mtime

    previous = cache.get('res')
    if previous:
        if previous != str(result):
            reload_dir.send(path=path_to_watch, sender=previous)

    cache.set('res', str(result), 20)
