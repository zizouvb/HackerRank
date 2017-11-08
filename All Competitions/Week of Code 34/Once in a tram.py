def onceInATram(x):
    # Complete this function
    x=x+1
    islucky = lambda x: sum(int(i) for i in str(x)[0:3]) == sum(int(i) for i in str(x)[3:6])
    while not islucky(x):
        x = x+1
    return x
if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x)
    print(result)
