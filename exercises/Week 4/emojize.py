#using emoji library :)

import emoji

text = input("Input: ")
text = emoji.emojize(text, language='alias')
print(text)
