import random

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["+",",",".","-","'","&","!","?",":",";","#","~","=","/","$","£","^","(",")","_","<",">"]

def generate_pwd():

    upper1 = random.choice(alphabet)
    upper2 = random.choice(alphabet)

    lower1 = str.lower(random.choice(alphabet))
    lower2 = str.lower(random.choice(alphabet))

    digit1 = random.choice(digits)
    digit2 = random.choice(digits)

    symbol1 = random.choice(symbols)
    symbol2 = random.choice(symbols)

    print(upper1 + upper2 + lower1 + lower2 + digit1 + digit2 + symbol1 + symbol2)

generate_pwd()