#/usr/bin/python3


def menu():
    print("""Welcome to my fibonacci series printing program. 
             Just enter the number of term you want and you'll have it. """)

def fibonacci(numbers):
    fibo = [0,1]
    if (numbers==0):
        return []
    elif (numbers in (1,2)):
        return fibo
    else: 
        for i in range(0,numbers-2):
            fibo.append(fibo[-1]+fibo[-2])
    return fibo

menu()

print(fibonacci(int(input("How many terms do you want to print? : "))))

