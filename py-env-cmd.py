import re
from subprocess import run
import os
import sys
import time



cmd= os.getenv('DWS_TESTER_COMMAND')
threshold= int(os.getenv('DWS_TESTER_THRESHOLD'))
interval= int(os.getenv('DWS_TESTER_INTERVAL'))

cmd_args=cmd.split(' ')

i=1
exit_code=-1
while i<=threshold:
	print ('\nAttemping to run the command. Attemping #'+str(i)+' of '+str(threshold)+'.')
	run_result=run(cmd_args)
	if run_result.returncode==0:
		exit_code=0
		break
	print('the execution of the command was not successful due to the following error, retrying '+str(interval)+' seconds later...')
	print('exit code for the command was:  '+str(run_result.returncode))
	time.sleep(interval)
	i+=1
if run_result.returncode==0:
	print('\nThis program ended successsfully with exit code #0')
	exit(0)
else:
	print('\nRunning the command was not successfull, exit code for the command was:  '+str(run_result.returncode))
	print('This program ended with exit code #1')
	exit(1)
	
		
