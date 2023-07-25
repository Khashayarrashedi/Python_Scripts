
input_str=input("Please type your String: ")
vowels=["A","a","U","u","I","i","E","e","O","o"]

for vowel in vowels:
    input_str=input_str.replace(vowel, '')
    # print(input_str.replace(vowel, ''))

print(input_str)
