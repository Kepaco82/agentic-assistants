import argparse
import subprocess
import sys
from pathlib import Path

from scripts.generate_docs import main as generate_docs

SCRIPTS_DIR = Path(__file__).parent


def run_script(script_name: str, args: list[str] | None = None) -> int:
    command = [sys.executable, str(SCRIPTS_DIR / script_name)]

    if args:
        command.extend(args)

    result = subprocess.run(command)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        prog="agentic",
        description="Agentic Assistants command-line interface.",
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "list",
        help="List available assistants.",
    )

    subparsers.add_parser(
        "validate",
        help="Validate canonical assistants.",
    )

    subparsers.add_parser(
        "docs",
        help="Generate Markdown documentation for all assistants.",
    )

    create_parser = subparsers.add_parser(
        "create",
        help="Create a new assistant.",
    )
    create_parser.add_argument(
        "name",
        help="Assistant folder name, such as customer-success.",
    )

    show_parser = subparsers.add_parser(
        "show",
        help="Show metadata for one assistant.",
    )
    show_parser.add_argument(
        "name",
        help="Assistant folder name, such as executive.",
    )

    search_parser = subparsers.add_parser(
        "search",
        help="Search assistants by keyword.",
    )
    search_parser.add_argument(
        "query",
        help="Keyword to match against assistant metadata.",
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Assemble an assistant into one complete prompt.",
    )
    run_parser.add_argument(
        "name",
        help="Assistant folder name, such as executive.",
    )

    export_parser = subparsers.add_parser(
        "export",
        help="Export an assistant prompt to the build folder.",
    )
    export_parser.add_argument(
        "name",
        help="Assistant folder name, such as executive.",
    )

    args = parser.parse_args()

    if args.command == "list":
        raise SystemExit(
            run_script("list_assistants.py")
        )

    if args.command == "validate":
        raise SystemExit(
            run_script("validate.py")
        )

    if args.command == "docs":
        generate_docs()
        return

    if args.command == "create":
        raise SystemExit(
            run_script("create_assistant.py", [args.name])
        )

    if args.command == "show":
        raise SystemExit(
            run_script("show_assistant.py", [args.name])
        )

    if args.command == "search":
        raise SystemExit(
            run_script("search_assistants.py", [args.query])
        )

    if args.command == "run":
        raise SystemExit(
            run_script("run_assistant.py", [args.name])
        )

    if args.command == "export":
        raise SystemExit(
            run_script("export_assistant.py", [args.name])
        )

    parser.print_help()


if __name__ == "__main__":
    main()