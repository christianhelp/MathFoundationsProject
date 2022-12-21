import time


def welcomeMessage():
    print("Please select a number to continue")
    print("1 -  Primes, GCD, LCM")
    time.sleep(1)
    print("2 - Modular Arithmetic")
    time.sleep(1)
    print("3 - Combinatorics")
    time.sleep(1)
    print("4 - Exit Program")


def primeFacts(p):
    orig = p
    if p == 0:
        print("ERROR. 0 FACTORIZATION NOT POSSIBLE")
        return
    if p == 1:
        print("1 is neither a prime number nor a composite number.")
        return
    result = []
    div = 2
    while p > 1:
        while p % div != 0:
            div += 1
        result.append(div)
        p = p / div
        div = 2
    print(f"Prime factorization of {orig} is:\n{list(result)}")


def findFactors(p) -> list:
    if p == 0:
        print("ERROR. NUMBER MUST BE 1 OR HIGHER")
        return []
    elif p == 1:
        print("The 1 factor of 1 is:\n1")
        return [1]
    div = 1
    countFactors = 0
    factors = []

    while div <= p:
        if p % div == 0:
            countFactors += 1
            factors.append(div)
        div += 1
    return factors


def GCD(p, q) -> int:
    result1 = findFactors(p)
    result2 = findFactors(q)
    first_set = set(result1)
    second_set = set(result2)

    return max(first_set.intersection(second_set)) if len(first_set.intersection(second_set)) > 0 else 0


def LCM(p, q):
    print(f"The LCM between {p} and {q} is {int((p * q) / GCD(p, q))}")


def modAdd(a, b, m):
    a_count = 0
    b_count = 0

    print(f"Modular arithmetic of {a_count} + {b_count} mod {m} is {(a_count + b_count) % m}")

    while a_count < a or b_count < b:
        if a_count != a:
            a_count += 1
        if b_count != b:
            b_count += 1
        print(f"Modular arithmetic of {a_count} + {b_count} mod {m} is {(a_count + b_count) % m}")


def modMult(a, b, m):
    a_count = 0
    b_count = 0

    print(f"Modular arithmetic of {a_count} * {b_count} mod {m} is {(a_count + b_count) % m}")

    while a_count < a or b_count < b:
        if a_count != a:
            a_count += 1
        if b_count != b:
            b_count += 1
        print(f"Modular arithmetic of {a_count} * {b_count} mod {m} is {(a_count * b_count) % m}")


def modularArith(a, b, m):
    print("Printing Results for (0 to a) + (0 to b) mod m")
    modAdd(a, b, m)
    time.sleep(1)
    print("Printing Results for (0 to a) * (0 to b) mod m")
    modMult(a, b, m)


def factorial(m) -> int:
    if m == 0:
        return 1
    if m == 1:
        return 1
    return m * factorial(m - 1)


def combinatorics(n, m):  # n = number of letters in password m = number of digits

    x = m
    y = n

    total1 = (52 ** n) * (10 ** m)
    total2 = 0
    total3 = 0

    while x >= 0:
        total2 += (52 ** n) * (10 ** x)
        x -= 1

    while y >= 0:
        total3 += (52 ** y) * (10 ** m)
        y -= 1

    print("There are", total1, "possible passwords.")
    print("There are", total2, "possible passwords with at most", m, "digits.")
    print("There are", total3, "possible passwords with at most", n, "letters.")


def main():
    print("Welcome to the group of Christian Walker and Victor Martinez")
    time.sleep(1.5)
    welcomeMessage()
    response = input()

    if response == "4":
        print("Thank you for using our program! Happy holidays!\n*<[:{)")
        exit(0)

    if response > "3":
        print("Please provide a valid input!")

    while response != "4":

        if response == "4":
            break
        if response == "1":

            a = int(input("Please provide a non-negative integer a\n"))
            b = int(input("Please provide a non-negative integer b\n"))

            if a < b:
                primeFacts(a), primeFacts(b)
            else:
                primeFacts(b), primeFacts(a)

            GCD(a, b) if a < b else GCD(b, a)
            print(f"The GCD between {a} and {b} is {GCD(a, b)}") if a < b else print(
                f"The GCD between {b} and {a} is {GCD(a, b)}")
            LCM(a, b) if a < b else LCM(b, a)

        elif response == "2":
            a = int(input("Please enter a non-negative a\n"))
            b = int(input("Please enter a non-negative b\n"))
            m = int(input("Please enter a positive m\n"))

            modularArith(a, b, m)

        elif response == "3":
            n = int(input("Please enter a non-negative n\n"))
            m = int(input("Please enter a non-negative m\n"))
            combinatorics(n, m)
        else:
            print("PLEASE ENTER VALID INPUTS")
        welcomeMessage()
        response = input()
    print("Thank you for using our program! Happy holidays!\n*<[:{)")


if __name__ == "__main__":
    main()
