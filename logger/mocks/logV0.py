from sys import argv
from datetime import datetime
from os.path import exists

script, log = argv
exists(log)
today = datetime.now()
logTime = today.strftime('%d/%m/%Y %H:%M - ')

openFile = open(log, 'a+')
print openFile.read()
newLog = raw_input("Enter New Log: \n")
openFile.write('\n' + logTime + newLog)
openFile.seek(0)
print openFile.read()
openFile.close()
