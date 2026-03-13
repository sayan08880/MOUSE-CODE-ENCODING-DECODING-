# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',  # Space between words
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

# Reverse dictionary for decoding
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# Function to encode text to Morse code
def encode_to_morse(text):
    """Convert plain text to Morse code."""
    text = text.upper()
    encoded = ' '.join(MORSE_CODE_DICT.get(char, '?') for char in text)
    return encoded

# Function to decode Morse code to text
def decode_from_morse(morse_code):
    """Convert Morse code to plain text."""
    decoded = ''.join(REVERSE_MORSE_CODE_DICT.get(code, '?') for code in morse_code.split(' '))
    return decoded.replace('/', ' ')

# Main function to handle user input
def main():
    while True:
        print("[0] TO ENCODE TEXT, [1] TO DECODE MORSE CODE, [00] TO EXIT")
        choice = input("ENTER CHOICE : ")
        if choice == '0':
            text_input = input("ENTER TEXT: ")
            encoded_text = encode_to_morse(text_input)
            print(f"ENCODED: {encoded_text}")
        elif choice == '1':
            morse_code_input = input("ENTER MORSE CODE: ")
            decoded_text = decode_from_morse(morse_code_input)
            print(f"DECODED: {decoded_text}")
        elif choice == '00':
            print("EXITING THE PROGRAM.")
            break
        else:
            print("INVALID CHOICE. PLEASE ENTER 0, 1, OR 00.")

if __name__ == "__main__":
    main()
