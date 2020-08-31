import numpy as np
from urllib.request import urlopen
import json
import pickle
import datetime as dt
from apscheduler.schedulers.blocking import BlockingScheduler
import ssl

def get_traffic():
    api_key = "sEBxx1IjRT_igcq9cdtQiPBA_iB3_Wx9Ze8LfEKPy6I"
    fname=str(dt.datetime.now())[:19].replace(":","-")
    topLeft1 = "-7.604302"
    topLeft2 = "110.191991"
    buttomRight1 = "-7.964878"
    buttomRight2 = "110.530623"
    
    base = "https://traffic.ls.hereapi.com/traffic/6.2/flow.json"+\
    "?bbox="+topLeft1+"%2C"+topLeft2+"%3B"+buttomRight1+"%2C"+buttomRight2+"&"+\
    "apiKey="+ api_key

    try:
        response = urlopen(base)
        data=json.load(response)
        with open(fname+".p", 'wb') as fp:
            pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
        print("Success "+fname)
    except:
        print("Failed "+fname)

if __name__=="__main__":
#   sched = BlockingScheduler()
#   sched.add_job(get_traffic, 'cron', day_of_week='*', hour='*', 
#                 minute='*')
#   sched.start()
    get_traffic()