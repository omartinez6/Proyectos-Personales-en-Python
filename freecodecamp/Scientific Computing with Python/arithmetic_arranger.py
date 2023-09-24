def arithmetic_arranger(problems, solutions = False):
    
    # Manejo de excepciones
    
    prearranged_up = ''
    prearranged_down = ''
    prearranged_hyphen = ''
    prearranged_results = ''
    arranged_problems = ''
    problems_count = len(problems)
    if problems_count > 5:
        raise IndexError('Error: Too many problems.')
    for problem in problems:
        if not ('+' in problem or '-' in problem):
            raise ValueError('Error: Operator must be \'+\' or \'-\'.')
        elements = problem.split()
        
        element_one = elements[0]
        element_two = elements[2]
        operator = elements[1]
        
        len_one = len(element_one)
        len_two = len(element_two)
        
        if not (element_one.isdigit() and element_two.isdigit()):
            raise TypeError('Error: Numbers must only contain digits.')
        if len_one > 4 or len_two > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')  
    
        # Formateo
        
        max_lenght = 0
        if len_one > len_two:
            max_lenght = len_one
        else:
            max_lenght = len_two
        up = f'{element_one : >{max_lenght + 2}}    '
        down = f'+ {element_two : >{max_lenght - 1}}    '
        hyphen = f'{"-" * (max_lenght + 2)}    '
        
        if operator == '+':
            result = int(element_one) + int(element_two)
        else:
            result = int(element_one) - int(element_two) 
        results = f'{result: >{max_lenght + 2}}    '
        
        
        prearranged_up = prearranged_up + up
        prearranged_down = prearranged_down + down
        prearranged_hyphen = prearranged_hyphen + hyphen
        prearranged_results = prearranged_results + results
    
    if solutions:
        arranged_problems = prearranged_up + '\n' + prearranged_down + '\n' + prearranged_hyphen + '\n' + prearranged_results
    else:
        arranged_problems = prearranged_up + '\n' + prearranged_down + '\n' + prearranged_hyphen
        
   
    return arranged_problems
    
print(arithmetic_arranger(['1 + 1','7865 + 9856','2 + 9783','3 + 5','4 + 34'],True))