def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs) 
        except KeyError:
            print("Error: A key you tried to access doesn't exist.")
        except TypeError:
            print("Error: A type mismatch occurred. Check your input types.")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    if data is None:
        raise TypeError("Data cannot be None") 
    print(data['key']) 


print("Testing with missing key:")
some_function_with_risky_operation({'foo': 'bar'})  
'''
print("Testing with valid key:")
some_function_with_risky_operation({'key': 'bar'}) 

print("Testing with None:")
some_function_with_risky_operation(None)  
'''