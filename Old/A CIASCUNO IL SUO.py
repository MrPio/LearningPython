def list_word_length(a_list):
    output = []
    for word in a_list:
        output.append(len(word))
    return output


def list_word_length_2(a_list):
    return [len(_) for _ in a_list]


a_list_1 = ["ciao", "bestia!", "lezzo"]
print(list_word_length_2(a_list_1))
