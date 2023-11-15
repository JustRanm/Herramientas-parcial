from Operetions import ASCII_code, Binarie_number, Result

def Convetidor_abinarios():
    menu = ('=====Options====== \n1) Word \n2) Character \n3) Exit \n=================')
    Constante = True
    while Constante:
        print(menu)
        Choice = int(input('What do you want to do: '))
        if Choice == 1:
            word = input('What word do you want: ')
            resultado = Result(word)
        if Choice == 2:
            Character = input('What character do you want ')
            resultado = Result(Character)
        if Choice == 3:
            print('Thanks for using our serves')
            Constante = False
        else:
            print('Opcion no disponible')

Convetidor_abinarios()
