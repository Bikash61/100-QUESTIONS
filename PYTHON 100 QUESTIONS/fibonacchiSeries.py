def fibonachi(n):
    fib_seq =[0,1]
    while len(fib_seq)<n:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq[:n]

print("The fibonachi series is",fibonachi(15))