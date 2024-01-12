from uuid import uuid4

from connection import client

accounts_collection = client.bank.accounts

sender = {
    "account_id": uuid4(),
    "balance": 9999,
}
accounts_collection.insert_one(sender)

reciever = {"account_id": uuid4(), "balance": 5000}
accounts_collection.insert_one(reciever)


def callback(session, transfer):
    accounts = session.client.bank.accounts
    transfers = session.client.bank.transfers

    accounts.update_one(
        {"account_id": transfer["from_id"]},
        {
            "$inc": {"balance": -transfer["amount"]},
        },
        session=session,
    )

    accounts.update_one(
        {"account_id": transfer["to_id"]},
        {
            "$inc": {"balance": transfer["amount"]},
        },
        session=session,
    )

    sender = accounts.find_one({"account_id": transfer["from_id"]}, session=session)
    if sender["balance"] < 0:
        raise Exception("Insufficient balance")

    transfers.insert_one(transfer, session=session)

    print("Transaction completed")


transfer = {
    "transfer_id": uuid4(),
    "from_id": sender["account_id"],
    "to_id": reciever["account_id"],
    "amount": 10000,
}

with client.start_session() as session:
    session.with_transaction(lambda session: callback(session, transfer))

client.close()
