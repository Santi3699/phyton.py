def conversor_fc(temp):
    celsius = (temp - 32)/1.8
    return celsius

def conversor_cf(temp):
    farenheit = (temp * 1.8)/32
    return farenheit

temp = float(input("ingrese la temperatura en farenheit"))
print(conversor_cf(temp))
temp = float(input("ingrese la temperatura en celsius"))
print(conversor_fc(temp))
