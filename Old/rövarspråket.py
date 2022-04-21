def encode(text):
    vocals = "aeiou"
    count = 0
    for letter in text:
        count += 1
        if letter not in vocals:
            text = text[:count] + "o" + letter + text[count:]
            count += 2
    return text


def decode(text):
    vocals = "aeiou"
    check = False
    out = ""
    for index, letter in enumerate(text):
        if check and letter == "o":
            out += text[index - 1]
            check = False
            continue
        if letter not in vocals:
            check = True
        else:
            out += letter
    return out


print(encode("mangiare"))
print(decode("momanongogiarore"))
