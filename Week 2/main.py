age = 18

if age > 65:
    print("Je bent 65+")
elif age >= 18:
    print("Volwassen")
elif age < 18:
    print("Je bent nog niet volwassen")

def for_loop():
    for count in range(10):
        print(count)

def while_loop():
    num = 5

    while num == 5:
        print("num is gelijk aan 5")


for_loop()
while_loop()