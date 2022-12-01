# Morse Code Dictionary
chave = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Declaring functions
# Menu
def show_menu():
    print('------- [MENU] -------')
    print('[1] - Encode')
    print('[2] - Decode')
    print('[3] - Quit')
    print('----------------------')

# Choice validation
def validation(a):
    if a != '1' and a != '2' and a != '3':
        print('Invalid Option!')

# Encoder
def cripto(text):
    tcripto = ''
    for chave in text:
        if chave == 'a':
            tcripto = tcripto + ' ._'
        elif chave == 'b':
            tcripto = tcripto + ' _...'
        elif chave == 'c':
            tcripto = tcripto + ' _._.'
        elif chave == 'd':
            tcripto = tcripto + ' _..'
        elif chave == 'e':
            tcripto = tcripto + ' .'
        elif chave == 'f':
            tcripto = tcripto + ' .._.'
        elif chave == 'g':
            tcripto = tcripto + ' __.'
        elif chave == 'h':
            tcripto = tcripto + ' ....'
        elif chave == 'i':
            tcripto = tcripto + ' ..'
        elif chave == 'j':
            tcripto = tcripto + ' .___'
        elif chave == 'k':
            tcripto = tcripto + ' _._'
        elif chave == 'l':
            tcripto = tcripto + ' ._..'
        elif chave == 'm':
            tcripto = tcripto + ' __'
        elif chave == 'n':
            tcripto = tcripto + ' _.'
        elif chave == 'o':
            tcripto = tcripto + ' ___'
        elif chave == 'p':
            tcripto = tcripto + ' .__.'
        elif chave == 'q':
            tcripto = tcripto + ' __._'
        elif chave == 'r':
            tcripto = tcripto + ' ._.'
        elif chave == 's':
            tcripto = tcripto + ' ...'
        elif chave == 't':
            tcripto = tcripto + ' _'
        elif chave == 'u':
            tcripto = tcripto + ' .._'
        elif chave == 'v':
            tcripto = tcripto + ' ..._'
        elif chave == 'w':
            tcripto = tcripto + ' .__'
        elif chave == 'x':
            tcripto = tcripto + ' _.._'
        elif chave == 'y':
            tcripto = tcripto + ' _.__'
        elif chave == 'z':
            tcripto = tcripto + ' __..'
        elif chave == ' ':
            tcripto = tcripto + " -"
        elif chave == '1':
            tcripto = tcripto + " .____"
        elif chave == '2':
            tcripto = tcripto + " ..___"
        elif chave == '3':
            tcripto = tcripto + " ...__"
        elif chave == '4':
            tcripto = tcripto + " ...._"
        elif chave == '5':
            tcripto = tcripto + " ....."
        elif chave == '6':
            tcripto = tcripto + " _...."
        elif chave == '7':
            tcripto = tcripto + " __..."
        elif chave == '8':
            tcripto = tcripto + " ___.."
        elif chave == '9':
            tcripto = tcripto + " ____."
        elif chave == '0':
            tcripto = tcripto + " _____"
    print('\n')
    print('Texto criptografado:')
    print(tcripto)
    print('\n')

# Decoder
def descripto(text):
    text = text.split(' ')
    codigo = ' '
    for chave in text :
        if chave == '._':
            codigo = codigo + ('a')
        if chave == '_...':
            codigo = codigo + ('b')
        if chave == '_._.':
            codigo = codigo + ('c')
        if chave == '_..':
            codigo = codigo + ('d')
        if chave == '.':
            codigo = codigo + ('e')
        if chave == '.._.':
            codigo = codigo + ('f')
        if chave == '__.':
            codigo = codigo + ('g')
        if chave == '....':
            codigo = codigo + ('h')
        if chave == '..':
            codigo = codigo + ('i')
        if chave == '.___':
            codigo = codigo + ('j')
        if chave == '_._':
            codigo = codigo + ('k')
        if chave == '._..':
            codigo = codigo + ('l')
        if chave == '__':
            codigo = codigo + ('m')
        if chave == '_.':
            codigo = codigo + ('n')
        if chave == '___':
            codigo = codigo + ('o')
        if chave == '.__.':
            codigo = codigo + ('p')
        if chave == '__._':
            codigo = codigo + ('q')
        if chave == '._.':
            codigo = codigo + ('r')
        if chave == '...':
            codigo = codigo + ('s')
        if chave == '_':
            codigo = codigo + ('t')
        if chave == '.._':
            codigo = codigo + ('u')
        if chave == '..._':
            codigo = codigo + ('v')
        if chave == '.__':
            codigo = codigo + ('w')
        if chave == '_.._':
            codigo = codigo + ('x')
        if chave == '_.__':
            codigo = codigo + ('y')
        if chave == '__..':
            codigo = codigo + ('z')
        if chave == ' ':
            codigo = codigo + (' ')
        if chave == '.____':
            codigo = codigo + ('1')
        if chave == '..___':
            codigo = codigo + ('2')
        if chave == '...__':
            codigo = codigo + ('3')
        if chave == '...._':
            codigo = codigo + ('4')
        if chave == '.....':
            codigo = codigo + ('5')
        if chave == '_....':
            codigo = codigo + ('6')
        if chave == '__...':
            codigo = codigo + ('7')
        if chave == '___..':
            codigo = codigo + ('8')
        if chave == '____.':
            codigo = codigo + ('9')
        if chave == '_____':
            codigo = codigo + ('0')
        if chave == '-':
            codigo = codigo + (' ')
    print('\n')
    print('Texto descriptografado:')
    print(codigo)
    print('\n')

# EXECUÇÃO
while True:
    show_menu()

    print('Enter the desired option:')
    choice = input()
    validation(choice)
    if choice == '1':
        print('Enter the text to encode:')
        text = str(input()).lower()
        cripto(text)
    elif choice == '2':
        print('Enter the text to decode:')
        text = str(input()).lower()
        descripto(text)
    elif choice == '3':
        print('Quitting...')
        break
 
