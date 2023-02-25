from flask import Flask, request
from uuid import uuid4


"""
/records/
  GET -> list of all records
  POST -> creates new record (body of requests should contain a record in json format)

/records/<record_id>
  GET -> returns a single record
  DELETE -> deletes a record with matching id

Record format:
{
   "id": str
   "first_name": str
   "phone_number": str
}
"""
import pymongo

mongo_client = pymongo.MongoClient(
    host="sre.romcheg.me",
    port=27017,
    username="phonebook",
    password="phonebook-pass",
)

# NOTE: You may need to change these names for the DB and for the collection
RECORD_BOOK_DB = mongo_client["phonebook"]
RECORDS_COLLECTION = RECORD_BOOK_DB["records"]

service = Flask("my-service")


@service.get("/records/")
def list_all_records():
    all_records = RECORDS_COLLECTION.find({})
    result = []

    for record in all_records:
        del record['_id']
        result.append(record)

    return result, 200


@service.post("/records/")
def create_new_record():
    record = request.json
    record['id'] = str(uuid4())
    RECORDS_COLLECTION.insert_one(record)
    del record['_id']
    return record, 201


@service.get("/records/<record_id>")
def get_one_record(record_id):
    record = RECORDS_COLLECTION.find_one({"id": record_id})
    # NOTE – Use find_one() to check, if the record exists and return it, if it exists.
    # Return a 404, if the record does not exist.
    # documentation: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one
    # example: https://pymongo.readthedocs.io/en/stable/tutorial.html?highlight=insert_one#getting-a-single-document-with-find-one

    '''posts.find_one({"author": "Eliot"})'''

    if record is None:
        return "", 404
    else:
        del record['_id']
        return record, 200


@service.delete('/records/<record_id>')
def delete_record(record_id):
    record = RECORDS_COLLECTION.find_one({"id": record_id})
    if record is None:
        return "", 404
    else:
        RECORDS_COLLECTION.delete_one({"id": record_id})
        return "", 204

# PUT /records/<record id>
# Updates a record with a provided id with a new data, provided in a the request body.
# Use record creation as an example. To update the record in the database use the update_one() collection's method.

@service.put('/records/<record_id>')
def put_record(record_id):
    new_record_data = request.json
    old_record = RECORDS_COLLECTION.find_one({"id": record_id})

    if old_record is None:
        return "", 404
    else: 
        old_record.update(new_record_data)
        RECORDS_COLLECTION.update_one({"id": record_id}, {"$set": old_record})
        del old_record['_id']
        return old_record, 200

service.run("0.0.0.0", port=8090)
