#!/usr/bin/python3
#Base/Main file for Duplicate File Checker program
import os
import hashlib

def getMd5Sum(AbsFName):
  with open(AbsFName,'rb') as file_to_check:
    data = file_to_check.read()
  return hashlib.md5(data).hexdigest()

def getAllFilesDetails(ipath):
  for root, dirs, files in os.walk(ipath, topdown=True, followlinks=False):
    for FileName in files:
      print(root, FileName, os.path.getsize(os.path.join(root,FileName)), getMd5Sum(os.path.join(root,FileName)))
  
def main():
  basepath = '/Users/tyroneestacio/git/'
  getAllFilesDetails(basepath)

if __name__ == '__main__':
  main()
