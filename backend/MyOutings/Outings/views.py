from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import OutingSerializer
from .models import Outing

# get all outings
@api_view(['GET'])
def getOutings(request):
	outings = Outing.objects.all().order_by('-updated')
	serializer = OutingSerializer(outings, many=True)

	return Response(serializer.data)


# get single outing
@api_view(['GET'])
def getOuting(request, pk):
	outing = Outing.objects.get(id=pk)
	serializer = OutingSerializer(outing, many=False)

	return Response(serializer.data)


# update outing
@api_view(['PUT'])
def updateOuting(request, pk):
	data = request.data
	outing = Outing.objects.get(id=pk)
	serializer = OutingSerializer(instance=outing, data=data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data)


# delete outing
@api_view(['DELETE'])
def deleteOuting(request, pk):
	data = request.data
	outing = Outing.objects.get(id=pk)
	outing.delete()

	return Response("outing was deleted")


# create outing
@api_view(['POST'])
def createOuting(request):
	data = request.data 
	outing = Outing.objects.create(
		title = data['title'],
		place = data['place'],
		date = data['date'],
		participants = data['participants'],
		costs = data['costs'],
	)
	serializer = OutingSerializer(outing, many=False)

	return Response(serializer.data)

# List of endpoints
@api_view(['GET'])
def getRoutes(request):
	routes = [
		{
		"Endpoint": "/outings/",
		"method": "GET",
		"body": None,
		"description": "Returns an array of notes"
		},
		{
		"Endpoint": "/outings/id",
		"method": "GET",
		"body": None,
		"description": "Returns a single outing object"
		},
		{
		"Endpoint": "/outings/create",
		"method": "POST",
		"body": {"body": ""},
		"description": "Creates a new outing with data sent in post request"
		},
		{
		"Endpoint": "/outings/id/update",
		"method": "PUT",
		"body": {"body": ""},
		"description": "Creates an existing outing with data sent in post request"
		},
        {
		"Endpoint": "/outings/id/delete",
		"method": "Delete",
		"body": None,
		"description": "Deletes specific outing item"
		},
    ]
	return JsonResponse(routes, safe=False)
