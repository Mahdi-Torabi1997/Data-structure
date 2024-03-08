class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def set_item(self, key, value):
        hash_key = self._hash_function(key)
        key_exists = False
        bucket = self.table[hash_key]
        if bucket is None:
            self.table[hash_key] = [(key, value)]
        else:
            for i, kv in enumerate(bucket):
                k, _ = kv
                if key == k:
                    key_exists = True
                    bucket[i] = ((key, value))
                    break
            if not key_exists:
                bucket.append((key, value))

    def get_item(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        if bucket is not None:
            for k, v in bucket:
                if key == k:
                    return v
        return None

    def delete_item(self, key):
        hash_key = self._hash_function(key)
        key_exists = False
        bucket = self.table[hash_key]
        if bucket is not None:
            for i, kv in enumerate(bucket):
                k, _ = kv
                if key == k:
                    key_exists = True
                    break
            if key_exists:
                bucket.pop(i)
