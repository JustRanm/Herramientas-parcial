def ASCII_code(word_character):
     return ord(word_character)
        
   

def Binarie_number(numero_ascii):
    return bin(numero_ascii)[2:]
     

def Result(Naruto_shippuden_word):
    Results = []
    Binarios_lista= []
    for character in Naruto_shippuden_word:
        Ascci = ASCII_code(character)
        Binarios = Binarie_number(Ascci)
        Binarios_lista.append(Binarios)
        Results.append((character,Ascci,Binarios))
    for uwu in Results:
        Print = print(f'ASCCI value of {uwu[0]} is {uwu[1]}, and the representantion in binarie is {uwu[2]}')
    Binaries = print(f'Total is: {" ".join(Binarios_lista)}')
    return Print, Binaries
