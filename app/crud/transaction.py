from sqlalchemy.orm import Session
from..models import Transaction
from..schemas import TransactionCreate, TransactionUpdate, TransactionResponse
from fastapi import HTTPException
from typing import List

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return db_transaction

def update_transaction(db: Session, transaction_id: int, transaction: TransactionUpdate):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail='Transaction not found')
    for key, value in transaction.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail='Transaction not found')
    db.delete(db_transaction)
    db.commit()
    return db_transaction