from   django.http     import HttpResponse
from   django.template import loader
import pandas              as pd
import os

# Create your views here.
def index(request):
  DFDupFiles = pd.read_csv('/tmp/Results_DupContent.csv')
  lstDupFiles = []
  jsonDupFiles = {}
  template = loader.get_template('UIDupChecker/index.html')

  for index, row in DFDupFiles.iterrows():
    #lstDupFiles.append(DFDupFiles['Location'][index] + 
    lstDupFiles.append(os.path.join(DFDupFiles['Location'][index] + 
                                   DFDupFiles['FileName'][index] ))

  context = {
    "lstDupFiles": lstDupFiles,
  }

  return HttpResponse(template.render(context, request))
  #return HttpResponse('UI DupChecker Main page')

