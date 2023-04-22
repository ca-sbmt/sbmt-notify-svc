import json
from app.services.ses import send_email
def lambda_handler(event, context):
    print(event)
    try:
        for record in event['Records']:
            payload = record["body"]
            print(str(payload))
            res = send_email(str(payload))
            print(res)
            return {
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }
    except Exception as e:
        print(e)
        return {
            'statusCode': 400
            }
    
    
