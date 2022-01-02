from django.http.response import JsonResponse

# Create your views here.
def getHi(request):
  return JsonResponse({"message":"Hello world"},safe=False)