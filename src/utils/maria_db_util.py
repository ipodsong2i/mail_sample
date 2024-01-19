import pymysql
from utils.config import config

db_config = config.get_config("DATABASE")

db_adddress = db_config["HOST"]
db_port = db_config["PORT"]
db_user = db_config["USERNAME"]
db_password = db_config["PASSWORD"]
db_default_schame = db_config["DB_NAME"]
 
conn = pymysql.connect(host=db_adddress, port=db_port, user=db_user, password=db_password, db=db_default_schame, charset="utf8")
current_db = conn.cursor()