def chufa(a,b):
    try:
        re = a/b
    except Exception as e:
        re = e
    finally:
        return re

print(chufa('a',8))
print(chufa(1,0))