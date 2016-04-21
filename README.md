# NotifyWhenDone
Notifies you via PushBullet when a command is done running.

### NOTE:
This code was a quick and dirty hack because I was running large tasks and wanted to learn more python.  While I am fully aware I probably wrote messy code, I'm not responsible for the terrible things it might do including everything from deleting wrong files or directories to eating your socks or cat.  If it causes artificial sentience, however, that's completely my fault.

## Dependencies
[pushbullet.py](https://github.com/randomchars/pushbullet.py)

## Setup
Get your API key from [here](https://www.pushbullet.com/#settings) and put it into settings.json

## Usage
nwd command...
command:  The command and all arguments to run
e.g. "nwd ping google.com -n 60"
