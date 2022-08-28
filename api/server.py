from http import server
import pymongo
import requests
import json
import asyncio

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["youtube"]
mycol = mydb["VideoDetails"]



async def fun1():
    # await asyncio.sleep(10)
    result={}
    response_API={}
    KEY = "AIzaSyDpp9lDRRtv115hfv1cXHiBhMTcPpmXg8Q" # API KEY 
    url = "https://www.googleapis.com/youtube/v3/search?"+ KEY + "&part=snippet&q=football"
    response_API = requests.get(url)
    data=json.loads(response_API.content)
    value =data['items'][0]
    snippet_data=value['snippet']
    result.update({"publishedAt":snippet_data.get('publishedAt'),"title":snippet_data.get('title'),"description":snippet_data.get('description'),"thumbnailUrl":snippet_data['thumbnails']['default']['url']})
    title = mycol.find_one({"title":result.get("title")})
    if not title:
        mycol.insert_one(result)
    return result


async def main():
    while(True):
        task1 = asyncio.create_task(fun1())
        await task1

asyncio.run(main())

