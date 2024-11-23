"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    n = 1  
    while n <= len(result): 
        result.insert(n, '@')  
        n += 2 
    return result

output= fn_hack_9()
print(output)
