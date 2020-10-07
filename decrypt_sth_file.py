# Decrypt stash (.sth) file
from pathlib import Path


STASH_FILE = Path() / "tmp.sth"


if __name__ == "__main__":
    with open(STASH_FILE, "rb") as stream:
        line = stream.readline()
        xbytes = bytearray(c ^ 0xf5 for c in line)
        print(xbytes[:xbytes.index(0x00)].decode())
