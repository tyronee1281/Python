#!/usr/bin/python3
#Base/Main file for Duplicate File Checker program

import os
import hashlib
import pandas as pd

ResFName = 'Results.csv'
ErrFName = 'Error.csv'

#=================================================================================================
def getMd5Sum(AbsFName):
  with open(AbsFName,'rb') as iFile:
    data = iFile.read()
  return hashlib.md5(data).hexdigest()

#=================================================================================================
def getAllFilesDetails(ipath):
  ResFile = open(ResFName, 'w')
  ErrFile = open(ErrFName, 'w')

  ResFile.write(','.join(['FileName', 'Location', 'FileSize']) + '\n')
  for root, dirs, files in os.walk(ipath, topdown=True, followlinks=False):
    for FileName in files:
      AbsFName = os.path.join(root,FileName)
      if (AbsFName,os.R_OK):
        ResFile.write(','.join([FileName, root, str(os.path.getsize(AbsFName))]) + '\n')
      else:
        ErrFile.write(AbsFName + ',' + 'Not Authorized')
  
  ResFile.close()
  ErrFile.close()
  
  return 0
  
#=================================================================================================
def getDuplicates(iFile,colCheck):
  df = pd.read_csv(iFile)
  dfDupRecords = df[df[[colCheck]].duplicated(keep=False)]

  for index, row in dfDupRecords.iterrows():
    print(dfDupRecords['FileName'][index], 
          dfDupRecords['Location'][index], 
          dfDupRecords['FileSize'][index], 
          getMd5Sum(os.path.join(dfDupRecords['Location'][index],dfDupRecords['FileName'][index])))
  
  return 0 

#=================================================================================================
def main():
  basepath = '/Users/tyroneestacio/git/py_repo/src/'

  getAllFilesDetails(basepath)
  getDuplicates(ResFName,'FileSize')
  getDuplicates(ResFName,'FileName')

  return 0

#=================================================================================================
if __name__ == '__main__':
  main()




