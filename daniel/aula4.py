salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("Programador junior")
elif salario> 3000 and salario<= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador senior") 
else:
    print ("gFerente de projetos")