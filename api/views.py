from django.http import JsonResponse
from django.views import View

from records import models
from . import responses

class LoginAPI(View):
    def get(self, request):
        aadhar_number = request.GET.get('aadhar_number')
        try:
            patient = models.Patient.objects.get(
                user__useraadhar__number=aadhar_number
            )
        except models.Patient.DoesNotExist:
            return responses.Http401()
        return JsonResponse({'login': 'success'})


class CaseListAPI(View):
    def get(self, request):
        patient_id = request.GET.get('patient')

        try:
            patient = models.Patient.objects.get(id=patient_id)
        except models.Patient.DoesNotExist:
            return responses.Http401()
        cases = models.Case.objects.filter(patient=patient)
        return JsonResponse({'cases': cases, 'count': len(cases)})


class CaseDetailAPI(View):
    def get(self, request):
        return JsonResponse({'case': dict()})
