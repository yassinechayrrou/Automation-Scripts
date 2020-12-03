#!/usr/bin/python3

import sys
import hashlib


if __name__ == "__main__":
    options = ["help", "md5", "sha1", "sha2"]

    def hashChecker(fileToCheck, hashType, mem_chunck = 1024):
        try:
            with open(sys.argv[2], 'rb') as f:
                if hashType == "md5":
                    md5 = hashlib.md5()
                    for byte_block in iter(lambda: f.read(mem_chunck), b""):
                        md5.update(byte_block)
                    return md5.hexdigest()
                elif hashType == "sha1":
                    sha1 = hashlib.sha1()
                    for byte_block in iter(lambda: f.read(mem_chunck), b""):
                        sha1.update(byte_block)
                    return sha1.hexdigest()
                elif hashType == "sha2":
                    sha2 = hashlib.sha256()
                    for byte_block in iter(lambda: f.read(mem_chunck), b""):
                        sha2.update(byte_block)
                    return sha2.hexdigest()
        except IOError:
            print("Error: file corrupt or doesn't exist")
            exit()

    try:
        if sys.argv[1]:
            if sys.argv[1] in options:
                if sys.argv[1] == options[0]:
                    print("""Simple Hash Checker:
    A tool to help you verify if file hash is identical to the one provided in checksum file
                    Usage:
                    simpleHashChecker [hash_algorithm] [file] [checksum_to_compare] [options]

                    - help : help instructions

                    - hash_algorithms : sha1 / sha2 / md5
                        + md5  : verify using md5 algorithm
                        + sha1 : verify using sha128 algorithm
                        + sha2 : verify using sha256 algorithm

                    - options :
                        +bs : specify byte chuncks to verify with hash.
                            usage : [bs=value]
                                    value list : [1024, 2048, 4096]
                        +other suggestions are welcome
                            
                    Example :
                        ./simpleHashChecker help : prints help
                        No options:
                            ./simpleHashChecker sha2 fileName 3849457405hfadlhf3937502
                        With options:
                            ./simpleHashChecker sha2 fileName 3849457405hfadlhf3937502 bs=2048""")
                else:
                    try:
                        if sys.argv[2]:
                            try:
                                if sys.argv[4]:
                                    byte_chunk = sys.argv[4].split("=")
                                    if len(byte_chunk) == 2:
                                        if byte_chunk[0] == "bs":
                                            if int(byte_chunk[1]) < 1024:
                                                print("bs: size must be greater or equal to 1024")
                                                exit()
                                            if int(byte_chunk[1]) % 1024 != 0:
                                                print("size is multiple of 1024 and less or equal to 4096")
                                                exit()
                                            chunk = int(byte_chunk[1])
                                        else:
                                            print("option {} doesn't exist".format(byte_chunk[0]))
                                    else:
                                        print("verify option format is correct")

                            except IndexError:
                                pass

                            try:
                                hash_digest = hashChecker(sys.argv[2], sys.argv[1], chunk)
                            except NameError:
                                hash_digest = hashChecker(sys.argv[2], sys.argv[1])


                    except IndexError:
                        print("Error: File is missing")
                        exit()
                    try:
                        if sys.argv[3]:
                            if hash_digest == sys.argv[3].lower():
                                print("-> generated file checksum is identical to provided")
                            else:
                                print("-> generated file checksum is Not identical Be careful to use it")
                    except IndexError:
                        print("Error: Missing hash string to check")
            else:
                print("Error: hash algorithm is not supported")

    except IndexError:
        print("""usage:
        help: shows help and description of script
        sha1 :  verify using sha128 algorithm
        sha2 : verify using sha256 algorithm
        md5 : verify using md5 algorithm
        command: simplehashchecker md5 filename/filelocation hashProvidedToVerifyWith
        example: simplehashchecker md5 myfile.iso 2a521407387e6ea3b3c26f0692ca6d5f
        """)
