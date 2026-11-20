## Project Health Report

**Project:** DevCheatSheets | **Stack:** Markdown documentation (no manifest; text-based fallback) | **Date:** 2026-11-20 | **Assessed by:** Claude

> This is a documentation-only repository with no compiled code. Every dimension was assessed with the text-based fallback, so each grade carries the `?` marker. The grid is a poor fit for a docs repo — Code Quality and Test Coverage in particular measure markdown hygiene and automated validation, and read harsher than the repository's real state.

### Grades

| Dimension | Grade | Score | Key Finding |
|-----------|-------|-------|-------------|
| Build Health | A? | 95 | No build system. `scripts/validate.py` passes (README links, orphaned docs); 0 errors, 0 warnings. |
| Code Quality | F? | 50 | 23 markdown issues in ~2.4K lines (≈9.6/1K): 21 code fences without a language tag, 2 stub files. All cosmetic. |
| Architecture | A? | 92 | 27/27 topic files indexed in README, 0 orphans, 0 broken local links or image refs, 0 cycles. |
| Test Coverage | D?* | 35 | No tests. Validation is `validate.py` plus 2 CI workflows (`validate.yml`, `links.yml`). They cover the structure, not the content. |
| Dead Code | B? | 85 | 4 dead items: unused `Images/commitmessages.png`, stub `Css.md`, stub `UsefulClaudeCodeSkills.md`, stale `MauiTopics/` reference in `CLAUDE.md`. |
| API Surface | B~? | 85 | README index is consistent (category tables, link plus description). One outlier: a very long file name (`ScottSauber10OptionsToCreateMoreMaintainableDotNetApps.md`). |
| Security | B? | 85 | No real secrets. One sample credential in an example: `Kubernetes.md:117` (`SA_PASSWORD="pa55w0rd!"`). |
| Documentation | B? | 85 | README and CLAUDE.md are clear. CLAUDE.md is stale (describes `MauiTopics/` and `MAUI.md`, which don't exist). Two topic files are one-line stubs. |

### Overall GPA: 2.6 — Fair

> Fair — functional but accumulating tech debt

### Priority Recommendations

1. **Code Quality (F → A):** Add a language tag to the 21 opening code fences without one (`text`, `bash`, `powershell`, …):
   - `Documents/Herdr.md` (11), `Documents/AKS.md` (6), `Documents/Kubernetes.md` (3), `Documents/PowerShell.md` (3), `Documents/ABPcli.md` (2)
   - Complete or remove the stubs `Documents/Css.md` (2 lines) and `Documents/UsefulClaudeCodeSkills.md` (4 lines)
   Estimated effort: 30–45 minutes

2. **Documentation (B → A):** Refresh `CLAUDE.md`:
   - `CLAUDE.md:15` — Remove the `MauiTopics/*.md` bullet and the `Documents/MAUI.md` reference, and drop MAUI from the topic list
   - Mention `scripts/validate.py` and the two GitHub workflows in the Structure section
   Estimated effort: 10 minutes

3. **Dead Code (B → A):** Remove or use the unreferenced image:
   - `Images/commitmessages.png` — not referenced by any document; embed it in `Documents/Git.md` or delete it
   Estimated effort: 5 minutes

4. **Test Coverage (D → C):** Extend `scripts/validate.py` with cheap content checks:
   - Fail on topic files shorter than N lines
   - Fail on unreferenced images
   - Fail on unlabeled code fences (enable markdownlint `MD040` in CI)
   Estimated effort: 1–2 hours

5. **Security (B → A):** Replace the literal password in `Documents/Kubernetes.md:117` with a placeholder such as `<your-password>`.
   Estimated effort: 5 minutes

### Conclusion

The repository is structurally sound: the README index is complete, there are no orphaned files or broken links, and CI validation passes. The GPA of 2.6 is pulled down mainly by the dimensions that fit a docs repo poorly (Code Quality, Test Coverage), so treat it as indicative only. The best next step is the quick markdown cleanup — language tags on the 21 fences, the two stub files and the stale `CLAUDE.md` entry — which would lift the GPA past 3.0.
