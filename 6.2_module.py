def is_admin(func):
    def wrapper(user_type: str):
        if user_type != 'admin':
            raise ValueError("Permission denied")  
        return func(user_type) 
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print("Showing customer receipt...")  


try:
    show_customer_receipt(user_type='user')  
except ValueError as e:
    print(e)  

'''
try:
    show_customer_receipt(user_type='admin') 
except ValueError as e:
    print(e)  

'''