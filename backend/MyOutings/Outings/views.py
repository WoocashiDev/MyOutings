from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
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
