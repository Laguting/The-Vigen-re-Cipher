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
start = input("\n\n\33[1m\33[33mDo you want to start the program?\U0001F481 \n Enter Y if 'Yes' and N if 'No': \33[0m")
start = start.upper()
if start == "Y":
    print("\n\033[96m\33[4mThe Program is Starting...\033[0m\n")
    def countdown(n):
            if(n==0):
                print ("\n\33[45m\033[3mThank you for your patience\033[0m" + "\33[45m\033[3m!\033[0m\n")
            else:
                print(n)
                countdown(n-1)
    countdown(5)
elif start == "N":
    quit
else:
    quit

# Get the user's message and keyword make the code replace the input into uppercase letters with no spaces
instruction = Figlet(font = "bubble")
print("\33[7m-+°\33[0m" * 45)
print(colored(instruction.renderText("Read the Following !!!"), "red"))
inst_content = ("\33[102mEnter the Message and Keyword you have in mind below\U0001F53D \033[0m")
message_input = input("\n\33[104mMessage\U0001F4AC: \33[0m")
message_input = message_input.upper().replace(" ","")
key_input = input("\n\n\33[105mKey\U0001F511: \33[0m")
key_input = key_input.upper().replace(" ","")
print("")
print("\33[7m-+°\33[0m" * 45)

# Check the equivalent numbers of the letters inputted (Message & Key)
message_input = [ord(char) - 65 for char in message_input if char.isalpha()]
key_input = [ord(char) - 65 for char in key_input]

# Add the equivalent numbers of the letters inputted (Message & Key)
ciphered_txt = []
for i, val in enumerate(message_input):
    key_val = key_input[i % len(key_input)]
    ciphered_val = (val + key_val) % 26
    ciphered_txt.append(ciphered_val)
# Get the equivalent letters of the sum extracted from the Message & Key
ciphered_txt = ''.join([chr(val + 65) for val in ciphered_txt])

# Print the Ciphertext
print("")
reveal_rslt = Figlet(font = "speed")
print(colored(reveal_rslt.renderText("HERE IS THE RESULT..."), "cyan"))
print("\n\33[43m\33[41mThe result is: \33[0m", ciphered_txt, "\n\n")
print("\33[32m-+°\33[0m" * 45)

# Outro
ou_tro = Figlet(font = "bubble")
print(colored(ou_tro.renderText("Thank you for availing our service!"), "green")) 
closing = Figlet(font = "isometric3")
print(colored(closing.renderText("Closing..."), "white"))