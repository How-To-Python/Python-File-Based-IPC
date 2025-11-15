from rich.prompt import Prompt

def create_new_account(console):
   """  
   Prompt user for new account details and return as a dictionary.
   param console: Console - The Rich Console object to use for input/output
   return: dict - A dictionary containing the new account details

   """
   console.print("\n[bold green]Add New Account[/bold green]")
    
   account_name = console.input("Enter Account Name: ")
   account_type = console.input("Enter Account Type (e.g., Savings, Checking): ")
   initial_balance = console.input("Enter Initial Balance: ")

   try:
        initial_balance = float(initial_balance)
   except ValueError:
        console.print("[red]Invalid balance amount. Please enter a numeric value.[/red]")
        return

       # Add new account to state
   new_account_details = {
        "name": account_name,
        "type": account_type,
        "balance": initial_balance
    }
    
   console.print(f"[bold green]Account '{account_name}' added successfully![/bold green]\n")
   return new_account_details

    
def get_accounts(state):
    """
    Get the list of accounts from the shared state
    return: list - A list of account dictionaries
    """
    accounts = state.get("accounts", [])
    return accounts

def get_account_names(accounts):
    """
    Get a list of account names from the shared state
    return: list - A list of account names
    """
    accounts_names = [account['name'] for account in accounts]

    return accounts_names


def get_new_transaction_details(console, account_names):
    """
    Prompt user for new transaction details and return as a dictionary.
    param console: Console - The Rich Console object to use for input/output
    param account_names: list - A list of account names to choose from
    return: dict - A dictionary containing the new transaction details
    """
    console.print("\n[bold green]Add Transaction[/bold green]")
    account_name = Prompt.ask("Select Account", choices=account_names)
    amount = float(Prompt.ask("Enter Amount"))
    description = Prompt.ask("Enter Description")

    transaction_details = {
        "account_name": account_name,
        "amount": amount,
        "description": description
    }

    console.print(f"[bold green]Transaction added to account '{account_name}' successfully![/bold green]\n")
    return transaction_details