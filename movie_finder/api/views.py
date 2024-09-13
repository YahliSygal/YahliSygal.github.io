
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Watchlist
from .serializers import WatchlistSerializer
import requests

@api_view(['POST'])
def search_movie(request):
    movie_title = request.data.get('movie_title')
    # JustWatch or external API call logic goes here
    return Response({"status": "Movie found"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def manage_watchlist(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id')
        watchlist = Watchlist.objects.filter(user_id=user_id)
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
