
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich import box

def create_header():
    """Create the header section"""
    header_text = Text("🔄 FILE-BASED IPC READER STARTED 🔄", style="bold magenta", justify="center")
    return Panel(header_text, box=box.DOUBLE, border_style="magenta")

def create_footer():
    """Create the footer section"""
    footer_text = Text(
        "Monitoring: shared_state.json| Use writer.py to send commands | Press Ctrl+C to stop the reader process",
        style="dim cyan",
        justify="center"
    )
    return Panel(footer_text, box=box.SIMPLE, border_style="dim")



def create_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )
    return layout


def update_layout(layout):
    # .update() method can be used to refresh or change layout components
    # it comes from rich library's Layout class
    layout["header"].update(create_header())
    layout["footer"].update(create_footer())


def display_layout(console):
    layout = create_layout()
    update_layout(layout)
    return console.print(layout)