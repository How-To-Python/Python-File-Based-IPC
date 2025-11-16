"""Utility functions for account management"""
from ui.writer_layout import get_new_account_details

def add_new_account(state, console):
   """
    Adds a new account to the shared state
   """
    # Get new account details from user
   new_account_details = get_new_account_details(console)

   # Add new account to state
   state["accounts"].append(new_account_details)
   return state

def get_accounts(state):
    """
    Get the list of accounts from the shared state
    return: list - A list of account dictionaries
    """

    # Get list of accounts
    accounts = state.get("accounts", [])
    return accounts

def get_account_names(accounts):
    """
    Get a list of account names from the shared state
    return: list - A list of account names
    """

    # Get list of account names
    accounts_names = [account['name'] for account in accounts]

    return accounts_names
