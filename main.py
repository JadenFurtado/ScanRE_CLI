import os
import asyncio
from Scanner import CodeScanner
from dotenv import dotenv_values
from dotenv import load_dotenv

load_dotenv(".env")

art = """

█▀▀ █▀▀ █▀▀█ █▀▀▄ ░█▀▀█ ░█▀▀▀ 
▀▀█ █   █▄▄█ █  █ ░█▄▄▀ ░█▀▀▀ 
▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀ ░█ ░█ ░█▄▄▄

"""
if __name__=='__main__':
    print(art)
    scanType = os.getenv("SCAN_TYPE")
    targetsFilePath = os.getenv("TARGETS_FILE")
    targets = open(targetsFilePath,"r")
    if int(scanType) == 1:
        print("[*] Scanning repos listed in:"+targetsFilePath)
        for target in targets:
            if target is None or target == "/n":
                print("* Target was empty")
                print("* exiting")
                break
            else:
                target = target.strip()
                values = target.split("/")
                repoLink = target
                # adding sanity checks
                path = os.getenv("SCAN_PATH")
                if path is None:            
                    exit("* scan path cannot be null")
                repoName = values[4]
                if repoName is None:
                    exit("* repo name cannot be null")
                scanResultPath = os.getenv("RESULT_PATH")
                if scanResultPath is None:
                    exit("* scan result path cannot be null")
                try:
                    scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
                except:
                    print("* Error initializing scanner")
                try:
                    scanner.getCode()
                except:
                    print("* Error getting cloning the code")
                try:
                    scanner.scanCode()
                except:
                    print("* Error scanning the code")
                try:
                    scanner.generateReport()
                except:
                    print("* Error generating the report")
                try:
                    scanner.cleanUp()
                except:
                    print("Error cleaning up")
        targets.close()
    else:
        # code for scanning from folders
        targets = open(targetsFilePath)
        for folder in targets:
            if folder is None:
                print("Folder can't be None")
                break
            print("[*] Scanning code present in folder:"+folder)
            path = os.getenv("SCAN_PATH")
            if path is None:            
                exit("* scan path cannot be null")
            repoName = folder
            if repoName is None:
                exit("* repo name cannot be null")
            scanResultPath = os.getenv("RESULT_PATH")
            if scanResultPath is None:
                exit("* scan result path cannot be null")
            repoLink = " "
            scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
            scanner.scanCode()
            # try:
            #     asyncio.run(scanner.moveReport())
            # except:
            #     print("* Could not move the report")
            # try:
            #     asyncio.run(scanner.generateReport())
            # except:
            #     print("* Could not generate the report")
        targets.close()