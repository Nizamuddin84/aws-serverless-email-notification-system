import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):

    ses.send_email(
        Source='nizzu8436@gmail.com',
        Destination={
            'ToAddresses': ['shaik.nizamuddin8436@gmail.com']
        },
        Message={
            'Subject': {
                'Data': 'AWS Serverless Email'
            },
            'Body': {
                'Text': {
                    'Data': 'Hello! Email sent using AWS Lambda and SES.'
                }
            }
        }
    )

    return {
        'statusCode': 200,
        'body': 'Email Sent Successfully'
    }
