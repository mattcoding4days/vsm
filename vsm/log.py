import rich

class Log:
    """
    A convience wrapper class for formatted colorized output
    """

    def info(msg: str):
        """
        Log a green highlighted info msg
        """
        rich.print(f"[bold green][✓][/bold green] {msg}")

    def warn(msg: str):
        """
        Log a yellow highlighted warning message
        """
        rich.print(f"[bold yellow][!][/bold yellow] {msg}")

    def error(msg: str):
        """
        Log an error message then exit the program
        """
        rich.print(f"[bold red][X][/bold red] {msg}")
