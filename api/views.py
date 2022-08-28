from urllib import request
from django.views import View
from api.models import VideoDetails
from django.http.response import JsonResponse
from api.response import OK
import pymongo
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def search(request) -> OK:
    """search video based on their title and description

    Args:
        request (POST): request method.
        title: title of video.
        description: description of video.

    Returns:
        OK: dictionary data matching tile and description
    """
    if request.method=="POST":
        data = json.loads(request.body)
        response = VideoDetails.objects.find_one(queries=data)
        if response:
            return OK({"data": response})
        return OK({"data":"Not Found"})


class SearchView(View):
    def get(self,request) -> OK:
        """Function to retrieve all the videos data in descending order of their published time

        Args:
            request (GET): request method

        Returns:
            OK: List of all video data
        """
        sort = [("publishedAt", pymongo.DESCENDING)]
        data = VideoDetails.objects.retrieve_all(sort=sort)
        return OK({"data": data})
