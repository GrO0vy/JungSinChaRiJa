from http.client import HTTPResponse
from django.shortcuts import render

def index(request):
    return HTTPResponse("Hello, world. You're at the polls  index.")
# Create your views here.
