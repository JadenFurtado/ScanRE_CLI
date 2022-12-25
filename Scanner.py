import subprocess
import os
import asyncio
import json 
from json2html import *

# common scanner class for scanning repositories
class CodeScanner:
    def __init__(self,repoLink,path,repoName,scanResultPath):
        # Adding checks to variables
        if repoLink is None:
            print("repoLink cannot be none")
        else:
            self.repoLink=repoLink
        if path is None:
            print("scan path cannot be none")
        else:
            self.path=path
        if repoName is None:
            print("repo name cannot be none")
        else:
            self.repoName = repoName
        if scanResultPath is None:
            print("scan result path cannot be none")
        else:
            self.scanResultPath = scanResultPath
    
    # clone code from source repository
    def getCode(self):
        try:
            os.system('git clone '+self.repoLink+" "+self.path+"/"+self.repoName+"/")
            return "success"
        except:
            print("error")
            return "failed"

    # scan code using SemGrep
    def scanCode(self):
        try:
            os.system('docker run --rm -v "'+self.path+'/'+self.repoName+':/src" returntocorp/semgrep semgrep --config=auto --output=output.json --json --verbose --max-target-bytes 15MB')
            os.system('mv '+self.path+'/'+self.repoName+'/output.json '+self.scanResultPath+'/'+self.repoName+'.json')
            return "success"
        except:
            print("error")
            return "failed"
    
    # generate HTML report
    def generateReport(self):
        f = open(str(self.scanResultPath+'/'+self.repoName+'.json'))
        data = json.loads(f.read())
        output = json2html.convert(json = data)
        file = open(self.scanResultPath+'/'+self.repoName+'.html',"w")
        file.write(output)
        file.close()

    # delete the code to conserve memory
    def cleanUp(self):
        try:
            os.system('rm -rf '+self.path+'/'+self.repoName)
            print("success")
            return "success"
        except:
            return "failed"