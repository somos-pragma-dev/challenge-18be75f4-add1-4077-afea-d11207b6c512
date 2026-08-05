from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..crud import transaction
from..schemas import TransactionCreate, TransactionUpdate, TransactionResponse
from..db.database import get_db

router = APIRouter()

@router.post('/transactions/', response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return transaction.create_transaction(db=db, transaction=transaction)

@router.get('/transactions/{transaction_id}', response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = transaction.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return db_transaction

@router.put('/transactions/{transaction_id}', response_model=TransactionResponse)
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    return transaction.update_transaction(db, transaction_id=transaction_id, transaction=transaction)

@router.delete('/transactions/{transaction_id}', response_model=TransactionResponse)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return transaction.delete_transaction(db, transaction_id=transaction_id)