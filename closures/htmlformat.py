#htmlformat.py
"Python module to experiment closures"

BEFOREBOLD = '<b>'
AFTERBOLD = '</b>'

#BOLDBEFORE = '<b>'
#BOLDAFTER = '</b>'

def bold(text): 
    #return '{}{}{}'.format(BOLDBEFORE,text, BOLDAFTER)
    return '{}{}{}'.format(BEFOREBOLD,text, AFTERBOLD)

BEFOREBOLD = '<span class="bold">'
AFTERBOLD = '</span>'
