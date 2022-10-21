def stemmer(text):
    text_list = [word for word in text.split()]
    suffix_list = ['ed', 'ly', 'ing']
    answer = []

    for word in text_list:
        for suffix in suffix_list:
            if word.endswith(suffix):
                word = word[:-len(suffix)]
            else:
                continue
        if len(word) > 8:
            answer.append(word[:8])
        else:
            answer.append(word)

    return ' '.join(answer)


print(stemmer('provided'))
