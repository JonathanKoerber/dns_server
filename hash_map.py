from collections import MutableMapping
from random import randrange

class MapBase(MutableMapping):
    '''Base class to build other maps from'''
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other
        
        def __It__(self, other):
            return self._key < other._key
        
class UnsortedTableMap(MapBase):
    '''Map using an unordered list.'''
    def __init__(self):
        self._table = []
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key ErrorL '+ repr(k))
    
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
            self._table.append(self._Item(k,v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: '+ repr(k))
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        '''Generate iteration of the map's keys'''
        for item in self._table:
            yield item._key

class HashMapBase(MapBase):
    '''Abstract bass class for map uning hash-table with MAD compression'''
    
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return  (hash(k)*self._scale+self._shift)%self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) -1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -1
    
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
    
class ChainHashMap(HashMapBase):
    '''Hash map implemented with separate chaining for collision resolution'''
    
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    '''Hash map with linear probing for collision resolution'''
    _AVAIL = object()

    def _is_avalible(self, j):
        '''True in index j in avalible'''
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j, k):
        '''Search for key k in bucket at index j'''

        firstAvail = None
        while True:
            if self._is_avalible(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
                elif k == self._table[j]._key:
                    return (True, j)
                j = (j + 1) % len(self._table)
    
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value
    
    def _bucket_setitem(self, j, k, v):
        found, s  = self._find_slot(j,k)
        if not found:
            self._table[s] = self._Item(k,v)
            self.n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL
    
    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_avalible(j):
                yield self._table[j]._key