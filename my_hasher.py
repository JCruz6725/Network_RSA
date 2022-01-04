import hashlib

def md5_hasher (text):
    """ returns a string of a 128bit hash in md5 """

    md5_hash = hashlib.md5(text.encode())
    hash_data = md5_hash.hexdigest()
    return hash_data
