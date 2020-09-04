cal = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y
}

def calculator(operation, x, y):
    return cal.get(operation, lambda x, y: None)(x,y)



print(calculator('add', 2, 2))
print(calculator('mul', 2, 6))