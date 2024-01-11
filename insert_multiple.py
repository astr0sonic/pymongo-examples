from uuid import uuid4

from connection import client

accounts_collection = client.bank.accounts

account_1 = {
    "account_id": uuid4(),
    "account_type": "checking",
    "balance": 500,
}

account_2 = {
    "account_id": uuid4(),
    "account_type": "savings",
    "balance": 2000,
}

new_accounts = [account_1, account_2]

result = accounts_collection.insert_many(new_accounts)

print(f"Inserted document IDs: {result.inserted_ids}")

client.close()
