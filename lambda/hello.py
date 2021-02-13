import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content.Type': 'text/plain'
        },
        'body': 'Hello, CDK! YOu have hit {}\n'.format(event['path'])
    }
