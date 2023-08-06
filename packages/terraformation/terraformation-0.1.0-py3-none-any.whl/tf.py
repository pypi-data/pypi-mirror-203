#!/usr/bin/env python3
"""A simple Terraform wrapper to use variable definition files if they match
the workspace name."""

import glob
import os
import pathlib
import subprocess  # nosec
import sys

__version__ = "0.1.0"

TF_COMMANDS_TO_MODIFY = ["plan", "console", "import", "refresh"]


def get_workspace():
    """Return the Terraform workspace."""
    proc = subprocess.run(  # nosec
        ["terraform", "workspace", "show"],
        capture_output=True,
        check=True,
        text=True,
    )
    return proc.stdout.strip()


def is_debug_set():
    """Check if the debug environment variable is set."""
    debug = os.getenv("TF_DEBUG", "").lower()
    return debug in ["1", "true"]


def wrapper():
    # In case tf was run with no arguments.
    if len(sys.argv) == 1:
        os.execlp("terraform", "terraform")  # nosec

    # Build a new argument list.
    args = sys.argv[:]
    args[0] = "terraform"

    # Check if the Terraform command is one that we need to modify (include
    # tfvars files). If not, execute Terraform with the same arguments.
    for command in TF_COMMANDS_TO_MODIFY:
        if command in sys.argv:
            break
    else:
        os.execvp("terraform", args)  # nosec

    # We need to add the var files after the Terraform command (if we add it
    # before Terraform doesn't accept them) but not at the end (not to modify
    # other argument that accept optional values). So we add them right after
    # the Terraform command.
    command_index = args.index(command)
    workspace = get_workspace()
    var_file = pathlib.Path(f"{workspace}.tfvars")
    var_dir = pathlib.Path(workspace)
    if var_file.exists() and var_file.is_file():
        args.insert(command_index + 1, f"-var-file={var_file}")
    elif var_dir.exists() and var_dir.is_dir():
        for var_file in glob.glob(f"{var_dir}/*.tfvars"):
            args.insert(command_index + 1, f"-var-file={var_file}")

    # Print the new argument list to stderr if debugging is enabled.
    if is_debug_set():
        print(args, file=sys.stderr)

    os.execvp("terraform", args)  # nosec


if __name__ == "__main__":
    wrapper()
