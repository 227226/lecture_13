def recursive_nth_fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    number = int(input("Zadejte číslo:"))
    while number < 1:
        print("Zadali jste neplatné číslo.")
        number = int(input("Zadejte číslo:"))
    else:
        fib_seq = []
        for num in range(number + 1):
            fib_seq.append(recursive_nth_fibo(num))
        print(fib_seq)

        fib_seq = [recursive_nth_fibo(num) for num in range(number + 1)]
        print(fib_seq)


if __name__ == '__main__':
    main()
