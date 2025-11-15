from rich.text import Text
from rich.table import Table
from rich import box

def account_table(accounts):
    """
    Create a Rich Table to display account information
    param accounts: list - A list of account dictionaries
    return: Table - A Rich Table object containing account information
    """
    if not accounts:
        content = Text("No accounts available.", justify="center", style="white")
        return content
    else:
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


def transaction_table(transactions):
    """
    Create a Rich Table to display transaction information
    param transactions: list - A list of transaction dictionaries
    return: Table - A Rich Table object containing transaction information
    """
    if not transactions:
        content = Text("No transactions available.", justify="center", style="white")
        return content
    else:
        table = Table(title="Transactions", box=box.SIMPLE_HEAVY)
        table.add_column("Amount", justify="right", style="green")
        table.add_column("Description", style="yellow")

        for transaction in transactions:
            table.add_row(
                f"${transaction.get('amount', 0):.2f}",
                transaction.get("description", "No description")
            )
    return table