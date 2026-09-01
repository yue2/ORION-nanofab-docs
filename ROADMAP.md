## Content

- [ ] revise docs in user-guide/
- [ ] audit docs/superuser/training/ for completeness and source traceability
- [ ] audit docs/superuser/maintenance/ for procedure gaps and safety conflicts
- [ ] audit docs/superuser/error-recovery/ for conflicting guidance vs. ZEISS manual
- [ ] audit docs/safety/ for emergency procedures and high-voltage warnings
- [ ] audit docs/reference/ for glossary completeness and broken internal links
- [ ] audit docs/information-base/ for source PDF transcription completeness
- [ ] verify all `sources:` frontmatter fields reference existing PDFs under `sources/`
- [ ] verify all image paths in Markdown point to valid files under `assets/img/`
- [ ] verify access-level tags (`all-users`, `superuser`) match folder structure
- [ ] resolve all **WARNING — CONFLICTING GUIDANCE** blocks with Tool Owner approval
- [ ] resolve all **WARNING — WAITING FOR MANUAL CONFIRMATION** blocks
- [ ] update `last-reviewed` dates for all published pages
- [ ] check for orphaned or unreferenced pages in NAV

## Code

- [ ] fix pagination redirect (SPA data-page routing)
- [ ] implement full-text search with access-level filtering (all-users vs. superuser)
- [ ] add search result access-control logic in `app.js`
- [ ] test pagination navigation across all user-guide pages
- [ ] test pagination navigation across all superuser pages
- [ ] verify build script generates correct `data-page` attributes
- [ ] add CI/CD workflow file for automated builds (`.github/workflows/`)
- [ ] create CONTRIBUTING.md for colleague onboarding
- [ ] document build instructions in README.md
- [ ] upload to GitHub and configure repo settings

## Review & Handoff

- [ ] Request Tool Owner sign-off on all flagged procedural conflicts
- [ ] Brief team on documentation structure and audit rules (AGENTS.md)
- [ ] Set up GitHub branch protection for documentation PRs
- [ ] Archive source PDFs in `sources/` as immutable reference