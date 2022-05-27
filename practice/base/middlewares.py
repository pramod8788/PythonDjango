from django.shortcuts import HttpResponse
# Function based middleware 

# def my_middleware(get_response):
#     print("One time Initialization")

#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response

#     return my_function


# Class based middleware
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Father Middleware Initialization")

    def __call__(self, request):
        print("This is before Father view")
        response = self.get_response(request)
        print("This is after Father view")
        return response

class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Mother Middleware Initialization")

    def __call__(self, request):
        print("This is before Mother view")
        # response = HttpResponse("Get Out For Test")
        response = self.get_response(request)
        print("This is after Mother view")
        return response

        