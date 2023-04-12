# from __future__ import print_function

# def lambda_handler(event, context):
#     for record in event['Records']:
#         print("test")
#         payload = record["body"]
#         print(str(payload))



# def read_and_delete_event_from_queue(event, context ):
#     queue_url = 'SQS_QUEUE_URL'

#     # Receive message from SQS queue
#     response = sqs.receive_message(
#         QueueUrl=queue_url,
#         AttributeNames=[
#             'SentTimestamp'
#         ],
#         MaxNumberOfMessages=10,
#         MessageAttributeNames=[
#             'All'
#         ],
#         VisibilityTimeout=0,
#         WaitTimeSeconds=0
#     )

#     message = response['Messages'][0]
#     receipient = message['Receipient']

#     # Delete received message from queue
#     sqs.delete_message(
#         QueueUrl=queue_url,
#         ReceiptHandle=receipt_handle
#     )
#     print('Received and deleted message: %s' % message)