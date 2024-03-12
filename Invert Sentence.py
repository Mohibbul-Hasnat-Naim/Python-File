# text = input('Text:' ).lower()
# print(text)

def intverted_text():
    text = input('Text:' ).lower()
    print(text)
    inverted_text = []
    for letters in text:
        inverted_text.append(letters)

    inverted_text.reverse()
    # print(inverted_text)

    inv_text = ''.join(map(str, inverted_text))
    print(inv_text)

# intverted_text()

def inverted_textV2():
    text = input('Input Text:' )
    # print(text)
    inv_text = ''
    for x in range(len(text),0,-1):         
        inv_text+=(text[x-1])
    print(inv_text)
    print(text+inv_text)

inverted_textV2()