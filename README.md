# platform-operator

## Zweck
Autonomous platform operator prototype for Hektor runtime operations.

## Zugeordneter Wissensraum
- Hermes / Autonomie KI

## Stack
- Python, systemd service, requirements.txt

## Lokales Setup

`powershell
git clone Hektorconsulting/platform-operator
cd platform-operator
`

Read docs/AGENT_CONTEXT.md and docs/OPERATIONS.md before changing code or automation.

## Environment Variables

Only names and placeholder values are documented. Never commit real secret values.

## Entwicklung

Codex/Hermes should work through short-lived branches and pull requests. Keep changes small, reversible, and documented.

## Deployment

No deployment process is assumed until the current runtime path is verified.

## Offene Punkte

- Confirm production role and source-of-truth owner.
- Add project-specific setup commands after runtime verification.
- Keep secrets out of reports, commits, logs, and handoff bundles.