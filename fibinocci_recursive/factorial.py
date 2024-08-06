def getFactorial(num=None, f=1):
    if num is None:
        return 0
    if num > 1:
        return num * getFactorial(num - 1)
    else:
        return f
