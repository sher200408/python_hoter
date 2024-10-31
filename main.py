import json
import hashlib

class Hoter:
    """ Mehmonxonalar klassi """
    def __init__(self, what_stars):
        self.what_stars = what_stars
        self.in_action = False
        self.room = False

class Hoter_room_internal(Hoter):
    """ Mehmonxonaning ichki xonalari """
    def __init__(self, what_stars):
        self.lux_room = False
        self.biznisClass = False
        self.comfoct = False
        super().__init__(what_stars)
        
    def __str__(self):
        return "Hoter Class and Room and internal"

class Person:
    """ Odam klassi, ism, familiya, email va kartani o‘z ichiga oladi """
    def __init__(self, name, surname, email, password, pin, karta):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password  # Typo corrected
        self.pin = pin
        self.karta = karta

    def __str__(self):
        return "Person About"

def json_farmata_jonadis(person):
    """ Person obyektini JSON formatda saqlash """
    data = {
        "name": person.name,
        "surname": person.surname,
        "email": person.email,
        "password": person.password,
        "pin": person.pin,
        "karta": person.karta
    }
    with open("person.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Ma'lumotlar JSON formatda saqlandi")

def json_farmad_study():
    """ JSON faylni o'qish va ma'lumotlarni chiqarish """
    try:
        with open("person.json", "r") as f:
            data = json.load(f)
            print("Saqlangan ma'lumotlar:", data)
    except FileNotFoundError:
        print("Fayl topilmadi!")

def register_person_check():
    """ Ro'yhatdan o'tish uchun funksiyani chaqirish """
    print("Iltimos, ro'yhatdan o'ting.")
    name = input("Ismingizni kiriting: ")
    surname = input("Familiyangizni kiriting: ")
    email = input("Email kiriting: ")
    password = input("Parolingizni kiriting: ")
    pin = input("PIN kiriting: ")
    karta = input("Karta kiriting: ")
    
    # Yangi mijoz yaratish va uni JSON formatda saqlash
    new_person = Person(name, surname, email, password, pin, karta)
    json_farmata_jonadis(new_person)
    print(f"Yangi mijoz ro'yhatdan o'tdi: Ismi = {name}, familiyasi = {surname}")

register_person_check()
