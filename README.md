Morse Code Encoder and Decoder (Python)

Overview
This project is a Morse Code Encoder and Decoder developed using Python. 
The program allows users to convert plain text into Morse code and decode 
Morse code back into readable text. The system runs in a terminal-based 
interface where the user selects options to encode or decode messages.

Features
- Encode text to Morse code
- Decode Morse code to text
- Supports uppercase and lowercase letters
- Supports numbers and punctuation
- Interactive terminal menu
- Continuous program loop until user exits
- Basic error handling for invalid input

Technologies Used
- Python
- Dictionary data structures
- Command Line Interface (CLI)

Program Workflow

1. Start Program
When the program runs, the user is shown a menu:

[0] TO ENCODE TEXT
[1] TO DECODE MORSE CODE
[00] TO EXIT

2. Encode Text
If the user selects option 0:
- The program asks for text input.
- Each character is converted into Morse code using a dictionary.
- The encoded Morse code is displayed.

Example
ENTER TEXT: HELLO
ENCODED: .... . .-.. .-.. ---

3. Decode Morse Code
If the user selects option 1:
- The user enters Morse code separated by spaces.
- The program converts Morse code back into text using a reverse dictionary.
- The decoded message is displayed.

Example
ENTER MORSE CODE: .... . .-.. .-.. ---
DECODED: HELLO

4. Exit Program
If the user enters 00 the program stops running and exits.

Morse Code System

The program uses two dictionaries.

Morse Dictionary
Stores mappings from characters to Morse code.

Example
A → .-
B → -...
C → -.-.

Reverse Dictionary
Automatically generated dictionary used to convert Morse code back to characters.

Project Structure

morse-code-project
│
├── morse_code.py
└── README.txt

User Interface
The program runs completely inside the terminal and provides:
- Menu driven options
- User input prompts
- Encoded or decoded output

Future Improvements
- Add sound output for Morse signals
- Create graphical user interface (GUI)
- Add file input and output
- Add real-time Morse typing detection
- Add LED blink simulation for Morse signals

License
This project is open-source and available under the MIT License.

Author
Sayan
BCA Student | Programming | Python Development
