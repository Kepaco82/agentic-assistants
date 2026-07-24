import argparse
import subprocess
import sys
from pathlib import Path

from scripts.generate_docs import main as generate_docs
from scripts.assistant_router import route_request
from scripts.assistant_orchestrator import orchestrate_request
from scripts.assistant_executor import execute_request
from scripts.llm_client import LLMClient

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

    route_parser = subparsers.add_parser(
        "route",
        help="Route a request to the best matching assistant.",
    )
    route_parser.add_argument(
        "request",
        help="The request to classify and route.",
    )

    plan_parser = subparsers.add_parser(
        "plan",
        help="Create an ordered multi-assistant execution plan.",
    )
    plan_parser.add_argument(
        "request",
        help="The request to analyze and plan.",
    )

    execute_parser = subparsers.add_parser(
        "execute",
        help="Execute a request through an LLM assistant workflow.",
    )
    execute_parser.add_argument(
        "request",
        help="The request to execute.",
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

    if args.command == "route":
        result = route_request(args.request)

        if result is None:
            print("No matching assistant found.")
            return

        print(f"Assistant: {result['assistant_id']}")
        print(f"Score: {result['score']}")
        print(f"Matched terms: {', '.join(result['matched_terms'])}")
        return

    if args.command == "plan":
        result = orchestrate_request(args.request)

        if result is None:
            print("No matching assistants found.")
            return

        print(f"Primary: {result['primary']}")
        print(f"Secondary: {', '.join(result['secondary']) or 'None'}")
        print(f"Workflow: {' -> '.join(result['workflow'])}")
        print(f"Confidence: {result['confidence']}")

        print("Reasoning:")
        for reason in result["reasoning"]:
            print(f"- {reason}")

        return
    if args.command == "execute":
        llm_client = LLMClient()

        result = execute_request(
            args.request,
            llm_client=llm_client,
        )

        if result is None:
            print("No matching assistants found.")
            return

        print(f"Workflow: {' -> '.join(result['workflow'])}")
        print()
        print(result["final_response"])
        return
        
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