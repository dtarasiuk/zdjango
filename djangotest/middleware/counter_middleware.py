from simple.models import Counter

class CounterMiddleware:

    def process_request(self, request):
        data = Counter(url=request.path)
        data.save()
