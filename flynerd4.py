serials = {"db z": 5, "db gt": 6, "db super": 10, "mcgayver": 1}

print("Lista seriali do obejrzenia: ")
print(list(serials.keys()))
wybrany = input("Jaki serial chciałbyś obejrzeć?, Podaj jego nazwę:")
print("Swietny wybór, ocena wystawiona dla tego serialu to: {}".format(
    serials[wybrany]))

nowy_serial = str(input("Proszę dodaj nowy serial:"))
print("Swietnie!")
nowa_ocena = int(input("A teraz skali od 1 do 10 oceń serial, który dodałeś: "))
serials[nowy_serial] = nowa_ocena
print("Dziękuję za twoją opinię.")
print("Poniżej lista wszystkich seriali wraz z ich oceną")

szer = 31
l_seriali = list(serials.keys())

print("-"*szer)
print("| * {:^15s} * | {:^5} |".format("Serial","Ocena"))
print("-"*szer)

for x in l_seriali:
	print("| * {:^15s} * | {:^5} |".format(x,serials[x]))
	print("-"*szer)