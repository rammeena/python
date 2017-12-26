from pycassa import *

class KeyspaceProxy(object):
    def __init__(self, keyspace, connection_pool):
        self.keyspace = keyspace
        self.connection_pool = connection_pool

    def __getitem__(self):
        return ColumnFamilyProxy(self._pool, cf)


class ColumnFamilyProxy:
    def __init__(self, pool, cf_name):
        self._cf = ColumnFamily(pool, cf_name)

    def __getitem__(self, rowkey):
        return RowProxy(self._cf, rowkey)

class RowProxy():
    def __init__(self, column_family, rowkey):
        self._cf = column_family
        self._rowkey = rowkey

    def __getitem__(self, column_name):
        row = self._cf.get(self._rowkey, [column_name])
        return row[column_name]

    def __setitem__(self, column_name, value):
        self._cf.insert(self._rowkey,{column_name: value})

