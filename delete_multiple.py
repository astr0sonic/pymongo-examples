from pprint import pprint
from uuid import uuid4

from connection import client

accounts_collection = client.bank.accounts

accounts = []
for i in range(5):
    account = {
        "account_id": uuid4(),
        "account_type": "checking",
        "balance": (i + 1) * 100000,
    }
    accounts.append(account)
result = accounts_collection.insert_many(accounts)
print(f"Documents inserted: {len(result.inserted_ids)}")

big_balance = {
    "balance": {"$gte": 100000},
}

account = accounts_collection.find_one(big_balance)
pprint(account)

result = accounts_collection.delete_many(big_balance)

print(f"Documents deleted: {result.deleted_count}")

account = accounts_collection.find_one(big_balance)
pprint(account)

client.close()
