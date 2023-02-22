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
    host="phonebook.cluster-cccaxfvn82dm.us-east-1.docdb.amazonaws.com",
    port=27017,
    username="phonebook",
    password="phonebook",
    tls=True,
    tlsInsecure=True,
)

# NOTE: You may need to change these names for the DB and for the collection
RECORD_BOOK_DB = mongo_client["phonebook"]
RECORDS_COLLECTION = RECORD_BOOK_DB["phonebook"]

service = Flask("my-service")


@service.get("/records/")
def list_all_records():
    all_records = []

    # NOTE – Use collection's find() method with an empty filter – {} to retreive all documents.

    return all_records, 200


@service.post("/records/")
def create_new_record():
    record = request.json
    record['id'] = str(uuid4())

    # NOTE - use the collection's insert_one() method to store a new record in the database
    # documentation: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
    # example: https://pymongo.readthedocs.io/en/stable/tutorial.html?highlight=insert_one#inserting-a-document

    return record, 201


@service.get("/records/<record_id>")
def get_one_record(record_id):
    # NOTE – Use find_one() to check, if the record exists and return it, if it exists.
    # Return a 404, if the record does not exist.
    # documentation: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one
    # example: https://pymongo.readthedocs.io/en/stable/tutorial.html?highlight=insert_one#getting-a-single-document-with-find-one


    return record, 200


@service.delete('/records/<record_id>')
def delete_record(record_id):
    # NOTE - use the collection's delete_one() method to store a new record in the database
    # documentation: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.delete_one

    # Use find_one() to check, if the record exists, before deleting.
    # Return a 404, if the record does not exist.
    # documentation: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one

    return "", 204


service.run("0.0.0.0", port=8090)
