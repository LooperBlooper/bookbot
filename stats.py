
def count_words(file_contents):
    return len(file_contents.split())

def count_chars(file_contents):
    dict = {}
    for char in file_contents:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(item):
    return item["num"]

def dict_list(dict_sep):
    list_dict = []
    for key, value in dict_sep.items():
        if key.isalpha():
            list_dict.append({"char":key, "num":value})
    list_dict.sort(key=sort_on, reverse=True)
    return list_dict