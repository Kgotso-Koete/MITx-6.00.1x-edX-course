# generate all combinations of N items
def powerSet(items):
    set_size = len(items)
    # enumerate the 2**N possible combinations
    for permutation in range(2**set_size):
        combo = []
        print(permutation)
        
        # append all items with an 'in' flag (1)
        for item in range(set_size):
            print(bin(item))
            # test bit jth of integer i. Other words, odd numbers have an 'in' flag
            if (permutation >> item) % 2 == 1:
                combo.append(items[item])
        yield combo
        
ps = powerSet(['a','b','c'])
for i in ps:
    print (i)

p