import datetime
import time
import json
import os
import sys

from pushbullet import Pushbullet
from subprocess import call

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print('Notifies you via PushBullet when a command finishes')
	print(' nwd command...')
	print('  command:  The command and all arguments to run')
	print('  e.g. "nwd ping google.com -n 60"')
	print(' nwd -h')
	print('  Shows this kind of lame help message')
	exit(0)

with open('settings.json', 'r') as f:
	settings = json.load(f)
if settings['api_key'] == 'put_key_here':
	print('You should check the README on how to add your API key')
	exit(0)

try:
	pb = Pushbullet(settings['api_key'])
except:
	print ("Your API key is invalid")
	exit(1)

if settings['command_started_title'].isspace():
	if len(sys.argv) == 1:
		pb.push_note(settings['command_started_title'], 'Running command ' + sys.argv[1] + ' with no arguments')
	else:
		pb.push_note(settings['command_started_title'], 'Running command ' + sys.argv[1] + ' with arguments ' + str(sys.argv[2:]))

task_output = open('out.txt', 'w')
retcode = call(sys.argv[1:], stdout = task_output)
task_output.close()

with open('out.txt', 'rb') as f:
	filename = 'out_'+datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H%M%S')+'.txt'
	task_output_data = pb.upload_file(f, filename)
os.remove('out.txt')
	
if retcode == 0:
	pb.push_file(**task_output_data, title=settings['command_done_title'])
else:
	pb.push_file(**task_output_data, title=settings['command_error_title'], body='Command failed with errorcode:  ' + str(retcode) + '.  Output to follow')
