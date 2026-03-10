heslo=input("Input password:")
def check_password(heslo):
    if len(heslo) < 8:
        return False
    if not any(char.isupper() for char in heslo):
        return False
    if not any(char.islower() for char in heslo):
        return False
    if not any(char.isdigit() for char in heslo):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in heslo):
        return False
    return True

if check_password(heslo)==True:
    print("Heslo je platné.")
else:
    print("Heslo není platné. Musí být alespoň 8 znaků dlouhé, obsahovat velká a malá písmena, čísla a speciální znaky.")