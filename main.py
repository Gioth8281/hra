# Importuju modul
import random

# Variable abych věděl na jakém je hráč kole.
round_count = 1

# Hlavní systém
while True:
    # Random číslo systém (začátek)
    howmuchint = 1
    randomnumlist = []

    # for cyklus který vygeneruje random číslo které bude odpověď
    for i in range(howmuchint):
        randomnumrange = 20
        randomnum = random.randint(1, randomnumrange)
        randomnumlist.append(randomnum)

    randomnum_select = random.choice(randomnumlist)
    # Random číslo systém (konec)

    # Vypíše odpoveď pro debugging
    print(randomnum_select)
    print()

    # Zde nám to řekne ať zadáme odpověď s conditions které jsou níže
    while True:
        user_input = input(f"Zadej číslo mezi 1 a {randomnumrange}: ")
        print()
        
        # Když hráč napíše číslo spustí se "try", když napíše něco jiného spustí se "except"
        try:
            input_value = int(user_input)
            # Jestli číslo je mezi 1 a randomnumrange pojedeme dál
            if 1 <= input_value <= randomnumrange:
                # Pokud jsi uhádl dobře vypíše to náhodně zprávu
                if input_value == randomnum_select:
                    randomwinlist = ["Správně!", "Máš to správně, jsi dobrý!", "Jsi výherce!", "Vyhrál jsi!"]
                    randomwin = random.choice(randomwinlist)
                    print(randomwin)
                    # Toto je round system který určí jestli jdeš do dalšího kola (v tomto případě jdeš)
                    round_system = 1
                    break
                # Pokud jsi uhádl špatně vypíše to zprávu
                else:
                    print("Špatně! Prohrál jsi.")
                    # Toto je round system který určí jestli jdeš do dalšího kola (v tomto případě nejdeš)
                    round_system = 2
                    break
            # Jestli číslo není mezi 1 a randomnumrange přejdeme zpátky na druhý while loop
            else:
                print(f"Číslo musí být mezi 1 a {randomnumrange}! Zkus to znovu.")
        # Zde vidíme že except vypíše zprávu když jsme nenapsali číslo a hodí nás zpátky na druhý while loop
        except ValueError:
            print("Tento znak není platné číslo! Zkus to znovu.")

    # V každým kole se "round_count" zvedne o jednu číslici nahoru
    round_count += 1

    # Toto je spojené s "round_system" variable který vidíme na řádku 41. (zde jsme prohráli a tím pádem ukončujeme celý while loop)
    if round_system == 2:
        if round_count == 2:
            print("Nedostal jsi se do žádného kola!")
            print()
            break
        else:
            round_count -= 1
            print(f"Na konec jsi se dostal do {round_count}. kola!")
            print()
            break
    # Toto je spojené s "round_system" variable který vidíme na řádku 47. (zde jsme vyhráli a tím pádem spouštíme celý while loop znova)
    else:
        print(f"Právě jsi se dostal do {round_count}. kola!")
        print()
        print("____________")
        print()

# Konec
input("Press any key to exit... ")
