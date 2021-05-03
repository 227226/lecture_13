def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    number = int(input("Zadejte číslo:"))
    while number < 1:
        print("Zadali jste neplatné číslo.")
        number = int(input("Zadejte číslo:"))
    else:
        return print(fibo(number - 1))


if __name__ == '__main__':
    main()
