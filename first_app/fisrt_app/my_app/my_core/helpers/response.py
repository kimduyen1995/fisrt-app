from rest_framework.response import Response

def response_data(data="", status=0, message="Failed"):
    result = {
        'statusCode': status,
        'message': message,
        'data': data
    }
    return Response(result)