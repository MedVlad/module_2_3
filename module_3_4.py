def del_prefix_ending(word):
    result = word
    prefix_ending = ['ment', 'dis', 'iest', 'alcum', 'ies']
    if word[0] == 'o':
        result = word.replace('o', '', 1)
    for pref_end in prefix_ending:
        result = result.replace(pref_end, '')
    return result

def single_root_words(root_word, *other_words):
    result = []
    root = del_prefix_ending(root_word.lower())
    i = 0
    word = ''
    while i < len(other_words):
        word = del_prefix_ending(other_words[i].lower())
        if root == word:
            result.append(other_words[i])
        i += 1
    return result


result1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

print(result1)
print(result2)