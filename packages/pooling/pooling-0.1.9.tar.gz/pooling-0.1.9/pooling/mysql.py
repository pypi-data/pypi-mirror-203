#!/usr/bin/env python
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

__all__ = [
    "MysqlConnectionPoolBase",
    "MysqlclientConnectionPool",
    "MysqlConnectorPool",
    "MysqlConnectionPool",
]

import time
import logging

from zenutils import importutils

from .base import PoolBase


_logger = logging.getLogger(__name__)


class MysqlConnectionPoolBase(PoolBase):
    MAX_RECONNECT_SLEEP_TIME = 5
    RECONNECT_SLEEP_TIME_DELTA = 0.1

    def do_session_create(self, *args, **kwargs):
        raise NotImplementedError()

    def do_session_destory(self, real_session):
        try:
            real_session.close()
        except Exception as error:
            _logger.exception("MysqlConnectionPool.do_session_destory calling real_session.close() failed: error={error}...".format(error=error))
    
    def get_cursor(self, conn):
        return conn.cursor()

    def get_session(self, timeout=None):
        last_error = Exception("Too short time to get a connection...")
        stime = time.time()
        sleep_time = 0.0
        while True:
            ntime = time.time()
            if timeout:
                if ntime - stime > timeout:
                    break
            session = None
            try:
                session = PoolBase.get_session(self, timeout=timeout)
            except Exception as error:
                _logger.exception("MysqlConnectionPool.get_session calling PoolBase.get_session() failed: error={error}...".format(error=error))
                last_error = error
            if session:
                try:
                    session.ping()
                except Exception as error:
                    _logger.exception("MysqlConnectionPool.get_session calling session.ping() failed: error={error}...".format(error=error))
                    last_error = error
                    session._pooling_destory_session()
                    session = None
            if not session:
                sleep_time = self.get_session_sleep(sleep_time)
                if sleep_time:
                    time.sleep(sleep_time)
            else:
                return session
        raise last_error

    def get_session_sleep(self, sleep_time):
        sleep_time += self.RECONNECT_SLEEP_TIME_DELTA
        if sleep_time >= self.MAX_RECONNECT_SLEEP_TIME:
            sleep_time = 0.0
        return sleep_time

    def query(self, *args, **kwargs):
        """Execute a SELECT SQL and get all the results.

        @Results: result_table
        """
        timeout = None
        if "timeout" in kwargs:
            timeout = kwargs.pop("timeout")
        session = self.get_session(timeout)
        cursor = session.cursor()
        cursor.execute(*args, **kwargs)
        return cursor.fetchall()

    def execute(self, *args, **kwargs):
        """Execute an INSERT or UPDATE or DELETE SQL and get the lastrowid or the number of rows effected.

        @Results: tuple([int, int])
        """
        timeout = None
        if "timeout" in kwargs:
            timeout = kwargs.pop("timeout")
        session = self.get_session(timeout)
        cursor = self.get_cursor(session)
        cursor.execute(*args, **kwargs)
        return cursor.lastrowid, cursor.rowcount

    def executemany(self, *args, **kwargs):
        """Execute INSERTs or UPDATEs or DELETEs in batch mode and returns the number of rows effected.

        @Results: int
        """
        timeout = None
        if "timeout" in kwargs:
            timeout = kwargs.pop("timeout")
        session = self.get_session(timeout)
        cursor = self.get_cursor(session)
        cursor.executemany(*args, **kwargs)
        return cursor.rowcount

    def callproc(self, *args, **kwargs):
        """Calling mysql procedue.
        """
        timeout = None
        if "timeout" in kwargs:
            timeout = kwargs.pop("timeout")
        session = self.get_session(timeout)
        cursor = self.get_cursor(session)
        return cursor.callproc(*args, **kwargs)


class MysqlclientConnectionPool(MysqlConnectionPoolBase):
    """Mysql connection pool using `mysqlclient` adaptor.
    """

    def do_session_create(self, *args, **kwargs):
        import MySQLdb
        from MySQLdb.cursors import DictCursor
        if "cursorclass" in kwargs:
            cursorclass = kwargs.pop("kwargs")
            if isinstance(cursorclass, str):
                cursorclass = importutils.import_from_string(cursorclass)
        else:
            cursorclass = DictCursor
        kwargs.setdefault("cursorclass", cursorclass)
        kwargs.setdefault("autocommit", True)
        kwargs.setdefault("charset", "utf8mb4")
        if "collation" in kwargs:
            del kwargs["collation"]
        return MySQLdb.connect(*args, **kwargs)


class MysqlConnectorPool(MysqlConnectionPoolBase):
    """Mysql connection pool using `mysql-connection-python` adaptor.

    Default settings:
        autocommit: True,
        charset: "utf8mb4",
        collation: "utf8mb4_unicode_ci",
    """

    def do_session_create(self, *args, **kwargs):
        import mysql.connector
        kwargs.setdefault("autocommit", True)
        kwargs.setdefault("charset", "utf8mb4")
        kwargs.setdefault("collation", "utf8mb4_unicode_ci")
        return mysql.connector.connect(*args, **kwargs)

    def get_cursor(self, conn):
        return conn.cursor(dictionary=True, buffered=True)

class PyMySQLConnectionPool(MysqlConnectionPoolBase):
    """Mysql connection pool using `pymysql` adaptor.

    Default settings:
        cursorclass: pymysql.cursors.DictCursor
    """

    def do_session_create(self, *args, **kwargs):
        import pymysql
        import pymysql.cursors
        kwargs.setdefault("cursorclass", pymysql.cursors.DictCursor)
        if "collation" in kwargs:
            del kwargs["collation"]
        connection = pymysql.connect(*args, **kwargs)
        return connection

MysqlConnectionPool = MysqlclientConnectionPool # by default we use mysqlclient adaptor
