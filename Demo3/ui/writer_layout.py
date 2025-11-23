from rich.prompt import Prompt
from rich.table import Table
from rich import box

from ui.common_layouts import create_header, create_footer

#=============================================
# Writer Layout Functions
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


#=============================================================================
# Main Menu Functions
#=============================================================================
def create_main_menu():
    table = Table(title="[bold magenta]Available Commands[/bold magenta]", box=box.SIMPLE_HEAVY)
    table.add_column("Command", style="green")
    table.add_column("Description", style="yellow")
    table.add_row("1", "Add New Account")
    table.add_row("2", "Add New Transaction")
    table.add_row("3", "Change View")
    table.add_row("0", "Exit")
    
    return table

def show_main_menu(console):
    menu = create_main_menu()
    console.print(menu)

    choice = Prompt.ask(
            "[bold green]Enter command[/bold green]",
            choices=["0", "1", "2", "3"]
        )
    
    return choice


#=============================================================================
# View Choice Menu Functions
#=============================================================================
def create_view_choice_menu():
    table = Table(title="[bold magenta]Choose View[/bold magenta]", box=box.SIMPLE_HEAVY)
    table.add_column("Command", style="green")
    table.add_column("View", style="yellow")
    table.add_row("1", "SUMMARY")
    table.add_row("2", "ACCOUNTS")
    table.add_row("3", "TRANSACTIONS")
    return table

def show_view_choice_menu(console):
    """
    Prompt user to choose a view and return the selected view.
    param console: Console - The Rich Console object to use for input/output
    return: str - The selected view
    """

    view_menu = create_view_choice_menu()
    print("\n")
    console.print(view_menu)

    choice = Prompt.ask(
            "[bold green]Enter command[/bold green]",
            choices=["1", "2", "3"]
        )
    
    match choice:
        case "1":
            view = "SUMMARY"
        case "2":
            view = "ACCOUNTS"
        case "3":
            view = "TRANSACTIONS"

    console.print(f"\n[bold blue]Selected View: {view}[/bold blue]")
    return view