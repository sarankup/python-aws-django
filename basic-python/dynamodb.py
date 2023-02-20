'''
This python program is a basic example of how use the AWS DynamoDB.
Basically every database has 4 key operations CURD.
C = Create Record
U = Update Record
R = Read Read
D = Delete Record

This program assumes you have already setup the followings:
1. AWS account with IAM user + Access Keys with DynamodDB full acces Permission
'''

import boto3
from datetime import date
from boto3.dynamodb.conditions import Key


#refer to the aws boto3 documentation for more details.
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
def connect():
    dynamoClient = boto3.resource("dynamodb", region_name="us-east-1", aws_access_key_id='PUT YOUR KEY', aws_secret_access_key='PUT YOUR SECRET')
    dynamoDbTable = dynamoClient.Table("mycontacts")
    return dynamoDbTable


#After the connection, lets create a new record in the database.
#Make sure we have the partion key has been declard while creating the DynamoDB Table
#In this program, email column used as the partion key
#DynamoDB requires minimum 1 partion. It have have as many as you wish.
def create(dynamoDbTable):
    response = dynamoDbTable.put_item(Item={'name': "Saran", 'age': 40, "email":"abc@gmail.com"})
    print(response)

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
def delete(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
        dynamoDbTable.delete_item(Key={'email':'abc@gmail.com'})


'''
All python program starts from the main functions as follows
'''            
if __name__ == "__main__":
    #As it starts, this program creates DynamoDB refer by the following connect method.
    dynamoDbTable = connect()
    
    create(dynamoDbTable)    
    #read(dynamoDbTable)
    #update(dynamoDbTable)
    #delete(dynamoDbTable)
    