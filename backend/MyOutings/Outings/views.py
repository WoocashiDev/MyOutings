from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import OutingSerializer, ExpenseSerializer
from .models import Outing, Expense
from Profiles.models import Profile


## OUTINGS ##
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

	print(participants)
	outing = Outing.objects.create(
		title = data['title'],
		place = data['place'],
		date = data['date']
	)
	# many to many relationship handling
	participants = Profile.objects.filter(id__in=data['participants'])
	outing.participants.set(participants)

	serializer = OutingSerializer(outing, many=False)

	return Response(serializer.data)

## EXPENSES ##

# get all expenses from the outing
@api_view(['GET'])
def getExpenses(request, pk):
	outing = Outing.objects.get(id=pk)
	expenses = outing.expense_set.all()
	serializer = ExpenseSerializer(expenses, many=True)

	return Response(serializer.data)

# get single expense from particular outing
@api_view(['GET'])
def getExpense(request, pk, expense_id):
	outing = Outing.objects.get(id=pk)
	expense = outing.expense_set.filter(id=expense_id).first()
	serializer = ExpenseSerializer(expense, many=False)

	return Response(serializer.data)

# update expense
@api_view(['PUT'])
def updateExpense(request, pk, expense_id):
	data = request.data
	outing = Outing.objects.get(id=pk)
	expense = outing.expense_set.filter(id=expense_id).first()
	serializer = ExpenseSerializer(instance=expense, data=data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data)


# delete expense
@api_view(['DELETE'])
def deleteExpense(request, pk, expense_id):
	data = request.data
	outing = Outing.objects.get(id=pk)
	expense = outing.expense_set.filter(id=expense_id).first()
	expense.delete()

	return Response("Expense was deleted")

# create expense
@api_view(['POST'])
def createExpense(request, pk):
	data = request.data


	sponsor = Profile.objects.filter(id=data['sponsor']).first()
	beneficient = Profile.objects.filter(id=data['beneficient']).first()
	outing = Outing.objects.filter(id=pk).first()

	expense = Expense.objects.create(
		title = data['title'],
		value = data['value'],
		outing = outing,
		beneficient = beneficient,
		sponsor = sponsor
	)
	
	serializer = ExpenseSerializer(expense, many=False)

	return Response(serializer.data)


# List of endpoints
@api_view(['GET'])
def getRoutes(request):
	routes = [
		{
		"Endpoint": "/outings/",
		"method": "GET",
		"body": None,
		"description": "Returns an array of outings"
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
		"body": {
			"title": "",
			"place": "",
			"date": "",
			"participants": "",
			},
		"description": "Creates a new outing with data sent in post request"
		},
		{
		"Endpoint": "/outings/id/update",
		"method": "PUT",
		"body": {
			"title": "",
			"place": "",
			"date": "",
			"participants": "",
			},
		"description": "Creates an existing outing with data sent in post request"
		},
        {
		"Endpoint": "/outings/id/delete",
		"method": "Delete",
		"body": None,
		"description": "Deletes specific outing item"
		},
		{
		"Endpoint": "/outings/id/expenses",
		"method": "GET",
		"body": None,
		"description": "Returns all expenses associated with particular outing"
		},
		{
		"Endpoint": "/outings/id/expenses/expense_id",
		"method": "GET",
		"body": None,
		"description": "Returns particular expense within the outing"
		},
		{
		"Endpoint": "/outings/id/expenses/create",
		"method": "POST",
		"body": {
			"sponsor": "",
			"beneficient": "",
			"title": "",
			"value": ""
			},
		"description": "Creates a new expense inside of the outing"
		},
		{
		"Endpoint": "/outings/id/expenses/expense_id/edit",
		"method": "PUT",
		"body": {
			"sponsor": "",
			"beneficient": "",
			"title": "",
			"value": ""
			},
		"description": "Updates existing expense within the outing"
		},
		{
		"Endpoint": "/outings/id/expenses/expense_id/delete",
		"method": "DELETE",
		"body": None,
		"description": "Deletes existing"
		},
    ]
	return JsonResponse(routes, safe=False)
