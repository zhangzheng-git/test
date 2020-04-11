a = 1

def change(b):
    """变"""
    global a
    a = 10
    return a

newa  = change(a)
print(newa)
print(a)