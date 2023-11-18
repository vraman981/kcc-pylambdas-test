import boto3
import json


def lambda_handler(event, context):
    dydb = boto3.resource('dynamodb')
    id = event['id']
    data = event['data']
    pytest = dydb.Table("pytest")
    item = {
        'id': id,
        'data': data
    }
    try:
        pytest.put_item(Item=item)
        print("Below item inserted  successfully")
        print(item)
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps("Error.....")
        }
