longitud = int(input("Hasta que número cuento? "))

def fizzbuzz(long):
    for n in range(1, long):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)

fizzbuzz(longitud)
