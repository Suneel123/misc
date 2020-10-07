"""Decrypt stash (.sth) file

IBM HTTP Server (IHS) uses cms keystore.
When keystore of type cms is created using ikeyman tool, it generates 4 files

1. *.kdb: contains the private keys, certificates and CA's. It is encrypted
          with a password that can be stashed in the *.sth file.
2. *.rdb: contains information about outstanding certificate requests. It's
          critical that you maintain this 1:1 with KDB.
3. *.crl: contains revocation info. It is generally not interesting, unless it
          gets corrupted/mismatched in which case it can cause runtime errors.
4. *.sth: is a way to store obfuscated password to a file. Runtime tools can
          use this password instead of prompting for one interactively. It
          obviously has to be protected if you have private keys in the
          corresponding KDB.

You should treat all these files as a single atomic set of files and never copy
a subset. You always reference *.kdb from configuration or with the certificate
management tools.

The set of 4 files all put together is similar to PKCS12 file in other tools.
"""

from pathlib import Path


STASH_FILE = Path() / "tmp.sth"


if __name__ == "__main__":
    with open(STASH_FILE, "rb") as stream:
        line = stream.readline()
        xbytes = bytearray(c ^ 0xf5 for c in line)
        print(xbytes[:xbytes.index(0x00)].decode())
