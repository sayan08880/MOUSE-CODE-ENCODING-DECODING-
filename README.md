# Morse Code Encoder & Decoder (Python)

A simple **Python command-line application** that converts **plain text to Morse code** and **Morse code back to text**.

This project demonstrates basic **Python dictionary usage, loops, and string processing**.

---

# Features

* Encode **text → Morse code**
* Decode **Morse code → text**
* Supports:

  * Letters (A–Z)
  * Numbers (0–9)
  * Common punctuation
* Command-line interface
* Continuous program loop
* Exit option

---

# Morse Code Example

Text:

```id="a8k92s"
HELLO
```

Encoded output:

```id="g71xq3"
.... . .-.. .-.. ---
```

---

# Encoding Example

Input:

```id="o93a7c"
HELLO WORLD
```

Output:

```id="c3f6y1"
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Here `/` represents a **space between words**.

---

# Decoding Example

Input:

```id="4z8n1b"
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Output:

```id="1j7mwe"
HELLO WORLD
```

---

# Program Menu

When you run the program, you will see:

```id="2m8xk0"
[0] TO ENCODE TEXT
[1] TO DECODE MORSE CODE
[00] TO EXIT
```

Example usage:

```id="e0c9a2"
ENTER CHOICE : 0
ENTER TEXT: HELLO
```

---

# Requirements

Python **3.x**

No external libraries required.

---

# How to Run

1. Clone the repository

```id="v7s2aa"
git clone https://github.com/yourusername/morse-code-tool.git
```

2. Open the project folder

```id="6b1j3h"
cd morse-code-tool
```

3. Run the program

```id="p6fxme"
python morse_code.py
```

---

# Project Structure

```id="xv0jz9"
morse-code-tool/
│
├── morse_code.py
└── README.md
```

---

# How It Works

The program uses a **Python dictionary** that maps:

* Characters → Morse code

Example:

```id="i8prdw"
'A': '.-'
'B': '-...'
'C': '-.-.'
```

A **reverse dictionary** is automatically generated for decoding:

```id="b9z5qk"
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
```

This allows quick lookup when converting Morse code back to text.

---

# Supported Characters

* Letters **A–Z**
* Numbers **0–9**
* Common punctuation
* Space between words (`/`)

Unsupported characters are replaced with:

```id="7r1xt9"
?
```

---

# Learning Purpose

This project helps beginners learn:

* Python dictionaries
* String manipulation
* Command-line programs
* Encoding and decoding logic

---

# Author

**Sayan**

BCA Student
Python Learning Project

---

# License

Free to use for **educational purposes**.
