#!/usr/bin/python3

import sys
import hashlib


if __name__ == "__main__":
    options = ["help", "md5", "sha1", "sha2"]

    def hashChecker(fileToCheck, hashType):
        try:
            with open(sys.argv[2], 'rb') as f:
                if hashType == "md5":
                    md5 = hashlib.md5()
                    for byte_block in iter(lambda: f.read(1024), b""):
                        md5.update(byte_block)
                    return md5.hexdigest()
                elif hashType == "sha1":
                    sha1 = hashlib.sha1()
                    for byte_block in iter(lambda: f.read(1024), b""):
                        sha1.update(byte_block)
                    return sha1.hexdigest()
                elif hashType == "sha2":
                    sha2 = hashlib.sha256()
                    for byte_block in iter(lambda: f.read(1024), b""):
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
                    help : shows the help manual
                    sha1 :  verify using sha128 algorithm
                    sha2 : verify using sha256 algorithm
                    md5 : verify using md5 algorithm
                    Other encryption might be added soon such as pgp

                    Second argument contain your file / file location
                    Third argument contains the checksum hash provided by file owner
                    Example :
                              ./simpleHashChecker md5 fileName 3849457405hfadlhf3937502
                              Result -> Identical Or Not Identical""")
                else:
                    try:
                        if sys.argv[2]:
                            hash_digest = hashChecker(sys.argv[2], sys.argv[1])
                    except IndexError:
                        print("Error: File is missing")
                        exit()
                    try:
                        if sys.argv[3]:
                            if hash_digest == sys.argv[3]:
                                print("-> generated file checksum is identical to provided")
                            else:
                                print("-> generated file checksum is Not identical Be careful to use it")
                    except IndexError:
                        print("Error: Missing hash string to check")
            else:
                print("Algorithm is not supported")

    except IndexError:
        print("""usage:
        help: shows help and description of script
        sha1 :  verify using sha128 algorithm
        sha2 : verify using sha256 algorithm
        md5 : verify using md5 algorithm
        command: simplehashchecker md5 filename/filelocation hashProvidedToVerifyWith 
        example: simplehashchecker md5 myfile.iso 2a521407387e6ea3b3c26f0692ca6d5f
        """)
