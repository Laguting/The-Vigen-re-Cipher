# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: The inputted message and keyword by the user which should be in all uppercase and no spaces to be ciphered using Vigenere cipher.
# Initial Messages
from pyfiglet import Figlet
from termcolor import colored
ti_tle = Figlet(font = "starwars")
print("\33[1m_" * 177)
print(colored(ti_tle.renderText("\nTHE VIGENERE CIPHER"), "magenta"))
print("\33[1m_" * 177)

welcome = Figlet (font = "slant")
print("\33[36m_\33[0m" * 177)
print(colored(welcome.renderText("HI, WELCOME!"), "yellow"))
print("\33[36m_\33[0m" * 177)

# Start the program
# Get the user's message and keyword
# Check the equivalent numbers of the letters inputted (Message & Key)
# Add the equivalent numbers of the letters inputted (Message & Key)
# Get the equivalent letters of the sum extracted from the Message & Key
# Print the Ciphertext
# Outro