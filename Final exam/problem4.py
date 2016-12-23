def longest_run(input_list):
    
    L_copy1 = input_list[:]  
    L_copy2 = input_list[:] 
    
    # IMPLEMENTATION FOR DECREASING NUMBERS
    def decrease_run(input_list):
        ordered_batch = []
        while input_list and (not ordered_batch or ordered_batch[-1] >= input_list[0]):
            ordered_batch.append(input_list[0]) # keep appending ordered numbers
            input_list = input_list[1:] # shrink the list after appending item
        return ordered_batch, input_list # return first batch of ordered numbers and remaining list items

    decr_result = []
    while input_list: # iterate while there is still an input list available
        sublist, input_list = decrease_run(input_list) # return new batch of ordered numbers 
        decr_result.append(sublist) # add all batches together
    # store the longest batch as the best
    best_dec = max(decr_result, key = len)
    
    
    # IMPLEMENTATION FOR INCREASING NUMBERS
    def increase_run(L_copy1):
        ordered_batch = []
        while L_copy1 and (not ordered_batch or ordered_batch[-1] <= L_copy1[0]):
            ordered_batch.append(L_copy1[0]) # keep appending ordered numbers
            L_copy1 = L_copy1[1:] # shrink the list after appending item
        return ordered_batch, L_copy1 # return first batch of ordered numbers and remaining list items

    incr_result = []
    while L_copy1: # iterate while there is still an input list available
        sublist, L_copy1 = increase_run(L_copy1) # return new batch of ordered numbers 
        incr_result.append(sublist) # add all batches together
    # store the longest batch as the best
    best_inc = max(incr_result, key = len)
  
    
   
    if len(best_inc) == len(best_dec):
        if L_copy2.index(best_inc[0]) < L_copy2.index(best_dec[0]):
            return sum(best_inc)
        else:
            return sum(best_dec)
    elif len(best_inc) > len(best_dec):
        return sum(best_inc)
    else:
        return sum(best_dec)

print(longest_run([3, 2, -1, 2, 7]))
