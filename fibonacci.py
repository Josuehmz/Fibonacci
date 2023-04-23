# Define a dictionary to store previously calculated Fibonacci numbers
fib_dict = {0: 0, 1: 1}

def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_dict[n]

def main():
    while True:
        n = int(input("Enter a number to calculate its Fibonacci value: "))
        result = fibonacci(n)
        print("The Fibonacci value of {} is: {}".format(n, result))
        answer = input("Do you want to calculate another Fibonacci value? (yes or no) ")
        if answer.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
