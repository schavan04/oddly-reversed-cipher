import os
import utils

def run_encoder():
    os.system('clear')
    message = ""
    while message != ":q!":
        try:
            message = utils.take_input()
            enc_message = utils.encode(message)
            print("\n" + enc_message)
        except KeyboardInterrupt:
            print("\n\n  ** PROGRAM EXITED **\n")
            break

if __name__ == "__main__":
    run_encoder()