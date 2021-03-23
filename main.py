# Morse Code Translator

# Use dictionary to xref between test and morse.

morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": " "
}

def list_to_string(s):
    str1 = " "
    return(str1.join(s))

running = True

while running:

    # Input string to translate.

    message_txt = input("Enter text to convert to Morse Code ('*' to stop):").upper()

    if message_txt == "*":
        running = False
        break

    #Convert text to Morse Code.

    morse_msg =[morse_dict[letter] for letter in message_txt]
    print(f"Morse Code is: {list_to_string(morse_msg)}")
