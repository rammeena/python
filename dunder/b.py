#b.py

from c import ProgressBar

"""Context manager testing"""
with ProgressBar(5) as p:
    print("printing p: {}".format(p))
    for i in range(5):
        p.update(i)

#with ProgressBar(5) as p:
#    for i in range(2):
#        p.update(i)
