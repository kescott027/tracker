#!/usr/bin/env python

"""
creates a new encounter
"""

import json


def parse_parameters(event):
    try:
        returnParameters = event['queryStringParameters'].copy()
    excpet Exception as e:
        returnParameters = {}   
    try:
        resource_id = event.get('path', '').split(/)[-1]
        if resource_id.isdigit():
            returnParameters['resource_id'] = resource_id
        else:
            return {"parsedParams": None, "err":
                Exception("resource_id is not a number")}
    except Exception as e:
        return {"parsedParams": None, "err": e}
    return {"parsedParams": returnParameters, "err": None}

def lambda_handler(event, context):
    validated_parameters = parse_parameters(event)
    if validated_parameters['err'] is not None:
        return respond(validated_parameters['err'])
    else:
        return respond(None, validated_parameters.get('ParsedParams', None))

