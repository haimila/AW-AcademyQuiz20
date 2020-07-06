def intro():
    global pelitila
    while True:

        try:

            print("Welcome to AWS trivia!")
            pelataanko = input("Do you want to start the game Y/N?")

        except:

            print("Input either Y to start or N to quit!")
            continue

        else:
            if pelataanko[0].lower() == "y":
                break

            elif pelataanko[0].lower() == "n":
                pelitila = False
                break

def kysymys1():
    global pisteet
    while True:
        print("Which of these services is global? Choose A, B, or C.")
        print("A) EC2")
        print("B) IAM")
        print("C) VPC")
        vastaus = input("Your answer: ")

        if vastaus[0].lower() == "b":
            print("Correct!")
            pisteet += 1
            break

        else:
            print("Wrong answer!")
            break

def kysymys2():
    global pisteet
    while True:
        print("Which of these is EC2 part of?")
        print("A) IaaS")
        print("B) PaaS")
        print("C) SaaS")
        vastaus = input("Your answer: ")

        if vastaus[0].lower() == "a":
            print("Correct!")
            pisteet += 1
            break

        else:
            print("Wrong answer!")
            break

pelitila = True

intro()
while pelitila:
    pisteet = 0

    kysymys1()
    kysymys2()

    break



