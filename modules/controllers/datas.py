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
        param.status = data[1]
        param.sort = data[2]
        param.user_created = data[3]
        param.date_created = data[4]
        param.user_updated = data[5]
        param.date_updated = data[6]
        param.id_stream = data[7]
        param.quantity = data[8]
        param.avarage_cost = data[9]
        param.id_fund = data[10]

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

    def getDetailFunds(self, idFund):
      sql = f"SELECT * FROM public.datas where id_fund = '{idFund}'"
      self.cur.execute(sql)
      tempData = self.cur.fetchone()
      result = self.set(tempData)
      return result

    def getDetailItem(self, idFund, idStream):
      sql = f"SELECT * FROM public.datas where id_fund = '{idFund}' and id_stream = '{idStream}"
      self.cur.execute(sql)
      tempData = self.cur.fetchone()
      result = self.set(tempData)
      return result