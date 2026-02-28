from __future__ import annotations

import os
from typing import Union

from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SASession, sessionmaker

load_dotenv()


def _build_sql_url(db_type: str) -> str:
    """Build a SQLAlchemy URL for MySQL or PostgreSQL."""
    user = os.getenv("DB_USER", "")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME", "")

    if not db_name:
        raise ValueError("DB_NAME environment variable must be set")

    if db_type == "mysql":
        driver = "mysql+pymysql"
        port = port or "3306"
    elif db_type == "postgres":
        driver = "postgresql+psycopg2"
        port = port or "5432"
    else:
        raise ValueError(f"Unsupported SQL DB_TYPE: {db_type!r}")

    return f"{driver}://{user}:{password}@{host}:{port}/{db_name}"


def _build_mongo_uri() -> str:
    """Return a MongoDB URI using authSource=admin."""
    user = os.getenv("DB_USER", "")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "27017")
    db_name = os.getenv("DB_NAME", "")

    if not db_name:
        raise ValueError("DB_NAME environment variable must be set")

    return (
        f"mongodb://{user}:{password}@{host}:{port}/{db_name}"
        "?authSource=admin"
    )


def get_client() -> Union[SASession, MongoClient]:
    """Return a DB client based on DB_TYPE.

    For 'mysql' or 'postgres' returns a SQLAlchemy Session instance.
    For 'mongodb' returns a pymongo.MongoClient.
    """
    db_type = os.getenv("DB_TYPE", "mysql").lower()

    if db_type in {"mysql", "postgres"}:
        url = _build_sql_url(db_type)
        engine = create_engine(url)
        session_local = sessionmaker(bind=engine)
        return session_local()

    if db_type == "mongodb":
        uri = _build_mongo_uri()
        return MongoClient(uri)

    raise ValueError(f"Unsupported DB_TYPE: {db_type!r}")