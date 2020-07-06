def intro():
    global pelitila
    while True:

        try:

            print("Tervetuloa AWS-triviaan!")
            pelataanko = input("Haluatko aloittaa uuden pelin K/E?")

        except:

            print("Paina joko K aloittaaksesi pelin tai E sulkeaksi ohjelman!")
            continue

        else:
            if pelataanko[0].lower() == "k":
                break

            elif pelataanko[0].lower() == "e":
                pelitila = False
                break


pelitila = True

while pelitila:
    pisteet = 0

    intro()
    

    continue



