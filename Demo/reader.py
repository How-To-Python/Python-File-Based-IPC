# ==============================================
# FILE BASED IPC DEMONSTRATION: READER PROCESS
# ==============================================

import json # for reading JSON data
from pathlib import Path# for file path handling

#==========================================================================================================================
#TODO: Create a Constant for the shared state file path, must match the writer's path that points to shared state file
#==========================================================================================================================
    # Explanation: SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"
        # this is needed in both the reader and writer processes because they both need to access the same file
        # Path(), provides an object-oriented approach to handling file system paths
            # it will create a Path object representing the directory of the current script
        # Path(__file__), will give the full path to the current script `reader.py`:
            # ....\Python-File-Based-IPC\Demo\reader.py
            # __file__ is a special variable that holds the path of the current script
        # Path(__file__).parent, gets the directory part of the path which is, `Demo/` in this case
            # ensure it is relative to the current script's location
            # ...\Python-File-Based-IPC\Demo
        # Path(__file__).parent / "ipc_state.json", will append "ipc_state.json" to the directory path
            # ...\Python-File-Based-IPC\Demo\ipc_state.json
            # and "ipc_state.json" is the filename used for storing the shared state.
# print(f"Shared state file path: {SHARED_STATE_FILE}")
#==========================================================================================================================
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

# ipc_state.json: you do not have to create the file beforehand, the writer process will create it when it writes the first time
# but you can create an empty file manually if you want to avoid the FileNotFoundError on the first read attempt


#==========================================================================================================================
# TODO: Implement a function to initialize the reader process
#==========================================================================================================================
def initialize_reader():
    print("Reader process initialized.")
    #......Additional initialization logic 

#==========================================================================================================================
# TODO: Implement a function to read the shared state from the file and handle the case where the file does not exist yet
#   the function should:
#   try to open and read the JSON file
#   parse the JSON data into a Python dictionary
#   return the dictionary
#   if the file does not exist, it should:
#   Handle the FileNotFoundError exception
#   print a message indicating that the shared state file was not found
#   because the writer process may not have created it yet
#==========================================================================================================================
def read_shared_state():
    #==========================================================================================================================
    # `with`:
    #  is a context manager that ensures the file is properly closed after its suite finishes
    # the context manager handles opening and closing the file automatically
    # a context manager is a construct that allows for setup and teardown actions around a block of code
    # it is commonly used for resource management, such as file handling, network connections, and database connections
    # in this case, it ensures that the file is closed after reading, even if an error occurs during the read operation
    #==========================================================================================================================

    #==========================================================================================================================
    # `json.load(file)`:
    #  reads JSON data from a file object and parses it into a Python dictionary
    # it takes a file object as an argument and reads the entire content of the file
    # then it converts the JSON formatted string into a corresponding Python data structure
    #==========================================================================================================================
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")
        return {}
    

#==========================================================================================================================
# TODO: Implement a function to display the shared state
#==========================================================================================================================
def display_shared_state():
    state = read_shared_state()# state will be a dictionary
    print("Current Shared State:")
    for key, value in state.items():
        print(f"  {key}: {value}")


