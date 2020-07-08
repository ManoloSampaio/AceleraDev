from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from collections import Counter
from django.http import JsonResponse
import json
def lambda_function(request):
    serializer = json.load(request)
    count =  list(Counter( serializer['question']).values())
    answer = {'solution':count}
    #answer_final = json.dumps(list(answer.values()))
    return JsonResponse(answer, status=200)

