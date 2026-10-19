# Installation & distribution guide

## Universal packaging
The **skill directory** must be named `aster-landing-design`, with `SKILL.md` directly inside. Install the **directory**, not `SKILL.md` by itself; relative references are needed. Copy the full folder to an agent-supported skill root. Directory conventions vary by product/version and settings; verify against the IDE's current documentation.

| Agent / IDE | Typical project-local destination | Typical user destination |
|---|---|---|
| Claude Code | `.claude/skills/aster-landing-design/` | `~/.claude/skills/aster-landing-design/` |
| Cursor | `.cursor/skills/aster-landing-design/` or `.agents/skills/aster-landing-design/` | `~/.cursor/skills/aster-landing-design/` or `~/.agents/skills/aster-landing-design/` |
| Codex | `.agents/skills/aster-landing-design/` | `~/.agents/skills/aster-landing-design/` (supported setups) |
| GitHub Copilot / VS Code | `.github/skills/aster-landing-design/` where supported | See IDE settings/documentation |
| Gemini CLI | `.agents/skills/aster-landing-design/` where supported | See runtime/version documentation |
| Other AI IDEs | Agent Skills-configured skill root | See vendor documentation |

**Do not copy it into all directories automatically.** Choose the target IDE and inspect existing files first; a shared `.agents/skills` location can be used when supported.

## Manual installation (macOS/Linux)
After extracting the ZIP into a directory containing `aster-landing-design/`:

```sh
mkdir -p .agents/skills
cp -R aster-landing-design .agents/skills/
python3 .agents/skills/aster-landing-design/scripts/validate_skill.py
```

If that destination exists already, back it up or perform an intentional update; do not overwrite unknowingly.

## Manual installation (Windows PowerShell)
From the directory containing the unzipped skill:

```powershell
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse .ster-landing-design .\.agents\skillspy .\.agents\skillsster-landing-design\scripts
alidate_skill.py
```

PowerShell examples are for project-scoped `.agents/skills`; substitute your actual configured path as needed.

## Distributing through GitHub
Publish this folder in a repository, with root `SKILL.md` located under `aster-landing-design/`, include license and versioned releases. Consumers may `git clone` or download release ZIP. Do **not** advertise a `npx ...` installation command until the repository exists and that CLI's exact syntax has been verified. URLs to install are intentionally omitted until you publish.

## Activation test
After restarting or refreshing your agent, ask: `Use aster-landing-design to inspect my project and create a landing page for [topic]. Explain which skill references you used.` If the agent does not list the skill, confirm its configured scan path, name/frontmatter match, case, and folder nesting. On unsupported IDEs attach `SKILL.md`, `references/` and (when relevant) `assets/` directly to the agent context.

## Security
Read third-party skills before installing. They are instructions that may influence code changes. This package's validation script reads local files only and performs no network requests or writes. Treat generated code as subject to human review and repository tests.