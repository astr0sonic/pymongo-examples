from uuid import UUID

from connection import client

accounts_collection = client.bank.accounts

new_account = {
    "account_id": UUID("3e673226-0ed0-464f-ac8f-fade4af66806"),
    "balance": 1000,
}

result = accounts_collection.insert_one(new_account)

print(f"Inserted document ID: {result.inserted_id}")
