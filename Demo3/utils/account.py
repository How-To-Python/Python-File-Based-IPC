"""Utility functions for account management"""
from ui.writer_layout import get_new_account_details

def add_new_account(state, console):
   """
    Adds a new account to the shared state
    param state: dict - The current shared state
    param console: Console - The Rich Console object to use for input/output
    return: dict - The updated shared state with the new account added
   """
   new_account_details = get_new_account_details(console)
   state["accounts"].append(new_account_details)
   return state

