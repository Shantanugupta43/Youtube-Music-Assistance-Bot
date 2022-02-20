
#Coverts time into seconds
def sec_convert(t):
    
    m, s = t.split(':')
    return int(m) * 60 + int(s)
