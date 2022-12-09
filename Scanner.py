import subprocess
import os
import asyncio
import json 

# common scanner class for scanning repositories
class CodeScanner:
    def __init__(self,repoLink,path,repoName,scanResultPath):
        self.repoLink=repoLink
        self.path=path
        self.repoName = repoName
        self.scanResultPath = scanResultPath
    
    # clone code from source repository
    async def getCode(self):
        try:
            os.system('git clone '+self.repoLink+" "+self.path+"/"+self.repoName+"/")
            return "success"
        except:
            print("error")
            return "failed"

    # scan code using semgrep
    async def scanCode(self):
        try:
            os.system('docker run --rm -v "'+self.path+'/'+self.repoName+':/src" returntocorp/semgrep semgrep --config=auto --output='+self.repoName+'.json --json --verbose')
            os.system('mv '+self.path+'/'+self.repoName+'/output.json '+self.scanResultPath+'/'+self.repoName+'.json')
            return "success"
        except:
            print("error")
            return "failed"

    # delete the code to conserve memory
    async def cleanUp(self):
        try:
            os.system('rm -rf '+self.path+'/'+self.repoName+'/*')
            os.system('rm -rf '+self.path+'/'+self.repoName+'/.git')
            os.system('rmdir '+self.path+'/'+self.repoName)
            print("success")
            return "success"
        except:
            return "failed"

