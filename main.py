morse_code = {'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}




def morse_converter(text):
   translated_text = ""
   if text.startswith('.') or text.startswith('-'):
        d_decode = dict([(v, k) for k, v in morse_code.items()])
        text = text.split(' ')
        for x in text:
            translated_text += d_decode.get(x)
        return translated_text.strip()
   else:
        text = text.upper()
        for x in text:
            translated_text += morse_code.get(x) + ' '
        return translated_text.strip()

def game_loop():
    end_morse = False
    print("********WELCOME********")
    print("**********TO**********")
    print("*MORSE-CODE-CONVERTER*")

    while not end_morse:
        direction = input("Would you like to encode or decode: ").lower()
        if direction == 'encode':
            message_for_encode = input("Enter your message to encode: ").upper()
            print(morse_converter(message_for_encode))
        elif direction == 'decode':
            message_for_decode = input("Enter your message to decode: ").lower()

            print(morse_converter(message_for_decode))
        else:
            print("Not a valid direction")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == 'no':
            end_morse = True
            print('Goodbye')


game_loop()