import itertools


names = ['tom', 'jack', 'cathy', 'july']
letters = (len(name) for name in names)

max_letters = 0
longest_name = None
names.append('dongqihong')

for name, count in zip(names, letters):
    if count > max_letters:
        max_letters = count
        longest_name = name

print(longest_name, max_letters)