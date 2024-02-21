from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializer import *

@api_view(['POST', 'PUT'])
def start_coding(request):
    if request.method == "POST":
        
        serializer = CodeFormaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
    if request.method == 'PUT':    
        instance = CodeFormater.objects.get(pk=request.data.id)
        serializer = CodeFormaterSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_code_formater(request):
    id = request.query_params.get('id')
    try:
        code_formater = CodeFormater.objects.get(id=id)
    except CodeFormater.DoesNotExist:
        raise NotFound("CodeFormater with id {} does not exist".format(id))
    serializer = CodeFormaterSerializer(code_formater)
    return Response(serializer.data)


