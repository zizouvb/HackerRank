if __name__ == '__main__':
    arr = list()
    for _ in range(int(input())):
        command = input().split()
        args = command[1:]
        if command[0] == "print":
            print(arr)
        else:
            eval("arr."+command[0]+"("+",".join(args)+")")
