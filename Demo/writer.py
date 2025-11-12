# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================

import json # for reading JSON data
from pathlib import Path# for file path handling

# Path to the shared state file - must match the reader's path
SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"