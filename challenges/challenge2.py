   # Function positive_count with three arguments

def positive_count(a, b, c):
   
    positive_nums = [num for num in (a, b, c) if num > 0]
    
    if len(positive_nums) == 2:
        return True
    else:
        return False

result = positive_count(10, -5, 2)
print(result)  