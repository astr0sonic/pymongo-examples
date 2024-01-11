from uuid import uuid4

from connection import client

accounts_collection = client.bank.accounts

new_account = {
    "account_id": uuid4(),
    "balance": 1000,
}

result = accounts_collection.insert_one(new_account)

print(f"Inserted document ID: {result.inserted_id}")
