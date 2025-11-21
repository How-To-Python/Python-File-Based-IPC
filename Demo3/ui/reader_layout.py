from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich import box
from rich.columns import Columns

from ui.common_layouts import create_header, create_footer
from ui.accounts_layout import create_account_table
from ui.transactions_layout import create_transaction_table
from utils.transaction import get_all_transactions
#=============================================
# READER LAYOUT FUNCTIONS
#=============================================

def create_reader_layout():
    """
    Creates the base layout for the reader process
    return: Layout - A Rich Layout object with header, body, and footer sections
    """

    # create the main layout
    layout = Layout()

    #split the layout into header, body, and footer
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", size=16),
        Layout(name="footer", size=3)
    )

    header_text = "💸  BUDGET TRACKER CLI 💸"
    color = "magenta"
    footer_text = "Monitoring: shared_state.json | Use writer.py to send commands | Press Ctrl+C to stop the reader process"

    # .update() method can be used to refresh or change layout components
    # it comes from rich library's Layout class
    layout["header"].update(create_header(header_text, color))
    layout["footer"].update(create_footer(footer_text))

    return layout

def show_current_view(state, layout):
    """
    Update the reader's body based on the current view in state
    param state: dict - The current state dictionary
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    current_view = state.get("current_view", "SUMMARY")
    if current_view == "SUMMARY":
        return summary_view_panel(state, layout)
    elif current_view == "ACCOUNTS":
        return account_view_panel(state, layout)
    elif current_view == "TRANSACTIONS":
        return transaction_view_panel(state, layout)
    else:
        return layout

def summary_view_panel(state, layout):
    """
    Update the reader's body with summary view content based on the current state
    param state: dict - The current state dictionary
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    # get the current view from state to display in the title
    current_view = state.get("current_view", None)

    # get all accounts from state to access each account and their transactions
    accounts = state.get("accounts", [])

    # account table with all accounts
    all_accounts_table = create_account_table(accounts)

    # # transaction table with all transactions from all accounts
    # transactions = [trans for account in accounts for trans in account.get("transactions", [])]
    transactions_table = get_all_transactions(accounts, create_transaction_table)

    # add both tables side by side in a columns panel
    tables_panel = Columns([all_accounts_table, transactions_table])
    body = Panel(
        Align.center(tables_panel, vertical="middle"),
        title=current_view,
        border_style="green",
        box=box.ROUNDED
    )
    return layout["body"].update(body)

# this gets all transactions from all accounts along with the account name they belong to
def transaction_view_panel(state, layout):
    """
    Update the reader's body with summary view content based on the current state
    param state: dict - The current state dictionary
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """
    current_view = state.get("current_view", None)

    accounts = state.get("accounts", [])

    transactions_table = get_all_transactions(accounts, create_transaction_table)
    
    body = Panel(
        Align.center(transactions_table, vertical="middle"),
        title=current_view,
        border_style="green",
        box=box.ROUNDED
    )
    return layout["body"].update(body)

def account_view_panel(state, layout):
    """
    Update the reader's body with summary view content based on the current state
    param state: dict - The current state dictionary
    param layout: Layout - The Rich Layout object to update
    return: layout - The updated Rich Layout object
    """

    current_view = state.get("current_view", None)
    accounts = state.get("accounts", [])
    all_accounts_table = create_account_table(accounts)
    tables_panel = Columns([all_accounts_table])
    body = Panel(
        Align.center(tables_panel, vertical="middle"),
        title=current_view,
        border_style="green",
        box=box.ROUNDED
    )
    return layout["body"].update(body)
