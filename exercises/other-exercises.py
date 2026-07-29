words = ["apple", "bat", "cherry", "dog", "elderberry"]
#['APPLE', 'CHERRY', 'ELDERBERRY']

new_words = [word.upper() for word in words if len(word) > 3]
print(new_words)

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

def merge_dicts(dict_1, dict_2):
    for key, value in dict_1.items():
        if key in dict_2:
            # print(dict_2.get(key))
            # print(value)
            dict_1[key] = value+dict_2.get(key)
        



print(merge_dicts(dict_a, dict_b))