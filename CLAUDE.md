# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is Bart Van Hoey's personal reference / cheat-sheet collection — a set of Markdown notes on development tools and topics (Git, Docker, Kubernetes, .NET, Blazor, Next.js, MAUI, VS Code, Rider, Tailwind, etc.). There is no application code, no build system, and no test suite. Changes here are edits to documentation files, not software changes.

The repository is published via GitHub Pages directly from the `gh-pages` branch, which is also the repo's main/default branch — there is only one branch in normal use.

## Structure

- `README.md` — the index page: a Markdown table linking to every file in `Documents/`. When adding a new topic file, add a corresponding row here.
- `Documents/*.md` — one file per topic (e.g. `Git.md`, `Docker.md`, `VsCode.md`). Entries within a file are typically a `##` heading naming a task/problem ("Howto handle ...") followed by an explanation and/or fenced code block.
- `Images/` — screenshots referenced by the Markdown docs.

## Conventions

- `.markdownlint.json` disables `MD041` (first line must be a top-level heading) and `MD013` (line length) — don't "fix" files to satisfy these rules.
- Commit messages are generic (`Update`) for routine content edits — `Publish.bat` simply runs `git pull && git add . && git commit -m Update && git push`. Don't invent more elaborate commit messages for routine doc additions/edits unless asked.
- Keep new entries consistent with the existing style in a file: a `##`/`###` heading describing the problem or task, then a short explanation, then a fenced code block with the command/snippet.
