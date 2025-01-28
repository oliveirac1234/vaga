def inverter_string(s):
    inverted = ""
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]
    return inverted

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")