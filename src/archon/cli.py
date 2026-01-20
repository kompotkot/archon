import argparse


def version_handler(args: argparse.Namespace) -> None:
    """Version handler for displaying the version of the application."""
    print(f"0")


def cli() -> None:
    """
    Main entry point to Archon application with CLI.

    Sets up command line argument parsing and routes to appropriate handlers
    for search and utility commands.
    """
    parser = argparse.ArgumentParser(description="Archon CLI")
    parser.set_defaults(func=lambda _: parser.print_help())
    subcommands = parser.add_subparsers(description="Archon commands")

    version_parser = subcommands.add_parser(
        "version", description="Display the version of the application"
    )
    version_parser.set_defaults(func=version_handler)

    args = parser.parse_args()
    args.func(args)
