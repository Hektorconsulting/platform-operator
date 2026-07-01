# Agent Context

## Rolle des Repos
Autonomous platform operator prototype for Hektor runtime operations.

## Produkt-/Kundenbezug
Platform Operator

## Wichtige Ordner
- docs/: agent-readable context and operations notes.
- .github/workflows/: GitHub Actions, if present.
- Repository-specific source/config folders must be inspected before edits.

## Wichtige Dateien
- README.md: human and agent onboarding.
- docs/REPO_CLASSIFICATION.md: source-of-truth classification.
- docs/OPERATIONS.md: safe operational commands and guardrails.
- .env.example: variable names only, when environment variables are known.

## Bekannte Risiken
- Risk level: MEDIUM
- Secret values must not be copied into docs, commits, issues, PRs, logs, or handoff packages.
- Existing production workflows must not be changed without a separate review.

## Was Codex/Hermes tun darf
- Read and classify repository contents.
- Improve documentation and agent context.
- Open branches and pull requests for reversible changes.
- Add placeholder-only .env.example files when variable names are visible.

## Was nur nach Freigabe geaendert werden soll
- main / master direct pushes.
- Deployments, DNS, VPS services, n8n workflows, GitHub Secrets or Variables.
- Branch protection, default branch, collaborator, repo transfer, archive, or delete settings.

## Naechste sinnvolle Entwicklungsaufgaben
- Confirm repo role in Hektor Master Index.
- Add or refine setup/test/build commands after verified local execution.
- Review Actions permissions before changing CI/CD.