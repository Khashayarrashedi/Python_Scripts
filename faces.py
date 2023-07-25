def main():
    #---------------------------------------------- inputs
    given_str = input("Type a word or sentence:")
    #---------------------------------------------- func call
    out=convert(given_str)
    #---------------------------------------------- outputs
    print (out)

#---------------------------------------------- ALT 1 (with replace)
# def convert(given_str):
#     mod_given_str =given_str.replace(":)", "🙂").replace(":(", "🙁")
#     return mod_given_str

#---------------------------------------------- ALT 2 (with directory)
def convert(given_str):
    replace_list={":)": "🙂", ":(": "🙁"}
    for char in replace_list.keys():
        given_str= given_str.replace(char, replace_list[char])
    return given_str

main()