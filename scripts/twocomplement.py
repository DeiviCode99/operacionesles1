def complemento_a_1(binario_texto):
    inverso = ""
    for bit in binario_texto:
        if bit == "0":
            inverso += "1"
        else:
            inverso += "0"
    return inverso

def representacion_comp_dos(num):
    print("numero decimal: ", num)

    
    decimalplus = abs(num)
    binario=format(decimalplus,"b")
    print("numero positivo:", decimalplus)
    print("numero binario:  ", binario)

    copm_1 = ""
    for bit in binario:
        if bit == "0":
                copm_1 += "1"
        else:
                copm_1 += "0"
    print("complemento a 1: ",copm_1)

    comp_1_decimal = int(copm_1,2)
    #print(comp_1_decimal)

    comp_1_plus_1 = comp_1_decimal + 1
    #print("Sumamos 1: ", comp_1_plus_1)
    binario_2=format(comp_1_plus_1,"b")
    print("complemento a 2: ", binario_2)

    return ""
Ejemplo = representacion_comp_dos(-43)
print(Ejemplo)
