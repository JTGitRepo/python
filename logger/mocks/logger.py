from sys import argv, exit
from datetime import datetime
from os.path import exists


script, log = argv

today = datetime.now()
logTime = today.strftime('%m/%d/%Y %H:%M:%S - ')

def mainLogFileMethod():
    openFile = open(log, 'a+')
    print openFile.read()
    newLog = raw_input("Enter New Log: \n")
    openFile.write('\n' + logTime + newLog)
    openFile.seek(0)
    print openFile.read()
    openFile.close()

def yesOrNo(): 
    createNewLogFile = raw_input('Log file does not exist. Create log file %s?(y/n): ' % log)
    if str(createNewLogFile).lower() == 'y' or str(createNewLogFile).lower() == 'yes':
        mainLogFileMethod()
    elif str(createNewLogFile).lower() == 'n' or str(createNewLogFile).lower() == 'no':
        exit()
    else:
        print '%s is not an option' % createNewLogFile
        yesOrNo()

if exists(log):
    mainLogFileMethod()
else: 
    yesOrNo()
