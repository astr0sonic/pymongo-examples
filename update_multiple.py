from connection import client

accounts_collection = client.bank.accounts

documents_to_update = {
    "account_type": "savings",
}

set_field = {
    "$set": {"min_balance": 100},
}

result = accounts_collection.update_many(documents_to_update, set_field)

print(f"Documents matched: {result.matched_count}")
print(f"Documents updated: {result.modified_count}")

client.close()
