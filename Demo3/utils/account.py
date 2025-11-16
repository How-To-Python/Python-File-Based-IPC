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
