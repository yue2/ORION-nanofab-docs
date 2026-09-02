# Maintaining the ORION NanoFab Documentation

This project is **Markdown-first**. Future superusers should edit files under `docs/`, review the changes in Git, and regenerate the HTML site. Do not manually edit generated HTML.

## Documentation structure

```text
orion_nanofab_docs/
├── docs/                         # EDIT THESE MARKDOWN FILES
│   ├── index.md
│   ├── user-guide/               # all users
│   ├── superuser/                # restricted procedures
│   │   ├── training/
│   │   ├── maintenance/
│   │   └── error-recovery/
│   │       ├── shutdown/
│   │       └── troubleshooting/
│   ├── safety/                   # canonical safety section; superuser access
│   └── reference/                # all users
├── sources/                      # original PDFs/DOCX/JPG; preserve for traceability
├── assets/                       # site CSS/JS/images
├── src/data/nav_order.json       # GENERATED page order; do not hand-edit
├── build_site.py                 # converts Markdown to HTML data; writes nav_order.json
├── build_guide.py                # exports any docs/ folder to printable HTML in exports/
├── exports/                      # GENERATED printable HTML (user-guide.html, maintenance.html, ...)
├── index.html                    # generated site shell
└── MAINTAINING_THE_DOCS.md
```

## Editing workflow

1. Find the page under `docs/` and edit the Markdown, not `index.html` or generated JavaScript.
2. Keep the YAML metadata at the top of each page. Update `last-reviewed`, `sources`, and `status` when appropriate.
3. If a procedure changes because of a new controlled document, first add the new source file under `sources/`, then update the relevant Markdown page and its `sources:` list.
4. Do not silently reconcile conflicting source procedures. Record the conflict in the Markdown and have the Tool Owner approve the controlled wording.
5. Review the change in Git (diff + reviewer), then run `python3 build_site.py` from the project root.
6. Open `index.html` locally and test both User and Superuser navigation before publishing.
7. If you distribute printable exports, regenerate them with `python3 build_guide.py --<folder>` and verify the output under `exports/` (see "Exporting printable guides" below).


## Using the Documentation Reviewer Agent

This project includes a custom AI agent profile (`.agent.md`) that enforces read-only access and provides specialized documentation review guidance.

### Setup (one time)

1. Open this project folder in VS Code.
2. Open the integrated chat (Ctrl+Shift+I on Mac: Cmd+Shift+I).
3. Mention the agent in your first message:

   ```
   @ORION Documentation Reviewer: Review the calibration procedure for gaps.
   ```

   VS Code will load `.agent.md` automatically. The agent's specialized instructions and tool restrictions are now active.

### What the Agent Does

- **Reviews** Markdown procedures, Python build scripts, and source PDFs
- **Audits** YAML metadata, image paths, and broken links
- **Flags** procedural gaps with **WARNING — WAITING FOR MANUAL CONFIRMATION** blocks
- **Suggests** changes in chat; never modifies files
- **Enforces** strict read-only access per `AGENTS.md`

### Example Requests

- *"Audit the shutdown procedure against ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf. Are all steps present?"*
- *"Review docs/superuser/maintenance/ for conflicting guidance between local SOPs and manufacturer guidance."*
- *"Check all relative image paths in docs/user-guide/. Report broken links."*
- *"Review build_site.py for bugs in the --exclude-drafts filtering logic."*

### Important Limitations

The agent **cannot**:
- Edit, create, or delete files
- Run builds or Git commands that modify state
- Install packages or change settings
- Apply patches; it describes changes for you to apply manually

If a task requires file modification, the agent will describe the change in chat. You apply it manually.

### Customizing the Agent

If your workflow or access requirements change, edit `.agent.md` directly. The changes take effect the next time you reference the agent in a chat.

Refer to `AGENTS.md` for the access policy and governance rules that underpin the agent's behavior.

## Git workflow and version control

All documentation changes are tracked in Git. This enables:
- **Author attribution** on each page (Last edited by, Last modified, Git revision)
- **Contributor list** on the home page (extracted from all commits to `docs/`)
- **Change history** and accountability via Git log

### Initial setup (one time only)

```bash
cd /path/to/project
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add docs/ sources/ assets/
git commit -m "Initial documentation" 
```

Or if already configured globally, just initialize and commit:

```bash
git init
git add docs/ sources/ assets/
git commit -m "Initial documentation"
```

After editing documentation
1. Edit Markdown files under docs
2. Run the build: ```python3 build_site.py```
3. Review your changes: ```git diff docs/```
4. Stage and commit: 
```bash
git add docs/
git commit -m "Update [page-name]: [brief change description]"
```

## Access model

`access: all-users` pages are visible to trained users. `access: superuser` pages are marked restricted. The static site role switch is a preview only; real access control must be enforced by the hosting/authentication system.

## Content rules

- **User Guide:** normal operation plus warning recognition and clear stop/contact-superuser conditions.
- **Superuser / Training and Maintenance:** routine superuser duties. Safety information required for training is repeated here but the canonical safety material remains under `docs/safety/`.
- **Superuser / Error & Recovery:** shutdown, recovery, and troubleshooting procedures used when abnormal conditions occur.
- **Safety:** standalone canonical safety section.
- **Reference:** system concepts, controls, glossary, and source-document index.

## Markdown conventions

Use one H1 title per page, numbered lists for procedures, bullets for checks, and blockquotes for warnings/notes. Keep steps short and action-oriented. Put source filenames in YAML rather than deleting provenance.

## Adding a page

Create the `.md` file in the correct folder, add YAML metadata, then add its page entry to the `NAV` list in `build_site.py`. Running `build_site.py` regenerates `src/data/nav_order.json` automatically, so site navigation, pagination, search, and printable exports all keep the same order. Rebuild and test all links. Do not hand-edit `nav_order.json`.

## Source of truth

The Markdown files are the maintained documentation layer. The PDFs/DOCX/JPG files under `sources/` remain the evidence/reference layer. If a source is a formally controlled SOP or manufacturer manual, it takes precedence over this draft site until the site itself is placed under an approved document-control process.

## Full PDF information base

Every PDF in `sources/` has a complete source-transcription Markdown page under `docs/information-base/`. These pages contain the machine-extracted text page by page and a facsimile image of every PDF page. The page facsimiles preserve screenshots, figures, vector diagrams, handwritten annotations, and content that text extraction may miss.

Page images are stored under:

```text
assets/img/pdf-pages/<source-document>/page-001.webp
```

Do not manually edit the facsimile images. If a source PDF is replaced, regenerate its transcription/images from the new controlled source. Topic-oriented pages in `docs/user-guide/`, `docs/superuser/`, `docs/safety/`, and `docs/reference/` should remain curated operational documentation; `docs/information-base/` is the complete evidence/source layer.

## Citing the ZEISS Operator Manual for manual confirmation

When a local procedure has a logical gap, first check `ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf`. Add supported manufacturer guidance inside a **WARNING — WAITING FOR MANUAL CONFIRMATION** block. Always give both page systems when available:

```text
ZEISS Operator Manual §7.4.4, printed p. 161 (PDF page 166)
```

- **Printed page** means the page number printed in the footer/table of contents of the ZEISS manual.
- **PDF page** means the physical page number in the PDF viewer.
- Do not convert manufacturer guidance into an approved local step until a qualified superuser/tool owner confirms it applies to the installed instrument.
- If the Operator Manual does not cover the missing action, say so explicitly and cite the separate service/site document that must be checked.

## Adding and linking images

Keep documentation images under `assets/img/`. Use a descriptive subfolder rather than placing new images beside the Markdown files. The current convention is:

```text
assets/img/
├── general/                 # reusable overview / equipment images
│   └── orion-nanofab.png
└── pdf-pages/               # generated page facsimiles; do not edit by hand
```

### Example: add an image to the Home page

1. Copy the image into `assets/img/general/` and give it a stable descriptive filename. For example:

   ```text
   assets/img/general/orion-nanofab.png
   ```

2. Open `docs/index.md`.
3. Insert normal Markdown image syntax. Because `docs/index.md` is one directory below the project root, its source-relative path is:

   ```markdown
   ![ZEISS ORION NanoFab](../assets/img/general/orion-nanofab.png)

   *ZEISS ORION NanoFab workstation.*
   ```

4. Save the Markdown file.
5. Run `python3 build_site.py` from the project root.
6. Open `index.html` and verify the image, caption, mobile layout, and link paths.
7. Commit the image and Markdown change together so the documentation never references a missing asset.

For Markdown files nested more deeply under `docs/`, use the correct relative path back to the project root (for example `../../assets/...` or `../../../assets/...`). The build script normalizes these asset paths for the generated static site.

### Image maintenance rules

Use descriptive lowercase filenames with hyphens. Prefer PNG for screenshots/diagrams and JPEG/WebP for photographs when appropriate. Do not overwrite an image with materially different content without reviewing every page that references it. Add useful alt text inside `![...]`; do not use filenames as alt text. Keep original PDF page renders under `assets/img/pdf-pages/` separate from curated documentation figures.

## Auditing source completeness and procedure logic

The `docs/information-base/` files are the source-transcription layer. Text-readable PDFs should be represented there page-by-page without editorial shortening. Page facsimiles are retained directly below each page transcription to preserve figures, screenshots, handwritten annotations, and text that may not be represented by the PDF text layer.

When reviewing a new or revised procedure:

1. Compare every PDF page against its corresponding `docs/information-base/*.md` page section.
2. Preserve all source text. Do not silently rewrite or omit an awkward, duplicated, or apparently incorrect source instruction.
3. Check numbered and lettered sequences for gaps, prerequisites, state transitions, waits, verification criteria, and recovery/abort conditions.
4. If the source appears to omit a required transition, **do not invent the action**. Insert an explicit **manual-confirmation warning** in the curated procedure, for example:

   ```markdown
   > **WARNING — WAITING FOR MANUAL CONFIRMATION:** The local source jumps between steps. Add the relevant ZEISS Operator Manual guidance with **printed manual page number and PDF page number**, then state exactly what still requires site confirmation.
   ```

5. Keep the **WAITING FOR MANUAL CONFIRMATION** warning until a qualified superuser/tool owner confirms how the cited manufacturer guidance applies to the installed instrument.
6. Cite manufacturer guidance as `ZEISS Operator Manual §X.X, printed p. N (PDF page M)` so the reviewer can find it quickly. Record any other source used and update `last-reviewed`.
7. Rebuild the HTML and verify the manual-confirmation warning and page references are visible.

A **WAITING FOR MANUAL CONFIRMATION** block is an editorial safety flag, not an approved instruction. Manufacturer text may be appended inside the block for review, but it must not be presented as locally approved until confirmation is recorded.

## Exporting printable guides

`build_guide.py` exports any documentation folder under `docs/` into a single self-contained, printable HTML file under `exports/`. Local Markdown images are embedded as base64 so the exported file works offline. The script reads only local Markdown and local image assets, makes no network requests, invokes no shell, and never executes documentation content.

Run it with no flag for the default User Guide export, or pass a folder flag:

```bash
python3 build_guide.py                 # docs/user-guide/            → exports/user-guide.html
python3 build_guide.py --training      # docs/superuser/training/    → exports/training.html
python3 build_guide.py --maintenance   # docs/superuser/maintenance/ → exports/maintenance.html
python3 build_guide.py --shutdown      # docs/superuser/error-recovery/shutdown/       → exports/shutdown.html
python3 build_guide.py --troubleshooting  # docs/superuser/error-recovery/troubleshooting/ → exports/troubleshooting.html
python3 build_guide.py --safety        # docs/safety/                → exports/safety.html
python3 build_guide.py --reference     # docs/reference/             → exports/reference.html
python3 build_guide.py --information-base  # docs/information-base/  → exports/information-base.html
```

## Editing signatures and change monitoring

Approval signatures are intentionally **not implemented** at this stage. Editing traceability is separate from approval.

When the project is stored in a Git repository, `build_site.py` reads the most recent Git commit metadata for each Markdown file and shows it under the collapsible **Document information** panel:

- Last edited by
- Last modified
- Git revision (short commit hash)
- Page revision, status, owner and last-reviewed metadata

The Git lookup uses an argument-list invocation of `git log`; it does not invoke a shell. The repository commit history remains the authoritative editing audit trail. Use meaningful commit messages and individual Git identities rather than shared accounts.

If the documentation is distributed without its `.git` directory, Git history cannot be queried. For such offline copies, optional front matter can provide a display-only fallback:

```yaml
edited-by: "Superuser Name"
edited-date: "2026-08-31"
```

These fallback fields are not cryptographic signatures and should not be treated as proof of authorship. For monitoring edits, review `git log`, `git diff`, and your repository hosting service's branch/merge history. Do not add an `approved-by` field until an approval workflow is formally adopted.

## Code safety / malicious-operation review

Before publishing this revision, the build and browser code was reviewed for dangerous or unexpected operations. The intended code paths are limited to reading documentation/assets, writing generated local files, querying local Git metadata, exporting local Markdown to HTML files under `exports/`, browser-side search/navigation, and serving the pre-generated exported files.

The project does **not** intentionally contain code for deleting files, modifying permissions/ownership, installing software, uploading documentation, sending network requests, executing arbitrary Markdown content, or invoking shell command strings. `build_site.py` invokes only `git log` using a fixed argument list and `shell=False` (the Python default). `build_user_guide_pdf.py` renders local Markdown and image files with ReportLab and writes the PDF under `exports/`.

Future maintainers should repeat a source review when adding scripts or third-party JavaScript, and should pin/review dependencies in the deployment environment.

## Build dependencies

`build_guide.py` reads local Markdown and image files and writes printable HTML under `exports/`; it makes no network requests and invokes no shell.

```bash
python3 build_site.py
```

No `pip install` step is required. Both `build_site.py` and `build_guide.py` use only the Python standard library, so a future superuser can rebuild the site and the printable exports with a normal Python 3 installation. Earlier project versions depended on third-party packages such as `mistune`; those dependencies were removed. Keep any new build or export scripts dependency-free, or document their requirements in this section.

## Build modes and seeing local edits

The site is a single-page application. Markdown page content is compiled into `assets/app.js`; `index.html` is only the shell. A successful build therefore may leave `index.html` looking nearly unchanged on disk while `assets/app.js` contains the new documentation text.

Use `python3 build_site.py` during editing. This includes all pages, including `status: draft` pages. Use `python3 build_site.py --exclude-drafts` for a publication-style build that omits pages whose frontmatter has exactly `status: draft`. Use `python3 build_site.py --drafts-only` to review only draft pages. The two flags are mutually exclusive.

The builder prints the absolute project root, Markdown source directory, generated JavaScript bundle, and exact `index.html` to open. Check these paths if an edit appears not to build; this catches the common case of editing one extracted ZIP copy while opening another copy in the browser.

Each build also changes the `assets/app.js?v=...` query in `index.html`. This cache-busts the generated page bundle so a browser is less likely to reuse an older JavaScript file. If an already-open browser tab still shows old content, reload the page; a hard refresh can still be useful.

Git commits are not required to preview edits. The builder reads the current Markdown files directly from disk. Git is used only for optional editing-history metadata.
