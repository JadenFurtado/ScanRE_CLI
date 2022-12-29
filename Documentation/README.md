# Documentation:

* Step 0: Install requirements.txt

Run 

```
pip install -r requirements.txt
```

## Scan code from github repositories:

* Step 1: Load the scanner configuration into .env file as shown in the .envexample

```
SCAN_TYPE = 1
SCAN_PATH = <path_to_where_you_want_the_code_cloned>
RESULT_PATH = <path_to_store_scan_result>
TARGETS_FILE = targets.txt
PATHS_FILE = paths.txt
```

* Step 2: Add the links of github repositories you would like to scan to targets.txt

* Step 3: Run main.py

## Scan code from folders:

* Step 1: Load the scanner configuration into the .env file, except set SCAN_TYPE to anything other than 1

* Step 2: Add the Paths to the folders you want to scan in SCAN_PATH

* Step 3: Add list of folders to be scanned into the targets.txt file

* Step 4: Run main.py