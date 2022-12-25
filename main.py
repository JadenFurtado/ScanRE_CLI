import os
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
    if int(scanType) == 1:
        print("scanning repos listed in targets.txt")
        targets = open("targets.txt","r")
        for target in targets:
            if target is None or target == "/n":
                print("Target was empty")
                print("exiting")
                break
            else:
                target = target.strip()
                values = target.split("/")
                repoLink = target
                # adding sanity checks
                path = os.getenv("SCAN_PATH")
                if path is None:            
                    exit("scan path cannot be null")
                repoName = values[4]
                if repoName is None:
                    exit("repo name cannot be null")
                scanResultPath = os.getenv("RESULT_PATH")
                if scanResultPath is None:
                    exit("scan result path cannot be null")
                print(values)
                try:
                    scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
                except:
                    print("Error initializing scanner")
                try:
                    scanner.getCode()
                except:
                    print("Error getting cloning the code")
                try:
                    scanner.scanCode()
                except:
                    print("Error scanning the code")
                try:
                    scanner.generateReport()
                except:
                    print("Error generating the report")
                try:
                    scanner.cleanUp()
                except:
                    print("Error cleaning up")
        targets.close()
    else:
        print("scanning code present in folder")
        path = os.getenv("SCAN_PATH")
        if path is None:            
            exit("scan path cannot be null")
        repoName = input("Enter the folder name")
        if repoName is None:
            exit("repo name cannot be null")
        scanResultPath = os.getenv("RESULT_PATH")
        if scanResultPath is None:
            exit("scan result path cannot be null")
        repoLink = " "
        try:
            scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
        except:
            print("Error initializing scanner")
        try:
            scanner.scanCode()
        except:
            print("Could not scan code")
        try:
           scanner.generateReport()
        except:
            print("Could not generate the report")