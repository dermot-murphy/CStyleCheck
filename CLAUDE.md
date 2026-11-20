# Claude Code — standing instructions for CStyleCheck

## Branching strategy (Gitflow)

- This repo uses **Gitflow**. All feature/fix PRs target `develop`; hotfixes are the only exception that may target `main` directly.
- `develop` → `main` sync PRs are created only when explicitly requested by the repo owner; never create one automatically.
- After a release, `main` and `develop` are synced (docs, version bumps, etc. flow back to `develop`).
- Development branch naming convention: `claude/<topic>-<id>` (e.g. `claude/embedded-c-style-standards-pgqhdc`).

## Issue workflow

- Fix **all open GitHub issues**. Issues labelled `deferred` are parked (closed as not planned) — ignore them unless reopened.
- Never self-merge a PR — create the PR and wait for an external merge.

## Approval / authorisation (ASPICE)

- The repo owner's merge of a PR **is** the authorisation of every work product, review record, audit sign-off, CR approval / QA sign-off and Risk Owner confirmation that the PR introduces (CSC-DEV-002 §5.2). No signatures are collected.
- In approval tables write `By merge (CSC-DEV-002 §5.2) | On PR merge`; never leave `*pending*` signature entries or list signatures as an open owner action.

## Git / tagging

- In the **cloud** environment (`/home/user/CStyleCheck`), tag pushes (`git push origin <tag>`) return HTTP 403 from the git proxy. There, tell the user to push tags manually from their local machine.
- In a **local** session (`U:\GitHub\CStyleCheck`, the user's own git credentials, no proxy), tag pushes work. Push the tag after the user confirms.

## Repository scope

- GitHub MCP tools are restricted to `dermot-murphy/CStyleCheck` only.

## Paths

- Remote working directory: `/home/user/CStyleCheck`
- User's local repo root: `U:\GitHub\CStyleCheck`
