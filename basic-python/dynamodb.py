import boto3
from datetime import date
from boto3.dynamodb.conditions import Key


def connect():
    dynamoClient = boto3.resource("dynamodb", region_name="us-east-1", aws_access_key_id='PUT YOUR KEY', aws_secret_access_key='PUT YOUR SECRET')
    dynamoDbTable = dynamoClient.Table("mycontacts")
    return dynamoDbTable

def create(dynamoDbTable):
    response = dynamoDbTable.put_item(Item={'name': "Saran", 'age': 40, "email":"abc@gmail.com"})
    print(response)

    
def read(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
            print(response["Items"][i])
            
def update(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
            response["Items"][i]["age"]=30
            print(response["Items"][i])
            dynamoDbTable.put_item(Item=response["Items"][i])

def delete(dynamoDbTable):
    response = dynamoDbTable.query(KeyConditionExpression=Key('email').eq("abc@gmail.com"))
    for i in range(0, len(response["Items"])):
            dynamoDbTable.delete_item(Key={'email':'abc@gmail.com'})
            
if __name__ == "__main__":
    dynamoDbTable = connect()
    create(dynamoDbTable)
    #read(dynamoDbTable)
    #update(dynamoDbTable)
    #delete(dynamoDbTable)
    