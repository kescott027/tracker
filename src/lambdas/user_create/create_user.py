#!/usr/bin/env python

"""
creates a new user from a JSON document
"""

from __future__ import print_function
import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    try:
        username = event['username']
        password = event['password']
    except Exception as e:
        respond(e, None)        
    else:
        return respond(None, event)
