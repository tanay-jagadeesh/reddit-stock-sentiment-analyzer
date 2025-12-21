""""Purpose of this file is to clean data""""
import re 

def remove_url(txt, p):
    res = re.sub(p, "[URL REMOVED]", txt)
    return res