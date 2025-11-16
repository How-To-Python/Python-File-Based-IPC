# ==============================================
# FILE BASED IPC DEMONSTRATION: WRITER PROCESS
# ==============================================
import json
from pathlib import Path


from rich.prompt import Prompt
from rich.console import Console

from ui.writer_layout import create_writer_layout, show_menu, get_new_account_details, get_new_transaction_details
from utils.account import get_accounts, get_account_names


console = Console()

SHARED_STATE_FILE = Path(__file__).parent / "ipc_state.json"

def read_shared_state():
    """
    Read the shared state from the JSON file.
    return: dict - The current state dictionary
    """
    try:
        with open(SHARED_STATE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Shared state file not found.")

def add_new_account():
   """
    Adds a new account to the shared state
   """
   state = read_shared_state()
   new_account_details = get_new_account_details(console)
   state["accounts"].append(new_account_details)

   with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)

def add_new_transaction():
    """
    Add a transaction to an account in the shared state
    """
    state = read_shared_state()
    accounts = get_accounts(state)
    account_names = get_account_names(accounts)

    transaction_details = get_new_transaction_details(console, account_names, state)
    account_name = transaction_details['account_name']
    amount = transaction_details['amount']
    description = transaction_details['description']

    for account in accounts:
        if account['name'] == account_name:
            account.setdefault('transactions', []).append({
                "amount": amount,
                "description": description
            })
            break

    with open(SHARED_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)

def handle_menu__choice(choice):
    """
    Handle the user's menu choice
    param choice: str - The user's menu choice
    return: int - 0 to exit, else None
    """
    match choice:
        case "0":
            console.print("\n[yellow]Exiting Command Client. Goodbye! 👋[/yellow]\n")
            return 0
        case "1":
            add_new_account()
        case "2":
            add_new_transaction()
        case "3":
            console.print("\n[yellow]Viewing Accounts! 👋[/yellow]\n")
        case "4":
            console.print("\n[yellow]Viewing Transactions! 👋[/yellow]\n")
        case "5":
            console.print("\n[yellow]Switching View! 👋[/yellow]\n")
        case "6":
            console.print("\n[yellow]Updating Content! 👋[/yellow]\n")
        case "7":
            console.print("\n[yellow]Showing Current State! 👋[/yellow]\n")
        case _:
            console.print("[red]❌Invalid choice. Please try again.[/red]")

def main():
    """
    Main function to run the writer process

    """
    create_writer_layout(console)
        # Prompt the user to ensure the reader.py is running
    console.print("[cyan]Command Client Started![/cyan]")
    console.print("[yellow]Make sure interface_server.py is running in another terminal[/yellow]\n")
    input("Press Enter to continue...")


    while True:
        
        choice = show_menu(console)
        result = handle_menu__choice(choice)

        if result == 0:
            break

        input("\nPress Enter to continue...")
     

if __name__ == "__main__":
    main()