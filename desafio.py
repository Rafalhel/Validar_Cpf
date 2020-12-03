while True:
    cpf = input("Digite um Cpf:")
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("/", "")
    val_cpf = cpf
    novo_cpf = cpf[:9]
    x = 10
    z = 0
    try:
        for c in novo_cpf:
            c = int(c)
            y = c * x
            z += y
            result = 11 - (z % 11)
            if result > 10:
                result = 0
            x -= 1
            if x < 2:
                x = 11
        novo_cpf += str(result)
        y = 0
        z = 0
        for c in novo_cpf:
            c = int(c)
            y = c * x
            z += y
            result = 11-(z % 11)
            if result > 10:
                result=0
            x -= 1
        novo_cpf += str(result)
        if novo_cpf == val_cpf:
            print("O Cpf ",cpf, "é válido!")
        else:
            print("O Cpf ",cpf, "não é válido!")
    except:
        print("Valor inválido")