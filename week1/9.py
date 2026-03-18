# import pyperclip
# pyperclip.copy('If you copy some text to the clipboard '
# '(for instance, this sentence) and run this program, the output and clipboard contents become this:')
# text = pyperclip.paste()
# alt_text = ''
# make_uppercase = False
# for character in text:
#     if make_uppercase:
#         alt_text += character.upper()
#     else:
#         alt_text += character.lower()
#     make_uppercase = not make_uppercase
# pyperclip.copy(alt_text)
# print(alt_text)

# pyperclip.copy('Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars')
# text = pyperclip.paste()
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i]= '* '+ lines[i]
# text = '\n'.join(lines)
# pyperclip.copy(text)
# print(text)

def is_phone_number(text):
    if len(text)!= 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!= '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: '+segment)
print('Done')