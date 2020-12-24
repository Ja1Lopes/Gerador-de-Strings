import string
import itertools
import os

caminho = os.environ['HOMEPATH']
diretorio = 'C:' + caminho + '\\Desktop\\'
file = diretorio + 'Strings.txt'

arq = open(file, 'w+')

def generate(maxChar, limite, ch): 

    estado = True
    while estado:
        for s in itertools.combinations_with_replacement(ch, maxChar):
            i = ''.join(s)
            yield i
        maxChar += 1
        if maxChar > limite:
            arq.close()
            print('Saindo')
            estado = False
            os.sys.exit()

def main():

    maxChar = int(input('Número de caracteres mínimo: \n'))
    limite = int(input('Número de caracteres máximo: \n'))
    
    tipo = input('Tipo de combinação: \n'
                 ' Letras (1) \n'
                 ' Números (2) \n'
                 ' Letras e Números (3) \n'
                 ' Letras, Números e Símbolos (4) \n')
    
    if tipo == '1':
        ch = string.ascii_letters + 'ç' + 'Ç'
        
    elif tipo == '2':
        ch = string.digits
        
    elif tipo == '3':
        ch = string.ascii_letters + string.digits + 'ç' + 'Ç'
        
    elif tipo == '4':
        ch = string.ascii_letters + string.digits + string.punctuation + 'ç' + 'Ç'
    
    for i in generate(maxChar, limite, ch):
        arq.write(f"{i} ")

if __name__ == '__main__':
    main()
    
