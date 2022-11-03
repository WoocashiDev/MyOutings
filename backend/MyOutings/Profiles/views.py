from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProfileSerializer
from .models import Profile


# get all profiles
@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all().order_by("-nickname")
    serializer = ProfileSerializer(profiles, many=True)

    return Response(serializer.data)


# get single profile
@api_view(['GET'])
def getProfile(request, pk):
	profile = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(profile, many=False)

	return Response(serializer.data)


# update profile
@api_view(['PUT'])
def updateProfile(request, pk):
	data = request.data
	profile = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(instance=profile, data=data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data)


# delete profile
@api_view(['DELETE'])
def deleteProfile(request, pk):
	data = request.data
	profile = Profile.objects.get(id=pk)
	profile.delete()

	return Response("profile was deleted")


# create profile
@api_view(['POST'])
def createProfile(request):
	data = request.data 
	profile = Profile.objects.create(
		user = data['user'],
		nickname = data['nickname']
	)
	serializer = ProfileSerializer(profile, many=False)

	return Response(serializer.data)

# List of endpoints
@api_view(['GET'])
def getRoutes(request):
	routes = [
		{
		"Endpoint": "/profiles/",
		"method": "GET",
		"body": None,
		"description": "Returns an array of Profiles"
		},
		{
		"Endpoint": "/profiles/id",
		"method": "GET",
		"body": None,
		"description": "Returns a single Profile object"
		},
		{
		"Endpoint": "/profiles/create",
		"method": "POST",
		"body": {
			"nickname": "",
			"user": "" 
			},
		"description": "Creates a new Profile with data sent in post request"
		},
		{
		"Endpoint": "/profiles/id/update",
		"method": "PUT",
		"body": {"body": ""},
		"description": "Updates an existing Profile with data sent in post request"
		},
        {
		"Endpoint": "/profiles/id/delete",
		"method": "Delete",
		"body": None,
		"description": "Deletes specific Profile object"
		},
    ]
	return Response(routes)