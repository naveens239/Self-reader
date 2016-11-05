from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pacereader.models import Passage, Subject
from api.serializer import PassageSerializer, SubjectSerializer
import json,ast


@api_view(['GET'])
def passage_list(request, format=None):
    if request.method == 'GET':
        passages = Passage.objects.all().order_by('?')
        serializer = PassageSerializer(passages, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def subject_list(request, format=None):
    if request.method == 'POST':
        data = request.POST
        data = ast.literal_eval(json.dumps(data))
        for key, value in data.iteritems():
            key_data = json.loads(key)
        for i in key_data:     
            serializer = SubjectSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

