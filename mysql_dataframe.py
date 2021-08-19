import mysql.connector as sql
import pandas as pd

db = sql.connect(host="localhost", database ='test',user="raj", passwd="Payanam$123rt")
cur = db.cursor()

cur.execute("SELECT * FROM data")
df_sql_data = pd.DataFrame(cur.fetchall())

db.close()

print (df_sql_data )