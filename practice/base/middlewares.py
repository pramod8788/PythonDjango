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
        # print("One time Initialization")

    def __call__(self, request):
        # print("This is before view")
        response = self.get_response(request)
        # print("This is after view")
        return response

    def process_view(request, *args, **kwargs):
        print("This process will execute before view")
        # return HttpResponse("This is before View")
        return None
    
    def process_exception(self, request, exception):
        print("Exception Ocurred")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)

    def process_template_response(self, request, response):
        print("Process template response from middleware")
        response.context_data["name"] = "Ramu Kaka"
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

        