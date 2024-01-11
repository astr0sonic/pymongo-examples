from pprint import pprint

from connection import client

accounts_collection = client.bank.accounts

documents_to_find = {
    "balance": {"$gt": 999},
}

cursor = accounts_collection.find(documents_to_find)

for account in cursor:
    pprint(account)

client.close()
