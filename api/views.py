from django.http import JsonResponse
from django.views import View

from records import models
from . import responses, serializers

class LoginAPI(View):
    def get(self, request):
        aadhar_number = request.GET.get('aadhar_number')
        try:
            patient = models.Patient.objects.get(
                user__useraadhar__number=aadhar_number
            )
        except models.Patient.DoesNotExist:
            return responses.Http401()
        return JsonResponse({'patient_id': patient.id, 'name': str(patient)})


class CaseListAPI(View):
    def get(self, request):
        patient_id = request.GET.get('patient_id')

        try:
            patient = models.Patient.objects.get(id=int(patient_id))
        except models.Patient.DoesNotExist:
            return responses.Http401()
        cases = models.Case.objects.filter(patient=patient).order_by('-created')

        serializer = serializers.CaseListSerializer(cases)

        return JsonResponse({
            'cases': serializer.serialize(),
            'count': len(cases)
        })


class CaseDetailAPI(View):
    def get(self, request):
        patient_id = request.GET.get('patient_id')

        try:
            patient = models.Patient.objects.get(id=int(patient_id))
        except models.Patient.DoesNotExist:
            return responses.Http401()

        case_id = request.GET.get('case_id')
        case = models.Case.objects.get(patient=patient, id=int(case_id))

        serializer = serializers.CaseDetailSerializer(case)

        return JsonResponse({
            'case': serializer.serialize()
        })
