# chroma_service.py

import chromadb
from chromadb.config import Settings

class ChromaService:
    def __init__(self, collection_name: str, chroma_client: chromadb.EphemeralClient):
        self.collection_name = collection_name
        self.chroma_client = chroma_client
        self.collection = self.chroma_client.get_or_create_collection(name=collection_name)

    def add_document(self, document_id: str, document_text: str, metadata: dict = None):
        """
        Agrega un documento a la colección.

        :param document_id: ID único del documento.
        :param document_text: Texto del documento.
        :param metadata: Metadatos opcionales del documento.
        """
        self.collection.add(
            ids=[document_id],
            documents=[document_text],
            metadatas=[metadata] if metadata else None
        )

    def get_document(self, document_id: str):
        """
        Recupera un documento por su ID.

        :param document_id: ID del documento.
        :return: Documento y metadatos.
        """
        result = self.collection.get(ids=[document_id])
        if result['ids']:
            return {
                'document': result['documents'][0],
                'metadata': result['metadatas'][0] if result['metadatas'] else None
            }
        return None

    def query_documents(self, query_text: str, n_results: int = 5):
        """
        Realiza una consulta en la colección y devuelve los resultados más relevantes.

        :param query_text: Texto de la consulta.
        :param n_results: Número de resultados a devolver.
        :return: Lista de documentos y metadatos.
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

# Configuración del cliente de ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_data")
chroma_service = ChromaService(collection_name="my_collection", chroma_client=chroma_client)