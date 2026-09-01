# ORION NanoFab Documentation

Edit documentation in `docs/`. Run `python3 build_site.py` to regenerate the HTML site data. See `MAINTAINING_THE_DOCS.md`.

### Build outputs

```bash
python3 build_site.py
python3 build_user_guide_pdf.py
```

The second command regenerates the Superuser-downloadable User Guide PDF with local Markdown images embedded.

## AI-Assisted Review

This project includes a custom VS Code agent (`.agent.md`) for read-only documentation auditing. See `MAINTAINING_THE_DOCS.md` for setup and usage.

The agent enforces strict access controls per `AGENTS.md` and cannot modify files, run builds, or execute Git commands that alter the repository.
