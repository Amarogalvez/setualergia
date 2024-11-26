import firebase_admin
from firebase_admin import firestore

db = firestore.client()

def create_document(collection, document_id, data):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.set(data)
 
def get_document(collection, document_id):
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

def update_document(collection, document_id, data):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(data)

def delete_document(collection, document_id):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()

def get_all_documents(collection):
    docs_ref = db.collection(collection)
    docs = docs_ref.stream()
    return [doc.to_dict() for doc in docs]
