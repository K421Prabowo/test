import json
import traceback

from modules.helpers.pgdb import conn 
from modules.helpers.logger import getLogger
from modules.models.datas import Data

logger = getLogger("datas")

class Datas():
    cur = None
    def __init__(self):
        if conn != None:
            self.cur = conn.cursor()

    def set(self, data):
        param = Data()
        param.id = data[0]
        param.id = data[1]
        param.type = data[2]
        param.froms = data[3]
        param.status = data[4]
        param.text = data[5]
        param.attachment = data[6]
        param.meta = data[7]
        param.data_date = data[8]

        return param
       
    def get(self, sql):
      self.cur.execute(sql)
      tempDatas = self.cur.fetchall()
      result = []
      for data in tempDatas:
         result.append(self.set(data))
      return result
    
    def getById(self, id):
      sql = f"SELECT * FROM public.datas where id = {id}"
      self.cur.execute(sql)
      tempData = self.cur.fetchone()
      result = self.set(tempData)
      return result

    def getAll(self, page, limit):
      offset = limit * page
      sql = f"SELECT * FROM public.datas ORDER BY 'id' LIMIT = {limit} OFFSET = {offset}"
      self.cur.execute(sql)
      tempData = self.cur.fetchall()
      result = self.set(tempData)
      return result

    def getDetailItem(self, idFund, idStream):
      sql = f"SELECT * FROM public.datas where id_fund = '{idFund}' and id_stream = '{idStream}"
      self.cur.execute(sql)
      tempData = self.cur.fetchone()
      result = self.set(tempData)
      return result