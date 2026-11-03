#!/usr/bin/env python3
"""Make sure this computer can build and print documents for the jobagento plugin.

The build script needs Python with Jinja2. It gets its own virtual
environment in the plugin's data folder, made once and kept across plugin
updates, so nothing is installed into the user's own Python. It prints
nothing when all is well; otherwise one short note per missing tool, which
Claude reads at session start and can pass on.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

CHROMES = [
    "google-chrome",
    "chrome",
    "chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def has_jinja(python):
    return python.is_file() and subprocess.run(
        [str(python), "-c", "import jinja2"], capture_output=True
    ).returncode == 0


def prepare_venv(data):
    """Create the venv with Jinja2 if it isn't there yet. Returns a note on failure."""
    venv = data / "venv"
    if has_jinja(venv / "bin" / "python"):
        return None
    data.mkdir(parents=True, exist_ok=True)
    log = data / "setup.log"
    with log.open("w") as out:
        for step in (
            [sys.executable, "-m", "venv", str(venv)],
            [str(venv / "bin" / "pip"), "install", "--quiet", "--disable-pip-version-check", "jinja2>=3.1"],
        ):
            if subprocess.run(step, stdout=out, stderr=out).returncode != 0:
                return f"Could not prepare the job-app Python environment (see {log})."
    return None


def main():
    notes = []
    note = prepare_venv(Path(os.environ["CLAUDE_PLUGIN_DATA"]))
    if note:
        notes.append(note)

    for tool in ("pdfinfo", "pdftotext"):
        if not shutil.which(tool):
            notes.append(f"{tool} is missing: install poppler (macOS: brew install poppler, Debian/Ubuntu: apt install poppler-utils).")

    if not any(shutil.which(c) or os.access(c, os.X_OK) for c in CHROMES):
        notes.append("Google Chrome is missing: the job-app builder prints with it, and the submitter fills forms in it.")
    if not shutil.which("npx"):
        notes.append("Node.js (npx) is missing: the browser tools need it.")

    if notes:
        print("jobagento plugin setup notes:")
        for n in notes:
            print(f"- {n}")


if __name__ == "__main__":
    main()
