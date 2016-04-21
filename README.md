# NotifyWhenDone
Notifies you via PushBullet when a command is done running.

### NOTE:
This code was a quick and dirty hack because I was running large tasks and needing to learn python.  While I am fully aware I probably wrote shitty code, I'm not responsible for the shit it does which includes everything from deleting wrong files to eating your cat.  If it causes artificial sentience however, that's completely my fault.

## Dependencies
[pushbullet.py](https://github.com/randomchars/pushbullet.py)

## Setup
Get your API key from [here](https://www.pushbullet.com/#settings) and put it into settings.json

## Usage
nwd command...
  command:  The command and all arguments to run
  e.g. "nwd ping google.com -n 60"
