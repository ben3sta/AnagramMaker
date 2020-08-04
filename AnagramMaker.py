import random

while 1:
    try:
        def anagram():
            anagrama = ""
            for i in a:
                rand = str(lista[random.randint(0,int(len(a))-1)])
                if a.count(rand) == anagrama.count(rand):
                    prevrand = rand
                    while True:
                        rand = str(lista[random.randint(0,int(len(a))-1)])
                        if rand != prevrand and a.count(rand) != anagrama.count(rand):
                            anagrama += rand
                            break
                else:
                    anagrama += rand
            return anagrama


        a = input("Word to disorganize: ")
        while 1:
            try:
                b = int(input("How many attempts? "))
                print("\n")
                break
            except ValueError:
                print("Please, enter a number\n")
                b = int(input("How many attempts? "))
                break

        lista = []
        for x in a:
            lista.append(x)

        for i in range(0,b):
            anagrama = anagram()
            print(anagrama)
    except KeyboardInterrupt:
        print("\n\n...Program manually stopped")
        break
