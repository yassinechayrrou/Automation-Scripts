# Automation-Scripts

This repository presents a different programs and scripts for automation
I usually will code something i feel might be useful for me
A list of each tool or software will be included in this readme with its purpose and problems

# Tools:

### 1- SimpleHashChecker

This is a python script for the purpose of comparing checksum hash file provided by a file owner to the actual file checksum.
Instead of just generating a hash to your file then comparing it letter by letter just use this script.
it is so simple to use the script just put the hash type (sha1/sha2/md5...) fileName/Location and the hash string you want to compare it with and then you get your result.

Note: the default reading mode of file is 1024M -- i will provide a better solution for controlling size of block to generate the hash from, this is just for now HOPEFULLY!!

Features To add:
- mods flag to specify memory byte chunks to read when generating a hash, this is good in case for having a low memory where the script will fail if the file size is bigger then actual memory
- add pgp method to check if file is identical or not currently i only set md5, sha256 and sha1

**Usage**
```
chmod +x simpleHashChecker
./simpleHashChecker md5 fileName md5hashtocompare
```
**help**
```
./simpleHashChecker help
```
