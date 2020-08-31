import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
import pickle
import datetime as dt
from apscheduler.schedulers.blocking import BlockingScheduler
import ssl
import requests

def get_traffic():
    app_id = "sfKZJRyGP8KpHvHWsqzO"
    app_code = "G7-OZu4Rml9nM7kBPmDBqH2qHQqAbjsYuDbtVNtQUIs"
    fname=str(dt.datetime.now())[:19].replace(":","-")
    base="https://traffic.hereapi.cn/traffic/6.2/flow.xml"+\
    "?app_id="+app_id+\
    "&app_code="+app_code+\
    "&bbox=-7.604302,110.191991;-7.964878,110.530623"+\
    "&responseattributes=sh,fc"


    topLeft = "-7.604302, 110.191991"
    buttomRight = "-7.964878, 110.530623"
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urlopen(base,context=gcontext)
    data=json.load(response)
    with open(fname+".p", 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    print("Success "+fname)
    # try:
    #     gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    #     response = urlopen(base,context=gcontext)
    #     data=json.load(response)
    #     with open(fname+".p", 'wb') as fp:
    #         pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    #     print("Success "+fname)
    # except:
    #     print("Failed "+fname)

if __name__=="__main__":

  get_traffic()
