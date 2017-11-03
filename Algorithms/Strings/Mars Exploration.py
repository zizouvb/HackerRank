print(len([1 for letter_input,letter_sos in zip(input(),'SOS'*99) if letter_input != letter_sos]))
