# aac_crud.py — CS 340 (Grazioso Salvare)
# Author: Julliane Pamfilo
# Purpose: CRUD operations for the 'animals' collection in the 'aac' MongoDB.

from __future__ import annotations
from typing import Any, Dict, List, Optional
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    I keep this class focused: connect once, then expose small CRUD helpers.

    Args:
        username: MongoDB username (e.g., 'aacuser')
        password: MongoDB password (URL-encoded internally)
        host:     MongoDB host (default 'localhost')
        port:     MongoDB port (default 27017)
        db_name:  Database name (default 'aac')
        collection_name: Collection name (default 'animals')
        auth_source: Auth DB ('aac' or 'admin'); default 'aac'
    """

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = "aac",
        collection_name: str = "animals",
        auth_source: str = "aac",
    ) -> None:
        user = quote_plus(username)
        pwd = quote_plus(password)
        uri = f"mongodb://{user}:{pwd}@{host}:{port}/{db_name}?authSource={auth_source}"
        try:
            self.client = MongoClient(uri)
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
        except PyMongoError as e:
            raise RuntimeError(f"Mongo connection failed: {e}")

    # ---------- CREATE ----------
    def create(self, data: Dict[str, Any]) -> Optional[str]:
        """Insert one document and return its _id as a string (or None if empty)."""
        if not data:
            return None
        try:
            result = self.collection.insert_one(data)
            return str(result.inserted_id)
        except PyMongoError as e:
            raise RuntimeError(f"Create failed: {e}")

    # ---------- READ ----------
    def read(
        self,
        query: Optional[Dict[str, Any]] = None,
        projection: Optional[Dict[str, int]] = None,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Return a list of documents; by default I drop '_id' for Dash tables."""
        try:
            proj = projection if projection is not None else {"_id": 0}
            cur = self.collection.find(query or {}, proj)
            if limit:
                cur = cur.limit(int(limit))
            return list(cur)
        except PyMongoError as e:
            raise RuntimeError(f"Read failed: {e}")

    def read_one(
        self,
        query: Dict[str, Any],
        projection: Optional[Dict[str, int]] = None,
    ) -> Optional[Dict[str, Any]]:
        try:
            proj = projection if projection is not None else {"_id": 0}
            return self.collection.find_one(query, proj)
        except PyMongoError as e:
            raise RuntimeError(f"Read one failed: {e}")

    def read_all(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        return self.read({}, {"_id": 0}, limit=limit)

    # ---------- UPDATE ----------
    def update(
        self,
        query: Dict[str, Any],
        new_values: Dict[str, Any],
        many: bool = True,
    ) -> int:
        """Run {'$set': new_values}; return modified_count."""
        if not new_values:
            return 0
        try:
            if many:
                result = self.collection.update_many(query, {"$set": new_values})
            else:
                result = self.collection.update_one(query, {"$set": new_values})
            return int(result.modified_count)
        except PyMongoError as e:
            raise RuntimeError(f"Update failed: {e}")

    # ---------- DELETE ----------
    def delete(self, query: Dict[str, Any], many: bool = True) -> int:
        """Delete docs matching query; return deleted_count."""
        try:
            if many:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return int(result.deleted_count)
        except PyMongoError as e:
            raise RuntimeError(f"Delete failed: {e}")

    # ---------- UTILITIES ----------
    def count(self, query: Optional[Dict[str, Any]] = None) -> int:
        try:
            return int(self.collection.count_documents(query or {}))
        except PyMongoError as e:
            raise RuntimeError(f"Count failed: {e}")
