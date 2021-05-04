def fibo():
    n = int(input('Which sequence number, must be above 1: '))

    def fibonnaci(n):
        if n <= 1:
            return(n)
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)

    print(fibonnaci(n))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        if not s1 or not s2:
            return 0
        return compareTo(s1.pop(), s2.pop())


def main():
    entry = input("Which calculation? fibo, gcd, compare, or quit: ")
    while entry:
        if entry == 'fibo':
            fibo()

        elif entry == 'gcd':
            a = int(input("Enter first integer , smaller first: "))
            b = int(input("Enter second integer, higher now: "))
            print(gcd(a, b))

        elif entry == 'compare':
            s1 = list(input("Enter first string: "))
            s2 = list(input("Enter second string: "))
            print(compareTo(s1, s2))

        elif entry == 'quit':
            break

        entry = input("which calculation? fibo, gcd, compare or quit: ")


if __name__ == '__main__':
    main()
