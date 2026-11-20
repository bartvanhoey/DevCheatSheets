# Code Audit Report

**Repository:** `Z:\Personal\MyGitHubRepos\DevCheatSheets`
**Date:** 2026-06-30
**Auditor:** Claude Code (graw-dev/code-audit)

---

## Executive Summary

**Overall Grade:** Good (well-maintained reference collection; minor content errors and consistency gaps)
**Critical Issues:** 0
**High Priority:** 3
**Medium Priority:** 8
**Low Priority / Observations:** 9

**Top 3 Priorities:**
1. Fix broken hyperlink in `Documents/Git.md:85` — renders as a mangled URL on GitHub Pages
2. Fix incorrect `docker run -t` description and duplicate `docker stop` row in `Documents/Docker.md`
3. Fix `CTRl` capitalisation typos in `Documents/VsCode.md` shortcut key table (6 occurrences)

---

## Findings by Category

### 1. Architecture & Design

#### 🟢 Low Priority / Observations

- `README.md` — Structure is clear and well-organised. Categories (IDE & Editors, DevOps & Cloud, .NET & C#, etc.) logically group all 26 topic files. Index is complete; every file in `Documents/` has a corresponding row. 🚫 Won't fix
- `CLAUDE.md` — Accurately describes the repository's structure and conventions. Good onboarding resource. 🚫 Won't fix
- `MauiTopics/` — Mentioned in CLAUDE.md as a directory for deeper MAUI notes but does not currently exist. If MAUI content is planned, either create the directory or remove the reference from CLAUDE.md. ✅ Fixed 2026-11-20

---

### 2. Code Quality

#### 🔴 High Priority

- `Documents/Git.md:85` — **Broken hyperlink.** The Whodid link is malformed: `[Whodid]([https://](https://www.npmjs.com/package/whodid))`. The `[https://]` prefix inside the link target breaks the URL and renders as a nested bracket expression on GitHub Pages. ✅ Fixed 2026-06-30
  - **Impact:** Readers clicking this link get a broken page.
  - **Recommendation:** Change to `[Whodid](https://www.npmjs.com/package/whodid)`
  - **Effort:** 2 minutes

- `Documents/Docker.md:33` — **Duplicate table row.** `docker stop <container-id>` appears twice (lines 32–33) with identical descriptions. ✅ Fixed 2026-06-30
  - **Impact:** Confusing redundancy; readers may assume there is a meaningful difference.
  - **Recommendation:** Delete the duplicate row.
  - **Effort:** 2 minutes

- `Documents/Docker.md:38` — **Incorrect command and description.** `docker run -t <image-name>:<tag> -f .\CreateTestDb.Dockerfile .` is described as "build docker container from specific Dockerfile." ✅ Fixed 2026-06-30 The `-t` flag on `docker run` means *tag*, not Dockerfile specification. The correct command uses `docker build -f`. The syntax is also invalid (`-f` after the image name is not a valid `docker run` flag).
  - **Impact:** A developer following this command will get an error or unexpected behaviour.
  - **Recommendation:** Replace with: `docker build -f .\CreateTestDb.Dockerfile -t <image-name>:<tag> .`
  - **Effort:** 5 minutes

#### 🟡 Medium Priority

- `Documents/VsCode.md:22,27,29,40,47,51,55` — **`CTRl` capitalisation typos** (lowercase `l`) in 7 shortcut key rows: ✅ Fixed 2026-06-30 `CTRl+ALT+C`, `CTRl+ALT+T`, `CTRl+B, CTRL+B`, `CTRl+K+S`, `CTRl+SHIFT+.`, `CTRl+SHIFT+G`, `CTRl+SHIFT+P -> Balance (outward)`.
  - **Recommendation:** Change all occurrences to `CTRL` (uppercase L).
  - **Effort:** 5 minutes

- `Documents/VsCode.md:84` — **Typo in extension name.** `C# Dev Kist` should be `C# Dev Kit`. ✅ Fixed 2026-06-30
  - **Impact:** Readers searching for this extension by name will not find it.
  - **Effort:** 1 minute

- `Documents/VsCode.md:91` — **Mid-word capitalisation in author name.** `Error Lens - ALexander` has a rogue capital (`ALexander`). ✅ Fixed 2026-06-30
  - **Recommendation:** Change to `Error Lens - Alexander`.
  - **Effort:** 1 minute

- `Documents/VsCode.md:94–96` — **Possible duplicate extension entries.** Both `html tag wrapper` (line 94) and `html tag Wrapper - hwencc` (line 96) appear to be the same extension listed twice; `-hwencc` is the author's marketplace ID. ✅ Fixed 2026-06-30
  - **Impact:** Redundant entries bloat the table and may confuse readers.
  - **Recommendation:** Verify whether these are distinct extensions; if the same, keep the `hwencc` entry (more specific) and remove the generic one.
  - **Effort:** 5 minutes

- `Documents/VsCode.md:184,197` — **Wrong code fence language for JSON content.** The `ColorTabs settings` block (line 184) and `Prettier settings` block (line 197) use ` ```bash ` fences but contain JSON configuration snippets. This disables JSON syntax highlighting. ✅ Fixed 2026-06-30
  - **Recommendation:** Change both fence labels from `bash` to `json`.
  - **Effort:** 2 minutes

- `Documents/Git.md:140` — **Stray backtick leaking out of inline code.** The line reads: `` git log origin/master..HEAD` view unpushed git commits `` — the closing backtick ends the code span mid-line, leaving "view unpushed git commits" as stray text. ✅ Fixed 2026-06-30
  - **Recommendation:** Restructure to: `` `git log origin/master..HEAD` — view unpushed git commits ``
  - **Effort:** 2 minutes

- `Documents/DotNet.md:60` — **Machine-specific hardcoded username.** The text reads `C:\Users\bartv\AppData\Roaming\Microsoft\UserSecrets` — `bartv` is specific to one machine. ✅ Fixed 2026-06-30
  - **Impact:** Readers on other machines will follow an incorrect path.
  - **Recommendation:** Replace with `%USERPROFILE%\AppData\Roaming\Microsoft\UserSecrets`
  - **Effort:** 2 minutes

- `Documents/DotNet.md:17,23,29` — **Heading style inconsistency.** Three headings use `### How to ...` (two words) while the repo-wide convention is `### Howto ...` (one word). ✅ Fixed 2026-06-30
  - **Recommendation:** Normalise to `### Howto ...`
  - **Effort:** 5 minutes

#### 🟢 Low Priority / Observations

- `Documents/Git.md:249,294` — Near-duplicate sections on reverting commits (`git reset --hard HEAD` vs `git reset --hard HEAD~1`). The distinction is meaningful but easy to miss. Add a one-liner clarifying `HEAD` vs `HEAD~1`. ✅ Fixed 2026-06-30

- `Documents/Git.md:279,298` — Near-duplicate sections on amending commit messages (un-pushed vs pushed). The pushed variant correctly adds `git push --force-with-lease`, but that command is erroneously placed inside the VIM `:wq` code block. Extract it to its own block after the VIM instructions. ✅ Fixed 2026-06-30

- `Documents/Git.md:97,105,110,115,125,129` — Non-standard ` ```batch ` fence label used in several blocks. GitHub Pages renders `batch` as plain text without syntax highlighting. Change to `bash` or `cmd`. ✅ Fixed 2026-06-30

- `Documents/Git.md:191` — `git push --force` recommended as a solution with no caveat. Add a note recommending `git push --force-with-lease` instead, which is safer. ✅ Fixed 2026-06-30

- `Documents/PowerShell.md:1` — Heading reads `## Powershell` — should be `## PowerShell` (capital S), consistent with README and Microsoft branding. ✅ Fixed 2026-06-30

---

### 3. Security

**N/A for this stack** — static Markdown documentation published via GitHub Pages. No application code, no user input, no authentication, no backend. No security findings apply.

---

### 4. Performance

**N/A for this stack** — static site served by GitHub Pages. No runtime performance concerns.

---

### 5. Testing

- A `validate.yml` GitHub Actions workflow exists (badge shown in README). The badge was green at the time of audit, indicating the workflow is active.
- No automated broken-link detection was found. Given the broken link at `Git.md:85`, adding a link-checker step to the validate workflow would be a worthwhile low-cost improvement. ✅ Fixed 2026-06-30
  - **Recommendation:** Add `lychee-action` or `markdown-link-check` to the validate workflow.
  - **Effort:** 30 minutes

---

### 6. Maintainability

#### 🟡 Medium Priority

- `Documents/PowerShell.md` — **Stub file with only 3 entries.** PowerShell is a primary tool for Windows/.NET developers (the stated audience), yet this is the thinnest file in the repo. 🚫 Won't fix
  - **Recommendation:** Expand with common PowerShell patterns relevant to the .NET/Windows workflow.
  - **Effort:** 1–2 hours

- `Documents/PowerShell.md:7,13,19` — **PowerShell code blocks use `bash` fence.** Change to `powershell` for correct syntax highlighting. ✅ Fixed 2026-06-30
  - **Effort:** 2 minutes

#### 🟢 Low Priority / Observations

- `.vscode/settings.json` — `cSpell.words` list is well-maintained and alphabetically ordered. 🚫 Won't fix
- `.markdownlint.json` — Suppresses `MD041`, `MD013`, `MD020`, `MD060` — all appropriate for this cheat-sheet format. 🚫 Won't fix
- Git commit history shows consistent activity and emoji conventional commit style. Good hygiene.

---

## Prioritized Action Plan

### Quick wins (< 30 minutes total)

1. Fix broken Whodid link — `Documents/Git.md:85`
2. Delete duplicate `docker stop` row — `Documents/Docker.md:33`
3. Fix `CTRl` → `CTRL` typos — `Documents/VsCode.md:22,27,29,40,47,51,55`
4. Fix `C# Dev Kist` → `C# Dev Kit` — `Documents/VsCode.md:84`
5. Fix `ALexander` → `Alexander` — `Documents/VsCode.md:91`
6. Fix `## Powershell` → `## PowerShell` — `Documents/PowerShell.md:1`
7. Fix stray backtick — `Documents/Git.md:140`
8. Replace `bartv` username with `%USERPROFILE%` — `Documents/DotNet.md:60`
9. Change `bash` fences to `json` — `Documents/VsCode.md:184,197`
10. Change `bash` fences to `powershell` — `Documents/PowerShell.md:7,13,19`
11. Change `batch` fences to `bash` — `Documents/Git.md:97,105,110,115,125,129`

### Medium-term (under 2 hours)

12. Fix incorrect `docker run -t` command — `Documents/Docker.md:38`
13. Resolve duplicate `html tag wrapper` extension entries — `Documents/VsCode.md:94–96`
14. Normalise `How to` → `Howto` headings — `Documents/DotNet.md:17,23,29`
15. Add `git push --force-with-lease` safety note — `Documents/Git.md:191`
16. Fix `git push --force-with-lease` placement inside VIM block — `Documents/Git.md:298–308`
17. Add broken-link check to validate workflow

### Long-term initiatives (ongoing)

18. Expand `Documents/PowerShell.md` — currently a stub for a core tool in the target audience's workflow

---

## Metrics

| Metric | Value |
|--------|-------|
| Files analysed | 8 of 28 Markdown files (representative sample) |
| Total Markdown files | 28 |
| Lines of content reviewed | ~1,100 |
| Critical findings | 0 |
| High priority findings | 3 |
| Medium priority findings | 8 |
| Low priority / observations | 9 |

---

*Generated by graw-dev/code-audit skill via Claude Code*
