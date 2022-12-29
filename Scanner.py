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
            self.repoLink = repoLink
        if path is None:
            print("scan path cannot be none")
        else:
            # remove new line from the string
            path = path.strip()
            self.path = path
        if repoName is None:
            print("repo name cannot be none")
        else:
            # remove new lines from the string
            repoName = repoName.strip()
            self.repoName = repoName
        if scanResultPath is None:
            print("scan result path cannot be none")
        else:
            self.scanResultPath = scanResultPath
        # self.scanCode()
        # self.generateReport()
    # clone code from source repository
    async def getCode(self):
        try:
            await os.system('git clone '+self.repoLink+" "+self.path+"/"+self.repoName+"/ --depth 1")
            return "success"
        except:
            print("error")
            return "failed"

    # scan code using SemGrep
    def scanCode(self):
        try:
            #p = os.system('docker run --rm -v "'+self.path+'/'+self.repoName+':/src" returntocorp/semgrep semgrep --config=auto --output=output.json --json --verbose --max-target-bytes 15MB')
            command = 'docker run --rm -v "'+self.path+'/'+self.repoName+':/src" returntocorp/semgrep semgrep --config=auto --output=output.json --json --verbose --max-target-bytes 15MB'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            process.wait()
            return "success"
        except:
            print("error")
            return "failed"
    # move the generated file
    async def moveReport(self):
        try:
            await os.system('mv '+self.path+'/'+self.repoName+'/output.json '+self.scanResultPath+'/'+self.repoName+'.json')
            return "success"
        except:
            print("error")
            return "failed"

    # generate HTML report
    async def generateReport(self):
        f = open(str(self.scanResultPath+'/'+self.repoName+'.json'))
        data = json.loads(f.read())
        output = json2html.convert(json = data)
        file = open(self.scanResultPath+'/'+self.repoName+'.html',"w")
        await file.write(output)
        file.close()

    # delete the code to conserve memory
    def cleanUp(self):
        try:
            os.system('rm -rf '+self.path+'/'+self.repoName)
            print("success")
            return "success"
        except:
            return "failed"