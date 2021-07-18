lower_alph = list("abcdefghijklmnopqrstuvwxyz")
upper_alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower_key = [e for e in reversed(lower_alph)]
upper_key = [e for e in reversed(upper_alph)]

def take_input():
    message = input("\n  (Enter ':q!' to exit) Enter message: ")
    return message

def encode(message):
    enc_words = []
    words = message.split()
    for word in words:
        enc_word = ""
        letters = list(word)
        for i in range(len(letters)):
            if letters[i] not in lower_alph and letters[i] not in upper_alph:
                enc_word += letters[i]
            else:
                if i % 2 != 0:
                    enc_word += letters[i]
                else:
                    if letters[i].islower():
                        j = lower_alph.index(letters[i])
                        enc_word += lower_key[j]
                    else:
                        j = upper_alph.index(letters[i])
                        enc_word += upper_key[j]
        enc_words.append(enc_word)
    enc_message = " ".join(enc_words)
    return enc_message