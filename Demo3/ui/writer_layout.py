from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table
from rich import box

from ui.common_layouts import create_header, create_footer


#=============================================
# WRITER LAYOUT FUNCTIONS
#=============================================
def create_writer_layout(console):
    """
    Creates the base layout for the writer process
    param console: Console - The Rich Console object to use for output
    """

    header_text = "📝 FILE-BASED IPC WRITER STARTED 📝"
    color = "cyan"
    footer_text = "Writing to: shared_state.json | Press Ctrl+C to stop the writer process."
    console.print(create_header(header_text, color))
    console.print(create_footer(footer_text))

def update_writer_layout(console, new_message):
    """
    Update the writer's layout with a new message
    param console: Console - The Rich Console object to use for output
    param new_message: str - The new message to display in the header
    """
    console.clear()
    header_text = "📝 Writer Updated State To: " + new_message
    color = "yellow"
    console.print(create_header(header_text, color))

def create_menu():

    table = Table(title="Available Commands", box=box.SIMPLE_HEAVY)

    table.add_column("Command", style="green")
    table.add_column("Description")
    table.add_row("1", "Switch View")
    table.add_row("2", "Update Content")
    table.add_row("3", "Add New Account")
    table.add_row("4", "Add New Transaction")
    table.add_row("5", "Show Current State")
    table.add_row("0", "Exit")
    
    return table

def show_menu(console):
    menu = create_menu()

    console.print(menu)
    choice = Prompt.ask(
            "[green]Enter command[/green]",
            choices=["0", "1", "2", "3", "4", "5"]
        )
    
    return choice