def word_count(filepath):
    with open(filepath) as f:
        file = f.read()
        word_split = file.split()
    return len(word_split)

def char_count(filepath):
    with open(filepath) as f:
        file = f.read()
        lower_file = file.lower()
        frequency = {}
        for char in lower_file:
            frequency[char] = frequency.get(char,0) + 1
    return frequency

def sort_on(dict):
    return list(dict.values())[0]

def sort_list(dict_count):
    list_dict = []
    for key, value in dict_count.items():
        list_dict.append({key: value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict