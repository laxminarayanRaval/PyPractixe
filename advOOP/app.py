# using Decorators
user = {'uname': "laxminarayan", 'access_level': 'admin'}
# user = {'uname': "laxminarayan", 'access_level': 'user'}


def user_has_permission(access_level='user'):  # making a custom decorator
    def my_decorator(func):  # a function Higher Order Function (having function as argument)
        def secure_func(*param):  # a function has parameter (param) for allowing other function to have it
            if user.get('access_level') == access_level:
                return func(*param)  # returning an argument function
        return secure_func  # returning "no idea why"
    return my_decorator  # returning Higher Order Function


# @user_has_permission('user')
@user_has_permission('admin')  # using Decorator
def my_function(param):  # passing a function as argument (only because of python first-class function)
    """Making Generic Decorators"""
    return f"<User {user.get('uname')} is now doing operation {param}, he is '{user.get('access_level')}' after all>"


@user_has_permission()  # default parameter 'user'
def my_another_func():
    """Another Function for testing Generic Decorator"""
    return f"<A Hello from Another Function>"


# print(my_function("Deleting Database"))
# print(my_another_func())
