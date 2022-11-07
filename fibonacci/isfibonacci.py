
# to find if the given number is fibonacci or not

def isfibo(n):
    # Function to find if the number is fibonacci
    fs = [0 for i in range (0,n+1)]
    def fib(a):
        fs[0] = 0
        fs[1] = 1
        for i in range(2,a+1):
                fs[i] = fs[i-1] + fs[i-2];
    fib(n)
    if n in fs:
        return("The number is fibonacci")
    else:
        return("The number is not fibonacci")

if __name__ == '__main__':
    num = input("Enter the number")
    result = isfibo(int(num))
    print(result)
