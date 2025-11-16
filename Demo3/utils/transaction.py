from utils.account import get_accounts

def subtract_from_balance(account_name, amount, state):
   """
   Subtract the transaction amount from the account balance
   param account_name: str - The name of the account
   param amount: float - The transaction amount
   param state: dict - The current state dictionary
   """

   accounts = get_accounts(state)
   for account in accounts:
       if account['name'] == account_name:
           account['balance'] -= amount
           break

def get_transactions(account):
    """
    Get the list of transactions for a given account
    param account: dict - The account dictionary
    return: list - A list of transaction dictionaries
    """
    transactions = account.get("transactions", [])
    return transactions