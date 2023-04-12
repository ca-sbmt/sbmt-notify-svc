import boto3
from botocore.exceptions import ClientError

def send_email(RECIPIENT):
    SENDER = "surasani.rama@themusings.tech" # replace

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-2"

    # The subject line for the email.
    SUBJECT = "This is test email"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Test Mail")
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Hey Hi...</h1>
    <p>This is Test email </p>
    </body>
    </html>
    """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
        
                        'Data': BODY_HTML
                    },
                    'Text': {
        
                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

# send_email("vishnu123sai@gmail.com")