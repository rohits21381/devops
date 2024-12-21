import boto3

# Initialize a session using Amazon Web Services (AWS)
session = boto3.Session(
    aws_access_key_id='your_access_key_id',
    aws_secret_access_key='your_secret_access_key',
    region_name='your_region'
)

# Create Lambda client
lambda_client = session.client('lambda')

# Load Lambda function code
with open('my_lambda_function.zip', 'rb') as f:
    lambda_code = f.read()

# Create Lambda function
response = lambda_client.create_function(
    FunctionName='myLambdaFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::your_account_id:role/lambda_role',
    Handler='my_lambda_function.lambda_handler',
    Code={'ZipFile': lambda_code},
    Description='My Lambda function',
    Timeout=15,
    MemorySize=128,
    Publish=True
)

print(f"Created Lambda function with ARN: {response['FunctionArn']}")

