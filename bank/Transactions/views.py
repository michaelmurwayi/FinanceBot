from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Records
from .serializer import RecordSerializer

@csrf_exempt
def records_list(request):
	"""list all records of transactions """
	if request.method == 'GET':
		record = Records.objects.all()
		serializer = RecordSerializer(record, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = RecordSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status= 400)
@csrf_exempt
def record_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        records = Records.objects.get(pk=pk)
    except Records.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(records)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(records, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        records.delete()
        return HttpResponse(status=204)