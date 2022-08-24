from user.models import Details


class MyCustomMiddleware:
    def __init__(self, get_res):
        self.get_res = get_res

    def __call__(self, request):
        res = self.get_res(request)

        url = request.path
        method = request.method
        print(url, method)
        Details.objects.create(method=method, url=url)
        return res



