#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def read_problem(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 2)
        if len(parts) >= 2:
            fm = parts[0] + "\n" + parts[1]
            # strip leading --- and parse simple key: value pairs; avoid yaml dep
            fm_body = fm.strip("-\n")
            for line in fm_body.splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = parts[2] if len(parts) == 3 else ""
    # Fallback title from first heading
    if not meta.get("title"):
        m = re.search(r"^#\s+(.+)$", body, re.M)
        if m:
            meta["title"] = m.group(1).strip()
    return {"meta": meta, "body": body}


def ensure_odr_available() -> str:
    # Prefer CLI if present; else check module
    for cmd in ("open-deep-research", "open_deep_research", "deep-research", "deep_research"):
        if shutil.which(cmd):
            return cmd
    try:
        import importlib

        importlib.import_module("open_deep_research")
        return "python -m open_deep_research"
    except Exception:
        return ""


def run_odr(cli_cmd: str, prompt: str) -> str:
    # Try common CLIs: assume it prints Markdown to stdout given a prompt arg
    candidates = [
        [cli_cmd, "--query", prompt],
        [cli_cmd, "--topic", prompt],
        [cli_cmd, prompt],
        ["python", "-m", "open_deep_research", "--query", prompt],
        ["python3", "-m", "open_deep_research", "--query", prompt],
    ]
    last_err = None
    for cmd in candidates:
        try:
            # Support when cli_cmd is space-separated (python -m ...)
            if isinstance(cli_cmd, str) and " " in cli_cmd and cmd[0] == cli_cmd:
                cmd = cli_cmd.split() + cmd[1:]
            out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
            if out and len(out.strip()) > 50:
                return out
        except Exception as e:
            last_err = e
            continue
    raise RuntimeError(
        f"Failed to execute open_deep_research. Tried several CLI forms. Last error: {last_err}"
    )


def wrap_with_front_matter(content_md: str, meta: dict) -> str:
    now = dt.date.today().isoformat()
    title = meta.get("title", "Deep Research Report")
    sdg = meta.get("sdg", "[]") if isinstance(meta.get("sdg"), str) else meta.get("sdg", [])
    if isinstance(sdg, list):
        # Render list as YAML array
        sdg_yaml = "[" + ", ".join([f'"{x}"' for x in sdg]) + "]"
    else:
        sdg_yaml = str(sdg)
    front_matter = (
        "---\n"
        f"title: \"{title}\"\n"
        f"authors: [\"agent:deep-research\"]\n"
        f"date: {now}\n"
        f"sdg: {sdg_yaml}\n"
        "licence: CC-BY-4.0\n"
        "spdx: CC-BY-4.0\n"
        "---\n\n"
    )
    return front_matter + content_md.strip() + "\n"


def main():
    ap = argparse.ArgumentParser(description="Generate a deep research style report from problem.md using open_deep_research")
    ap.add_argument("--problem", default="problem.md", help="Path to problem.md")
    ap.add_argument("--out", default="docs/report.draft.md", help="Output Markdown path")
    args = ap.parse_args()

    problem_path = Path(args.problem)
    if not problem_path.exists():
        print(f"ERROR: problem file not found: {problem_path}", file=sys.stderr)
        sys.exit(2)

    data = read_problem(problem_path)
    meta = data["meta"]
    body = data["body"].strip()
    title = meta.get("title", "Deep Research Task")

    preface = (
        f"You are an expert research collective. Produce a deeply cited, structured, long-form report in Markdown. "
        f"Topic: {title}. Use headings, tables where helpful, bullet lists, and include an executive summary, assumptions, methodology, findings, risks, and recommendations. "
        f"Cite sources inline with links. Keep it decision-oriented and reproducible.\n\n"
    )
    prompt = preface + body

    cli = ensure_odr_available()
    if not cli:
        print(
            "ERROR: open_deep_research not found.\n"
            "Install: pip install -U open-deep-research OR pip install -U open_deep_research\n"
            "Ensure you have API keys set (e.g., OPENAI_API_KEY, ANTHROPIC_API_KEY) as required by your provider.",
            file=sys.stderr,
        )
        sys.exit(3)

    print(f"Running open_deep_research via: {cli}")
    try:
        md = run_odr(cli, prompt)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(4)

    wrapped = wrap_with_front_matter(md, meta)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(wrapped, encoding="utf-8")
    print(f"Wrote draft report: {out_path}")


if __name__ == "__main__":
    main()

