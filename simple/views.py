from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import urlparse
# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def test_method(request):
    file = open('temp.svg', 'w')
    file.write(request.data['svg'])
    return HttpResponse("Hello world ")