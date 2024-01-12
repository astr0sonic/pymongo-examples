from pprint import pprint
from uuid import uuid4

from connection import client

accounts_collection = client.bank.accounts

account = {
    "account_id": uuid4(),
    "account_type": "checking",
    "balance": 777,
}
result = accounts_collection.insert_one(account)
document_id = result.inserted_id

document_to_delete = {
    "_id": document_id,
}

account = accounts_collection.find_one(document_to_delete)
pprint(account)

result = accounts_collection.delete_one(document_to_delete)

print(f"Documents deleted: {result.deleted_count}")

account = accounts_collection.find_one(document_to_delete)
pprint(account)

client.close()
