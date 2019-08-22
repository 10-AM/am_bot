import json
import random
import datetime
import time
import os

class Data():
    def __init__(self):
        with open("am_bot_data/data.json", "r") as dataJson:
            self.desc_dict = json.loads(dataJson.read())['description']
        self.start_time = time.time()

    def get_bot_status(self):
        total_line = 0
        
        folder = '.'
        size = 0
        for (path, dirs, files) in os.walk(folder):
            for file in files:
                filename = os.path.join(path, file)
                if '.pyc' in filename or '.git/' in filename:
                    continue
                print(filename)
                if 'py' in filename:
                    total_line += len((open(filename, encoding='utf-8').readlines()))
                size += os.path.getsize(filename)
        str_size = "%0.1f MB" % (size / (1024*1024.0))
        if str_size == '0.0 MB':
            str_size = "%0.1f KB" % (size / 1024.0)
        running_time = self.convert_running_time(str(datetime.timedelta(seconds=(time.time() - self.start_time))))
        result = dict()
        result["lines"] = total_line
        result["size"] = str_size
        result["time"] = running_time
        return result
    
    def convert_running_time(self, t):
        f = "{day}일 {hour}시간 {minute}분"
        print(t)
        if "days" in t:
            _days = t.split(',')[0]
            _time = t.split(',')[1]
            _day = _days.split(' ')[0]
            _hour = _time.split(':')[0]
            _minute = _time.split(':')[1]
            return f.format(day=_day, hour=_hour, minute=_minute)
        else:
            _times = t.split(':')
            return f.format(day="0", hour=_times[0], minute=_times[1])