brthdt = int(input("Enter your date of birth(MMDDYYYY): "))
tbrthdt = sum(int(digit) for digit in str(brthdt))
uno = sum(int(digit) for digit in str(tbrthdt))
dos = sum(int(digit) for digit in str(uno))
if uno == 10 or dos == 1:
    print("Your tarot birth cards are The Magician (I) and Wheel of Fortune (X).")
elif uno == 11 or dos == 2:
    print("Your tarot birth cards are The High Priestess (II) and Justice (XI).")
elif uno == 12 or dos == 3:
    print("Your tarot birth cards are The Empress (III) and The Hanged Man (XII).")
elif uno == 13 or dos == 4:
    print("Your tarot birth cards are The Emperor (IV) and Death (XIII).")
elif uno == 14 or dos == 5:
    print("Your tarot birth cards are The Hierophant (V) and Temperance (XIV).")
elif uno == 15 or dos == 6:
    print("Your tarot birth cards are The Lovers (VI) and The Devil (XV).")
elif uno == 16 or dos == 7:
    print("Your tarot birth cards are The Chariot (VI) and The Tower (XVI).")
elif uno == 17 or dos == 8:
    print("Your tarot birth cards are Strength (VII) and The Star (XVII).")
elif uno == 18 or dos == 9:
    print("Your tarot birth cards are The Hermit (VIII) and The Moon (XVIII).")
elif uno == 19:
    print("Your tarot birth cards are The Magician (I), Wheel of Fortune (X) and The Sun (XIX).")
elif uno == 20:
    print("Your tarot birth cards are The High Priestess (II) and Judgement (XX).")
elif uno == 21:
    print("Your tarot birth cards are The Empress (III) and The World (XXI).")
