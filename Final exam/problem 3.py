def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    
    # establishing manadarin digits for western equivalent
    mandarin_dict = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    # initiating key variables     
    result =''
        
    #if the number is a single digit, then do a single looku  
    if 0 <= int(us_num) <= 9:
        result += mandarin_dict[us_num[0]]   
    #if the number hast two digits, then do two lookups
    if 10 <= int(us_num) <= 19:
        if us_num == '10':
            result += mandarin_dict['10']
        else:
            result += mandarin_dict['10']
            result += ' '
            result += mandarin_dict[us_num[1]]
    #if the number has three digits, then do three look 
    if 20 <= int(us_num) <= 99:
        if us_num[1] == '0':
            result += mandarin_dict[us_num[0]]
            result += ' '
            result += mandarin_dict['10']
        else:
            result += mandarin_dict[us_num[0]]  
            result += ' '
            result += mandarin_dict['10']
            result += ' '
            result += mandarin_dict[us_num[1]]
    # return final result
    return result
          

          
          
print(convert_to_mandarin('97'))  