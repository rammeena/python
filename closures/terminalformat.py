#terminalformat.py

BEFOREBOLD = '\x1b[1m'
AFTERBOLD = '\x1b[0m'

#BOLDBEFORE= '\x1b[1m'
#BOLDAFTER = '\x1b[0m'

def bold(text):
    #return '{}{}{}'.format(BOLDBEFORE,text,BOLDAFTER)
    return '{}{}{}'.format(BEFOREBOLD,text,AFTERBOLD)
