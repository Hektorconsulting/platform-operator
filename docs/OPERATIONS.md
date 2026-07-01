# Operations

## Lokale Entwicklung

Start from a clean clone and a dedicated branch:

`powershell
git checkout main
git pull --ff-only
git checkout -b chore/<short-task-name>
`

## Tests

Use repository-specific test commands only after the stack has been verified. Do not invent destructive checks.

## Build

Build commands must be derived from visible project files such as package.json, pyproject.toml, equirements.txt, Dockerfile, or existing workflow files.

## Deployment

No deployment workflow was changed by Phase 15B GitHub Wave1. Deployment changes require separate approval and runtime verification.

## Rollback

Documentation-only PRs can be reverted by reverting the merge commit or closing the branch before merge.

## Secrets / Env Handling

- Do not print, commit, or copy secret values.
- .env.example may contain variable names and empty placeholder values only.
- Real values belong in approved local secret stores, GitHub Secrets, VPS vault/secrets paths, or service-specific credential stores.