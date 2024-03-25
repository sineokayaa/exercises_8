import json

# [["f", 10], ["k", 9], ["s", 29], ["w", 9]]
lst = input()
lst_json = json.loads(lst)

lst_json.sort(key=lambda x: x[1])
print(lst_json[::-1])
