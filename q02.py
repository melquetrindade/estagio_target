def checkString(string):
    string_lower = string.lower()
    
    # Conta a ocorrência da letra 'a'
    quantidade_a = string_lower.count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

string = input("Entre com uma string: ")
checkString(string)
