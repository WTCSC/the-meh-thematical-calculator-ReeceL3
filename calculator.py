from time import sleep
#introduction
print("Welcome to my math calculator I guess...")
sleep(1)
print("I suppose I can help you with some basic operations.")
sleep(1)

#functions for the program
def add(a, b):
    print("Heres your sum or whatever")
    return a + b
#subtraction
def subtract(a, b):
    print("Yeah subtraction is boring heres your answer")
    return a - b
#multiplication
def multiply(a, b):
    print("Do you really need to multiply? Fine, heres your product")
    return round (a * b, 2)
#divison
def divide(a, b):
    if b == 0:
        print("Seriously? Division by zero are you really that lame?")
        return None
    print("Heres your answer not that it matters anyways or anything")
    return a / b

#choices for the functions
def main():
    while True:
        print("\nWhat do you want now?")
        sleep(.5)
        print("1. Addition (ugh, so original)")
        sleep(.5)
        print("2. Subtraction (wow, thrilling)")
        sleep(.5)
        print("3. Multiplication (math party!)")
        sleep(.5)
        print("4. Division (sure, why not)")
        sleep(.5)
        print("5. Quit (finally)")
        sleep(.5)

        choice = input("Pick one (1-5): ")

        if choice == "5":
            print("Goodbye. I need a nap anyway.")
            break
            #if there an idiot and don't put the right option
        if choice not in ["1", "2", "3", "4"]:
            print("That’s not even a real option. Try again.")
            sleep(1)
            continue
            
            # Asks for numbers
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Nope use numbers don't type them out and make my job harder than it needs to be.")
            continue
            #eqautions
        if choice == "1":
            print(add(a, b))
        elif choice == "2":
            print(subtract(a, b))
        elif choice == "3":
            print(multiply(a, b))
        elif choice == "4":
            result = divide(a, b)
            if result is not None:
                print(result)


if __name__ == "__main__":
    main()
