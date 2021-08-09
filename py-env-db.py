import mysql.connector
from mysql.connector import Error
import re
import os
import sys

db_uri= os.getenv('DWS_MYSQL_DATABASE_URI')

db_uri_pattern='mysql://(.*?):(.*?)@(.*?):(\d*)/(.*?)/'

(username,pwd,hostname,port,dbname)=(re.compile(db_uri_pattern).findall(db_uri)[0])
conn=None

std_out=sys.stdout
std_err=sys.stderr
result=1
try:
	conn=mysql.connector.connect(host=hostname, database=dbname, user=username,password=pwd)
	if conn.is_connected():
		std_out.write('Connected to MySQL database \n')
except Error as e:
	std_err.write(str(e)+'\n')
finally:
	if conn is None :
		result=1
	if conn is not None and conn.is_connected():
		conn.close()
		result=0
print('***** Result is: '+str(result)+' *****')
exit(result)
	
