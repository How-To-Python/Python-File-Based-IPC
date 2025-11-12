# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================

import json # for reading JSON data
from pathlib import Path# for file path handling

# Path to the shared state file - must match the reader's path
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"


#==========================================================================================================================
# TODO: Implement a function to read the shared state from the file
#==========================================================================================================================
def read_shared_state():
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")
        return {}