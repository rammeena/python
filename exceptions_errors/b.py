from a import no_return

def call_exceptor():
    print("call_exceptor starts here.....")
    try:
        no_return()
    except:
        print("An exception was raise.....")
    print("executed after the exception")
