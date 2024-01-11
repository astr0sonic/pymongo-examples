from pprint import pprint
from uuid import UUID

from connection import client

accounts_collection = client.bank.accounts

document_to_update = {"account_id": UUID("3e673226-0ed0-464f-ac8f-fade4af66806")}

account = accounts_collection.find_one(document_to_update)
print("Before update:")
pprint(account)

add_to_balance = {"$inc": {"balance": 100}}

result = accounts_collection.update_one(document_to_update, add_to_balance)

print(f"Documents updated: {result.modified_count}")

account = accounts_collection.find_one(document_to_update)
print("After update:")
pprint(account)

client.close()
