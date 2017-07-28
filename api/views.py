from django.http import JsonResponse
from django.views import View


class LoginAPI(View):
    def get(self, request):
        return JsonResponse({'login': 'success'})


class CaseListAPI(View):
    def get(self, request):
        cases = []
        return JsonResponse({'cases': cases, 'count': len(cases)})


class CaseDetailAPI(View):
    def get(self, request):
        return JsonResponse({'case': dict()})
