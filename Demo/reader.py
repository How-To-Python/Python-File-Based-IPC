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
