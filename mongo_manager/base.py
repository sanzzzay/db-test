from typing import Optional, Dict, List, Any
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from bson.objectid import ObjectId

class MongoManager:
    """
    A manager class for MongoDB operations providing a clean interface
    for common database interactions.
    """
    
    def __init__(self, connection_string: str, database_name: str):
        """
        Initialize the MongoDB connection.
        
        Args:
            connection_string (str): MongoDB connection URI
            database_name (str): Name of the database to use
        """
        self.client: MongoClient = MongoClient(connection_string)
        self.db: Database = self.client[database_name]
        
    def get_collection(self, collection_name: str) -> Collection:
        """
        Get a collection by name.
        
        Args:
            collection_name (str): Name of the collection
            
        Returns:
            Collection: MongoDB collection object
        """
        return self.db[collection_name]
    
    def insert_one(self, collection_name: str, document: Dict) -> str:
        """
        Insert a single document into a collection.
        
        Args:
            collection_name (str): Name of the collection
            document (Dict): Document to insert
            
        Returns:
            str: ID of the inserted document
        """
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return str(result.inserted_id)
    
    def insert_many(self, collection_name: str, documents: List[Dict]) -> List[str]:
        """
        Insert multiple documents into a collection.
        
        Args:
            collection_name (str): Name of the collection
            documents (List[Dict]): List of documents to insert
            
        Returns:
            List[str]: List of inserted document IDs
        """
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        return [str(id) for id in result.inserted_ids]
    
    def find_one(self, collection_name: str, query: Dict, projection: Optional[Dict] = None) -> Optional[Dict]:
        """
        Find a single document in a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to filter documents
            projection (Optional[Dict]): Fields to include/exclude in the result
            
        Returns:
            Optional[Dict]: Found document or None
        """
        collection = self.get_collection(collection_name)
        return collection.find_one(query, projection)
    
    def find_many(self, 
                 collection_name: str, 
                 query: Dict, 
                 projection: Optional[Dict] = None,
                 sort: Optional[List] = None,
                 limit: Optional[int] = None) -> List[Dict]:
        """
        Find multiple documents in a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to filter documents
            projection (Optional[Dict]): Fields to include/exclude in the results
            sort (Optional[List]): List of (key, direction) pairs for sorting
            limit (Optional[int]): Maximum number of documents to return
            
        Returns:
            List[Dict]: List of found documents
        """
        collection = self.get_collection(collection_name)
        cursor = collection.find(query, projection)
        
        if sort:
            cursor = cursor.sort(sort)
        if limit:
            cursor = cursor.limit(limit)
            
        return list(cursor)
    
    def update_one(self, 
                  collection_name: str, 
                  query: Dict, 
                  update: Dict,
                  upsert: bool = False) -> int:
        """
        Update a single document in a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to find document to update
            update (Dict): Update operations to apply
            upsert (bool): Whether to insert if document doesn't exist
            
        Returns:
            int: Number of modified documents
        """
        collection = self.get_collection(collection_name)
        result = collection.update_one(query, update, upsert=upsert)
        return result.modified_count
    
    def update_many(self,
                   collection_name: str,
                   query: Dict,
                   update: Dict,
                   upsert: bool = False) -> int:
        """
        Update multiple documents in a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to find documents to update
            update (Dict): Update operations to apply
            upsert (bool): Whether to insert if documents don't exist
            
        Returns:
            int: Number of modified documents
        """
        collection = self.get_collection(collection_name)
        result = collection.update_many(query, update, upsert=upsert)
        return result.modified_count
    
    def delete_one(self, collection_name: str, query: Dict) -> int:
        """
        Delete a single document from a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to find document to delete
            
        Returns:
            int: Number of deleted documents
        """
        collection = self.get_collection(collection_name)
        result = collection.delete_one(query)
        return result.deleted_count
    
    def delete_many(self, collection_name: str, query: Dict) -> int:
        """
        Delete multiple documents from a collection.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to find documents to delete
            
        Returns:
            int: Number of deleted documents
        """
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query)
        return result.deleted_count
    
    def count_documents(self, collection_name: str, query: Dict) -> int:
        """
        Count documents in a collection that match a query.
        
        Args:
            collection_name (str): Name of the collection
            query (Dict): Query to filter documents
            
        Returns:
            int: Number of matching documents
        """
        collection = self.get_collection(collection_name)
        return collection.count_documents(query)
    
    def aggregate(self, collection_name: str, pipeline: List[Dict]) -> List[Dict]:
        """
        Perform an aggregation pipeline on a collection.
        
        Args:
            collection_name (str): Name of the collection
            pipeline (List[Dict]): Aggregation pipeline stages
            
        Returns:
            List[Dict]: Aggregation results
        """
        collection = self.get_collection(collection_name)
        return list(collection.aggregate(pipeline))
    
    def close(self):
        """Close the MongoDB connection."""
        self.client.close()