def is_all_upper(text: str) -> bool:
    # your code here
    #return True if bool(text.strip()) is False else text.isupper() 
    #bool(string) string안이 공백이면 False를 출력한다. 띄어쓰기라도 있는 경우에는 True를 출력한다.
    #return True if bool(text) is False else text.isupper()
    
    #if bool(text) is False :
    #    return True
    #elif type(text) is int :
    #    return True  
    #elif len(text.strip()) is 0 :
    #    return True
    #else:    
    #    return text.isupper() if text.isdigit() is False else True 
    return True if type(text) is int else text == text.upper()

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper(123) == True

    a=is_all_upper('ALL UPPER')
    b=is_all_upper('all lower')
    c=is_all_upper('mixed UPPER and lower')
    d=is_all_upper('')
    print(type(b))
    print("Coding complete? Click 'Check' to earn cool rewards!")
