def multi_bracket_validation(input_string):
    count_braces = 0
    count_squares = 0
    count_parens = 0
    last_open = [""]
    
    for x in input_string:
        if x == "}":
            if last_open[-1] != "{":
                print(f'error closing {x}. Doesn’t match opening {last_open[-1]}')
                return False
            else:
                last_open.pop()
            count_braces -= 1
        
        elif x == "]":
            if last_open[-1] != "[":
                print(f'error closing {x}. Doesn’t match opening {last_open[-1]}')
                return False
            else:
                last_open.pop()
            count_squares -= 1
        
        elif x == ")": 
            if last_open[-1] != "(":
                print(f'error closing {x}. Doesn’t match opening {last_open[-1]}')
                return False
            else:
                last_open.pop()
            count_parens -= 1

        elif x == "{":
            count_braces += 1
            last_open.append("{")
        elif x == "[":
            count_squares += 1
            last_open.append("[")
        elif x == "(":
            count_parens += 1
            last_open.append("(")
        
        all_counts = [count_braces, count_squares, count_parens]
            
    if all_counts[0] > 0 & (all_counts[1] >= 0 & all_counts[2] >= 0):
        return False, 'error unmatched opening { remaining.'
    elif all_counts[1] > 0 and (all_counts[0] >= 0 and all_counts[2] >= 0):
        return False, 'error unmatched opening [ remaining.'
    elif all_counts[2] > 0 & (all_counts[0] >= 0 & all_counts[1] >= 0):
        return False, 'error unmatched opening ( remaining.'
    else:
        return True

#1    
print(multi_bracket_validation('{}'))
#2
print(multi_bracket_validation('{}{}{}'))
#3
print(multi_bracket_validation('()[[Extra Characters]]'))
#4
print(multi_bracket_validation('(){}[[]]'))
#5
print(multi_bracket_validation('{}{Code}[Fellows](())'))
#6
print(multi_bracket_validation('[({}]'))
#7
print(multi_bracket_validation('(]('))
#8
print(multi_bracket_validation('{(})'))
#9
print(multi_bracket_validation('{}()[(])'))
#10
print(multi_bracket_validation('}(['))
