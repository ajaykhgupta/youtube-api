import pymongo
import pymodm

from pymodm import connect, fields,  MongoModel
from pymongo import ASCENDING, DESCENDING, IndexModel
from .manager import MongoManager
from pymongo import MongoClient

connect("mongodb://localhost:27017/youtube")

class VideoDetails(MongoModel):
    title = fields.CharField()
    description = fields.CharField()
    publishedAt = fields.DateTimeField()
    thumbnailUrl = fields.CharField()
    objects = MongoManager()

    class Meta:
        collection_name = "VideoDetails"
        indexes = [
            IndexModel("title", name="VideoTitle", background=True, unique=True),
            IndexModel("thumbnailUrl", name="ThumbnailUrl", background=True, unique=True)
        ]
        final = True
    
