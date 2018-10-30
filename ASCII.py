def code(invoerstring):
    outputstring = ''
    for letter in invoerstring:
        outputstring += chr(ord(letter)+3)
    return outputstring

print(code("RutteAlkmaarDen Helder"))