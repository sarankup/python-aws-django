from django.http import HttpResponse
from django.shortcuts import render
import datetime
import boto3
from datetime import date
from boto3.dynamodb.conditions import Key
import uuid
from django.shortcuts import redirect



#refer to the aws boto3 documentation for more details.
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
def connect():
    dynamoClient = boto3.resource("dynamodb", region_name="us-east-1", aws_access_key_id='', aws_secret_access_key='')
    dynamoDbTable = dynamoClient.Table("todo")
    return dynamoDbTable


def index(request):
    dynamoDbTable = connect()
    response = dynamoDbTable.scan()
    return render(request, "todo.html", {"todos": response["Items"] })

'''
This method read record(s) by query using the partion key
And print them by loop
'''
def read(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
        print(response["Items"][i])

'''
This method read the record from the db and update the values back to db
'''
def update(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
        response["Items"][i]["age"]=30
        print(response["Items"][i])
        dynamoDbTable.put_item(Item=response["Items"][i])


#This method remove the record by the key was send.
def delete(request):
    dynamoDbTable = connect()
    dynamoDbTable.delete_item(Key={'id':request.GET["id"]})
    return redirect('/todo')





def karan(request):
    return HttpResponse("Hello Karan Saran")


def create(request):
    dynamoDbTable = connect()
    context = dynamoDbTable.put_item(Item={"id": str(uuid.uuid4()), 'name': request.POST.get("name", "")})
    return redirect('/todo')
