from binascii import hexlify
import os


def please_create_hash():
    return random_hash


def random_hash():
    return hexlify(os.urandom(16)).decode()
