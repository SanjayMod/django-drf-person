from rest_framework.response import Response


def get_response_schema(data, error, status_code):
    """ Utility: Response structure """
    
    return Response({
        'data': data,
        'error': error,
    }, status=status_code)
