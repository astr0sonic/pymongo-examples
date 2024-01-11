from pprint import pprint
from uuid import UUID

from bson import ObjectId

from connection import client

accounts_collection = client.bank.accounts

document_to_find = {
    "_id": ObjectId("65a04cde396cdab009f0b235"),
    "account_id": UUID("3e673226-0ed0-464f-ac8f-fade4af66806"),
}

account = accounts_collection.find_one(document_to_find)

pprint(account)
