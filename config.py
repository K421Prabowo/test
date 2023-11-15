
import os
from dotenv import load_dotenv

load_dotenv()

isDev = bool(os.getenv('IS_DEV'))
host = os.getenv('HOST')
port = os.getenv('PORT')

dbhost = os.getenv("dbhost")
dbport = os.getenv("dbport")
dbname = os.getenv("dbname")
dbuser = os.getenv("dbuser")
dbpass = os.getenv("dbpass")

folder = os.getenv("folder")

fileoutput = './result/output.xlsx'
