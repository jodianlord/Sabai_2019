from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from clinicmodels.models import Patient, Visit
from visit.forms import VisitForm


@api_view(['POST'])
@csrf_exempt
def create_new_visit(request):
    try:
        if 'patient' not in request.POST:
            return JsonResponse({"message": "POST: parameter 'patient' not found"}, status=400)
        patient_id = request.POST['patient']

        # Patient exists, go on to create a new visit
        Patient.objects.get(pk=patient_id)

        visit_form = VisitForm(request.POST)
        if visit_form.is_valid():
            visit = visit_form.save()
            response = serializers.serialize("json", [visit, ])
            return HttpResponse(response, content_type='application/json')
        else:
            return JsonResponse(visit_form.errors, status=400)
    except ObjectDoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)


@api_view(['GET'])
def get_visit_by_id(request):
    try:
        if 'id' not in request.GET:
            return JsonResponse({"message": "GET: parameter 'id' not found"}, status=400)
        visit_id = request.GET['id']
        visit = Visit.objects.get(pk=visit_id)
        response = serializers.serialize("json", [visit, ])
        return HttpResponse(response, content_type="application/json")
    except ObjectDoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)


@api_view(['GET'])
def get_visit_by_patient(request):
    try:
        if 'patient_id' not in request.GET:
            return JsonResponse({"message": "GET: parameter 'patient_id' not found"}, status=400)
        patient_id = request.GET['patient_id']
        visits = Visit.objects.filter(patient=patient_id)
        if visits.count() == 0:
            return JsonResponse({"message": "Visit matching query does not exist"}, status=404)
        response = serializers.serialize("json", visits)
        return HttpResponse(response, content_type="application/json")
    except ObjectDoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)


@api_view(['GET'])
def get_visit_by_status(request):
    try:
        if 'status' not in request.GET:
            return JsonResponse({"message": "GET: parameter 'status' not found"}, status=400)
        status = request.GET['status']
        visits = Visit.objects.filter(status=status)
        if visits.count() == 0:
            return JsonResponse({"message": "Visit matching query does not exist"}, status=404)
        response = serializers.serialize("json", visits)
        return HttpResponse(response, content_type="application/json")
    except ObjectDoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=404)
