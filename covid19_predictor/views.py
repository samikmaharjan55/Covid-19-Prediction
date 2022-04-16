from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .fls_main import calculate_FLS
from django.http import JsonResponse
from .serializers import CovidSymptomsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import CovidSymptoms
# Create your views here.
# @csrf_exempt
# @api_view(('GET',))
# def covid(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         cough_slider = python_data.get('cough_slider', None)
#         fever_slider = python_data.get('fever_slider', None)
#         breath_slider = python_data.get('breath_slider', None)
#         age_field = python_data.get('age_field', None)
#         env = python_data.get('env', None)
#         hypertension = python_data.get('hypertension', None)
#         diabetes = python_data.get('diabetes', None)
#         cardiovascular = python_data.get('cardiovascular', None)
#         respiratory = python_data.get('respiratory', None)
#         immune = python_data.get('immune', None)
#         chance = fls_main.calculate_FLS(cough_slider, fever_slider, breath_slider, int(age_field),
#                                     env, hypertension, diabetes,
#                                     cardiovascular, respiratory, immune)
#         return JsonResponse({"Chance":chance})

@csrf_exempt
def symptoms_db(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_parsed = JSONParser().parse(stream)
        python_serialized = CovidSymptomsSerializer(
            data=python_parsed)
        if python_serialized.is_valid():
            python_serialized.save()
            response = {'Chance': 'chance'}
            last_instance = CovidSymptoms.objects.latest('id')
            cough = last_instance.cough
            print(cough)
            fever = last_instance.fever
            print(fever)
            breath = last_instance.breath
            age = last_instance.age
            environment = last_instance.environment
            hypertension = last_instance.hypertension
            print(hypertension)
            diabetes = last_instance.diabetes
            cardiovascular = last_instance.cardiovascular
            respiratory = last_instance.respiratory
            immune = last_instance.immune
            output = calculate_FLS(cough, fever, breath, age, environment, hypertension, diabetes, cardiovascular, respiratory, immune)

            return JsonResponse(output, safe=False)
        
            # response = {'response': 'Saved successfully'}
            # cough = last_instance.cough
            # fever = last_instance.fever
            # breath = last_instance.breath
            # age = last_instance.age
            # environment = last_instance.environment
            # hypertension = last_instance.hypertension
            # diabetes = last_instance.diabetes
            # cardiovascular = last_instance.cardiovascular
            # respiratory = last_instance.respiratory
            # print('LOLOLOLOL')
            # immune = last_instance.immune
            # chance = calculate_FLS(cough, fever, breath, int(age), int(environment), int(hypertension), int(diabetes), int(cardiovascular), int(respiratory), int(immune))
            # response = JSONRenderer().render(response)
            
            # return HttpResponse(response, content_type='application/json')
        # return HttpResponse(python_serialized.errors, content_type='application/json')
        return JsonResponse(python_serialized.errors, safe = True)
