import os
import json
import shutil
import datetime


bTime = datetime.datetime.now()
if os.path.isdir(f'OUTPUT/messages'):
    shutil.rmtree('OUTPUT/messages', ignore_errors=True)
    os.mkdir('OUTPUT/messages')
else:
    os.mkdir('OUTPUT/messages')

MSGs = 0
print('Sorting Message Logs...\n\n')
for directory, subdirectories, files in os.walk('INPUT\messages'):
    path = os.path.join(directory, 'channel.json')
    if os.path.isfile(path):
        with open(path,'r') as f:
            channel = json.load(f)

        try:
            dirPath = f"OUTPUT/messages/{channel['guild']['name']}"
            dirPath2 = ''
            for i in channel['guild']['name']:
                if '/' == i or "\\" == i or ':' == i or '*' == i or '<' == i or '>' == i or '|' == i or '?' == i or '"' == i:
                    continue
                else:
                    dirPath2 += i
            if os.path.isdir(dirPath) == False:
                if os.path.isdir(f'OUTPUT/messages/{dirPath2}') == False:
                    c = channel['guild']['name']
                    if '/' in c or "\\" in c or ':' in c or '*' in c or '<' in c or '>' in c or '|' in c or '?' in c or '"' in c:
                        c2 = ''
                        for i in c:
                            if '/' == i or "\\" == i or ':' == i or '*' == i or '<' == i or '>' == i or '|' == i or '?' == i or '"' == i:
                                continue
                            else:
                                c2 += i
                        dirPath = f"OUTPUT/messages/{c2}"
                        os.mkdir(dirPath)
                    else:
                        os.mkdir(dirPath)
                else:
                    dirPath = f"OUTPUT/messages/{dirPath2}"

            shutil.copyfile(f'{directory}/messages.csv',f"{dirPath}/{channel['name']}.csv")
            print(directory + ' -> ' + f"{dirPath}/{channel['name']}.csv")
            MSGs += 1
        except KeyError:
            continue
aTime = datetime.datetime.now()
timeDiff = aTime - bTime
print(f'\n\nComplete! ({MSGs} Files // Exec Time: {timeDiff})')
input('Press Enter to close:')
