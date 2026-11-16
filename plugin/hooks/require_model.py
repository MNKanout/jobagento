#!/usr/bin/env python3
"""PreToolUse hook for starting an agent (the Agent tool, Task in older
Claude Code).

Each jobagento agent's model lives in the database, not in its file:
get_settings returns agent_models, the defaults with the user's own choices
on a paid plan, and the main session passes the agent's one as `model`. A
hook cannot read it itself (it has no access to the user's /mcp login), so
it makes sure it was passed:

- a jobagento agent started without a model, or with one the Agent tool
  does not know, is denied, with what to do instead;
- anything else (a model given, or another plugin's or project's agent)
  passes untouched: this hook prints nothing for it.

If this hook itself fails, Claude Code starts the agent as asked.
"""
from __future__ import annotations

import json
import sys

PREFIX = "jobagento:"
MODELS = {"haiku", "sonnet", "opus"}


def decide(event: dict) -> str | None:
    """The reason to deny this call, or None to let it pass."""
    tool_input = event.get("tool_input") or {}
    agent = tool_input.get("subagent_type")
    if not isinstance(agent, str) or not agent.startswith(PREFIX):
        return None
    if tool_input.get("model") in MODELS:
        return None
    name = agent[len(PREFIX):]
    return (f"Start {agent} with its model from the database: call get_settings (once per command) and pass "
            f"model: agent_models['{name}'] (one of {', '.join(sorted(MODELS))}).")


def main() -> None:
    reason = decide(json.load(sys.stdin))
    if reason:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}))


if __name__ == "__main__":
    main()
