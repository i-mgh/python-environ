# python-environ
Working with environment variables in Python 
There are two scripts in this repository
1) py-env-db.py: this script read the 'DWS_MYSQL_DATABASE_URI' from the OS environment and trying to connect to your MySQL, if it can connect will return 0 otherwise will return the error and return code 1.

2) py-env-cmd.py: this script read the following environment variables: 
i) DWS_TESTER_COMMAND: command or script
ii) DWS_TESTER_THRESHOLD: how many times
iii) DWS_TESTER_INTERVAL: waiting in seconds
then will try to run the command or script that is loaded to the (i)
if the command/script was successful, the script will exit with code 0
otherwise, it will try to run the command/script until to (ii) and will sleep between each retry about (iii) seconds.

Sample to run this script
export DWS_MYSQL_DATABASE_URI='mysql://USERNAME:PASSWORD@MYSQL_IP:PORT/DBNAME/'
provide your USERNAME, PASSWORD, MYSQL_IP, PORT, DBNAME
export DWS_TESTER_COMMAND='python3 py-env-db.py'
export DWS_TESTER_THRESHOLD=4
export DWS_TESTER_INTERVAL=20
python3 py-env-cmd.py
