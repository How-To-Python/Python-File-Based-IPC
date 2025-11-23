from rich.text import Text
from rich.table import Table
from rich import box
from rich.prompt import Prompt


#=============================================================================
# Writer Layout Specific Components
# Used by the writer layout only
#=============================================================================

def get_new_transaction_details(account_names, console):
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


#=============================================================================
# Reader Layout Specific Components
# Used by the reader layout only
#=============================================================================

def create_transaction_table(accounts):
    """
    Create a Rich Table to display transaction information
    param transactions_with_account_names: list - List of transactions with account names
    return: Table - A Rich Table object containing the transaction data
    """
    table = Table(title="Transactions Overview", box=box.SIMPLE_HEAVY)

    table.add_column("Account Name", style="cyan", no_wrap=True)
    table.add_column("Amount", style="red")
    table.add_column("Description", style="green")

    transactions_with_account_names = [
    {**trans, "account_name": account.get("name", "Unknown")}
    for account in accounts
    for trans in account.get("transactions", [])
]

    for transaction in transactions_with_account_names:
        account_name = transaction.get("account_name", "Unknown")
        amount = f"${transaction.get("amount", 0.00):.2f}"
        description = transaction.get("description", "")

        table.add_row(account_name, amount, description)

    return table
