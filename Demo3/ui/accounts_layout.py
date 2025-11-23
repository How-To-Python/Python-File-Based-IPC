from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt
from rich import box


#=============================================================================
# Writer Layout Specific Components
# Used by the writer layout only
#=============================================================================

def get_new_account_details(console):
    """
    Prompt user for new account details and return as a dictionary.
    param console: Console - The Rich Console object to use for input/output
    return: dict - A dictionary containing the new account details
    """

    console.print("\n[bold green]Add New Account[/bold green]")

    account_name = Prompt.ask("Enter Account Name: ")
    account_type = Prompt.ask("Enter Account Type (e.g., Savings, Checking): ")
    initial_balance = Prompt.ask("Enter Initial Balance: ")

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


#=============================================================================
# Reader Layout Specific Components
# Used by the reader layout only
#=============================================================================

def create_account_table(accounts):
    """
    Create a Rich Table to display account information
    param accounts: list - A list of account dictionaries
    return: Table - A Rich Table object containing account information
    """
    table = Table(title="Accounts Overview", box=box.SIMPLE_HEAVY)
    table.add_column("Account Name", style="cyan", no_wrap=True)
    table.add_column("Account Type", style="magenta")
    table.add_column("Balance", justify="right", style="green")

    for account in accounts:
        table.add_row(
            account.get("name", "Unnamed"),
            account.get("type", "N/A"),
            f"${account.get('balance', 0):.2f}"
        )
    return table