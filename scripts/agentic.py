import argparse
import subprocess
import sys
from pathlib import Path


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

    args = parser.parse_args()

    if args.command == "list":
        raise SystemExit(run_script("list_assistants.py"))

    if args.command == "validate":
        raise SystemExit(run_script("validate.py"))

    if args.command == "create":
        raise SystemExit(
            run_script("create_assistant.py", [args.name])
        )

    if args.command == "show":
        raise SystemExit(
            run_script("show_assistant.py", [args.name])
        )

    parser.print_help()


if __name__ == "__main__":
    main()