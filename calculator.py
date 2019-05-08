def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def main():
    a = int(input("enter a number "))
    b = int(input("enter another number "))
    print("+ is", sum(a,b))
    print("- is", sub(a,b))
    print("/ is", div(a,b))
    print("* is", mul(a,b))

if __name__ == '__main__':
    main()
