"""
Database manager with optional MySQL support.

By default the project uses a local SQLite file (DB_FILE). To use MySQL,
set `MYSQL['ENABLED'] = True` in `config.py` and provide valid credentials.

This module will create the database (for MySQL) and required tables, and
insert newsletter and batch records using the appropriate driver.
"""

import sqlite3
from config import DB_FILE, MYSQL


def _get_mysql_connection_and_ensure_db(mysql_cfg):
    try:
        import mysql.connector
    except Exception as e:
        raise ImportError("mysql-connector-python is required for MySQL support.\nInstall with: pip install mysql-connector-python") from e

    # connect without database to ensure it exists
    conn = mysql.connector.connect(
        host=mysql_cfg["HOST"],
        port=mysql_cfg.get("PORT", 3306),
        user=mysql_cfg["USER"],
        password=mysql_cfg["PASSWORD"],
    )
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{mysql_cfg['DATABASE']}`")
    conn.commit()
    cur.close()
    conn.close()

    # reconnect to the specific database
    conn = mysql.connector.connect(
        host=mysql_cfg["HOST"],
        port=mysql_cfg.get("PORT", 3306),
        user=mysql_cfg["USER"],
        password=mysql_cfg["PASSWORD"],
        database=mysql_cfg["DATABASE"],
    )
    return conn


def get_connection():
    """Return (conn, db_type) where db_type is 'mysql' or 'sqlite'."""
    if MYSQL.get("ENABLED"):
        conn = _get_mysql_connection_and_ensure_db(MYSQL)
        return conn, "mysql"
    else:
        conn = sqlite3.connect(DB_FILE)
        return conn, "sqlite"


def create_tables():
    conn, dbtype = get_connection()
    cur = conn.cursor()

    # Use common DDL which works in both SQLite and MySQL (TEXT instead of specific types)
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS newsletters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        tags TEXT,
        timestamp TEXT,
        subscriber_count INTEGER,
        status TEXT
    )
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS batches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        newsletter_title TEXT,
        batch_file TEXT
    )
    """
    )

    conn.commit()
    cur.close()
    conn.close()


def _placeholder(dbtype):
    return "%s" if dbtype == "mysql" else "?"


def save_newsletter(newsletter, count):
    conn, dbtype = get_connection()
    cur = conn.cursor()

    ph = _placeholder(dbtype)
    sql = f"INSERT INTO newsletters(title, tags, timestamp, subscriber_count, status) VALUES ({ph},{ph},{ph},{ph},{ph})"

    params = (newsletter["title"], newsletter["tags"], newsletter["timestamp"], count, "Ready to Send")

    cur.execute(sql, params)

    conn.commit()
    cur.close()
    conn.close()


def save_batch(title, batch_file):
    conn, dbtype = get_connection()
    cur = conn.cursor()

    ph = _placeholder(dbtype)
    sql = f"INSERT INTO batches(newsletter_title, batch_file) VALUES ({ph},{ph})"
    cur.execute(sql, (title, batch_file))

    conn.commit()
    cur.close()
    conn.close()