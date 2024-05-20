from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TextSerializer


@api_view(['POST'])
def detect_text(request):
    """
    View that enables image reception and recording

    Keyword arguments:
    request -- (django.http.HttpRequest) The HttpRequest object containing all
    information about HTTP request.

    Returns:
    django.http.HttpResponse -- An HttpResponse object representing the view
    response
    """
    serializer = TextSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.save()
        data = {**serializer.data, **text.analyze()}
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def search_word(request):
    searched_word = request.data.get('search_word')
    serializer = TextSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.save()
        data = {**serializer.data, **text.search_word(searched_word)}
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def search_information(request):
    criteria = request.data.get('criteria')
    serializer = TextSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.save()
        data = {**serializer.data, **text.search_information(criteria)}
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

