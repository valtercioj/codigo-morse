class Morse(object):
    def __init__(self):
        self.morse_code = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }
 
 
    def encode(self, plaintext):
        ''' Codifica em codigo morse '''
        code = ''
        for char in plaintext.upper():
            if char in self.morse_code.keys():
                code += self.morse_code[char] + ' '
        print('-'*200)
        print(' '*5+'Texto codificado => '+code)
        print('-'*200)


texto = str(input(r"""

               _ _                                             
              | (_)                                            
  ___ ___   __| |_  __ _  ___    _ __ ___   ___  _ __ ___  ___ 
 / __/ _ \ / _` | |/ _` |/ _ \  | '_ ` _ \ / _ \| '__/ __|/ _ \
| (_| (_) | (_| | | (_| | (_) | | | | | | | (_) | |  \__ \  __/
 \___\___/ \__,_|_|\__, |\___/  |_| |_| |_|\___/|_|  |___/\___|
                    __/ |                                      
                   |___/                                       



																					author: Valtercio Junior
																					version: 1.0

Texto a ser Codificado: """))


morse = Morse()
codigo = morse.encode(texto)



