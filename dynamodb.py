import boto3


def hello():
    dynamoClient = boto3.resource("dynamodb", region_name="us-east-1")
    dynamoDbTable = dynamoClient.Table("test")

    dynamoDbDoc = dynamoDbTable.query(IndexName='processed-time_ms-index', KeyConditionExpression=Key('processed').eq(0))
    isTheUpdate = 0
    print("TOTAL RECORDS")
    print(len(dynamoDbDoc["Items"]))
    for i in range(0, len(dynamoDbDoc["Items"])):
        slackFinalStatus = ""
        eachItem = dynamoDbDoc["Items"][i]
        #print(eachItem)
        projectnamelike = "NOTHINGNOTHING"
        project_id = 0
        slackstatus = 1 #Because, slack notication sent already
        pubkitnotestatus = 0
            
            
if __name__ == "__main__":
    hello()