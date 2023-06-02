from django.http import HttpResponse, JsonResponse


class CommonTroubleshootingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, e):
        return JsonResponse({'detail':str(e)})
