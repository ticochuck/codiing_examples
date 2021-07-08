phrase = '(Hello World)',
 
def open_close_parenthesis(phrase):
    open_p = '('
    close_p = ')'
    parenthesis_dict = {
        '(': 0,
    }

    for x in phrase:
     
        if x == close_p:
            if parenthesis_dict[open_p] < 1:
                return False
            else:
                parenthesis_dict[open_p] -= 1
        elif x == open_p:
            parenthesis_dict[x] += 1
                            
    if parenthesis_dict[open_p] == 0:
        return True
    
    return False

print(open_close_parenthesis(phrase))