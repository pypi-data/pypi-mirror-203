import boto3
import os

# retrieve AWS credentials from env variables
aws_access_key = "AKIAREUC7U5FWQZZF5KD"
aws_secret_key = "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"

# create a session and CloudFormation client using the credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)
cloudformation = session.client('cloudformation')

# create a new stack
response = cloudformation.create_stack(
    StackName='my-stack',
    TemplateURL='https://s3.amazonaws.com/my-bucket/my-template.yml',
    Parameters=[
        {
            'ParameterKey': 'parameter1',
            'ParameterValue': 'value1'
        }
    ]
)
print(response)

# delete a stack
response = cloudformation.delete_stack(
    StackName='my-stack'
)
print(response)
