import json
import requests
    
def lambda_handler(event, context):
    message = "Very Good Morning "
    url = "https://api.sendgrid.com/v3/mail/send"
    payload = json.dumps({
      "personalizations": [
        {
          "to": [
            {
              "email": "sarankup@gmail.com"
            },
            {
              "email": "karanshetphalkar@gmail.com"
            }
          ]
        }
      ],
      "from": {
        "email": "priya@techiehug.com"
      },
      "subject": "Good Morning Message",
      "content": [
        {
          "type": "text/html",
          "value": message
        }
      ]
    })
    headers = {
      'Authorization': 'Bearer ???',
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response.json())
    }