import json
import pandas as pd

from datetime import date, datetime

from modules.helpers.pgdb import conn 
from modules.helpers.logger import getLogger
from modules.models.indexs import Data

logger = getLogger("uploads")

def uploadDatas(pic, file):
    cur = conn.cursor()
    dataStream = ''
    conn.commit()
    cur.close()
