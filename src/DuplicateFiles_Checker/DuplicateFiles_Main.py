#!/usr/bin/python3
#Base/Main file for Duplicate File Checker program

import os
import hashlib
import pandas as pd

ResFName = '/tmp/Results.csv'
ResDupFName = '/tmp/Results_DupName.csv'
ResDupFSize = '/tmp/Results_DupSize.csv'
ErrFName = '/tmp/Error.csv'

#=================================================================================================
def getMd5Sum(AbsFName):
  with open(AbsFName,'rb') as iFile:
    data = iFile.read()
  return hashlib.md5(data).hexdigest()

#=================================================================================================
def getInitialFileDetails(ipath):
  ResFile = open(ResFName, 'w')
  ErrFile = open(ErrFName, 'w')

  ResFile.write(','.join(['FileName', 'Location', 'FileSize']) + '\n')
  for root, dirs, files in os.walk(ipath, topdown=True, followlinks=False):
    for FileName in files:
      if (FileName == ResFName):
        pass
      else:
        AbsFName = os.path.join(root,FileName)
        if (AbsFName,os.R_OK):
          ResFile.write(','.join([FileName, root, str(os.path.getsize(AbsFName))]) + '\n')
        else:
          ErrFile.write(AbsFName + ',' + 'Not Authorized')
  
  ResFile.close()
  ErrFile.close()
  
  return 0
  
#=================================================================================================
def getInitialDups(iFile,colCheck):
  df = pd.read_csv(iFile)
  dfDupRecords = df[df[[colCheck]].duplicated(keep=False)]

  if (len(dfDupRecords) > 0):
    OutDup = open('/tmp/Dup'+ colCheck + '.csv', 'w')
    OutDup.write('FileName,Location,FileSize,md5Sum\n')
    for index, row in dfDupRecords.iterrows():
      OutDup.write(str(dfDupRecords['FileName'][index]) + ',' +
                   str(dfDupRecords['Location'][index]) + ',' +
                   str(dfDupRecords['FileSize'][index]) + ',' +
                   str(getMd5Sum(os.path.join(dfDupRecords['Location'][index],dfDupRecords['FileName'][index]))) + '\n')
    OutDup.close()
  
  return 0 

#=================================================================================================
def getDuplicateContents(iFile):
  df = pd.read_csv(iFile)
  dfDupRecords = df[df[['md5Sum']].duplicated(keep=False)]
  if (len(dfDupRecords) > 0):
    ContentDup = open('/tmp/DupContent.csv','w')
    ContentDup.write('FileName,Location,FileSize,md5Sum\n')
    for index, row in dfDupRecords.iterrows():
      ContentDup.write(str(dfDupRecords['FileName'][index]) + ',' +
                   str(dfDupRecords['Location'][index]) + ',' +
                   str(dfDupRecords['FileSize'][index]) + ',' +
                   str(getMd5Sum(os.path.join(dfDupRecords['Location'][index],dfDupRecords['FileName'][index]))) + '\n')
      #ContentDup.write(dfDupRecords[index])
  
    ContentDup.close()
  return 0

#=================================================================================================
def main():
  basepath = '/Users/tyroneestacio/git/py_repo/src/'

  getInitialFileDetails(basepath)
  getInitialDups(ResFName,'FileSize')
  getInitialDups(ResFName,'FileName')
  getDuplicateContents('/tmp/DupFileSize.csv')
  return 0

#=================================================================================================
if __name__ == '__main__':
  main()

