def swap_case(s):
    sentence=""
    for i in s:
        if i.isupper():
            sentence+= i.lower()
        elif i.islower():
            sentence+=i.upper()
        else:
            sentence+=i
    
    return sentence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)