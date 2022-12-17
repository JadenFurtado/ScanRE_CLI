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
            scanner = CodeScanner(repoLink,path,repoName,scanResultPath)
            scanner.getCode()
            scanner.scanCode()
            scanner.cleanUp()
    targets.close()