import os
from Scanner import CodeScanner

if __name__=='__main__':
    targets = open("targets.txt","r")
    for target in targets:
        target = target.strip()
        values = target.split("/")
        repoLink = target
        path = os.getenv("SCAN_PATH")
        repoName = values[4]
        scanResultPath = os.getenv("RESULT_PATH")
        print(values)
        scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
        scanner.getCode()
        scanner.scanCode()
        scanner.cleanUp()
    targets.close()