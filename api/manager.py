from bson.objectid import ObjectId
from pymodm.errors import ValidationError
from pymodm.manager import Manager
from pymongo.collection import ReturnDocument


class MongoManager(Manager):
    def retrieve_all(self, filters=None, queries=None, projection=None, limit=None, offset=None, sort=None, aggregator=None):
        query = {}
        if queries:
            query = queries

        elif filters:
            query = {"$and": filters}
        resources = self.model.objects.raw(query)

        if projection:
            resources = resources.project(projection)
        
        if not aggregator:
            if sort:
                resources = resources.order_by(sort)

            if offset:
                resources = resources.skip(offset)

            if limit:
                resources = resources.limit(limit)

        return list(resources.values())

    def find_one(self, queries=None, filters=None, projection=None, aggregator=None):
        query = {}
        if queries:
            query = queries

        elif filters:
            query = {"$and": filters}

        result = self.model.objects.raw(query)

        if projection:
            result = result.project(projection)

        if aggregator:
            result = result.aggregate(*aggregator)
            results = list(result)
            if len(results) > 0:
                result = results[0]
            else:
                result = None
            return result

        try:
            result = result.values().first()
        except self.model.DoesNotExist:
            result = None

        return result


    def insert_one(self, data):
        add_document = self.model.from_document(data)
        return add_document.save().to_son().to_dict()

