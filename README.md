# Coding Agent Context Docs Skill

Turn an application idea into an agreed product requirements document (PRD) and a project folder that a coding agent can use to start implementation.

Start with a typed description, a requirements document, reference URLs, an inspiration app open in your browser, or a combination. A requirements document is optional.

## Install with one command

Install [Node.js](https://nodejs.org/) (which includes npm and npx) and [Git](https://git-scm.com/), then run this command in your terminal:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill
```

Follow the prompts to select your coding agent and choose project or global installation. Project installation makes the skill available in the current project; global installation makes it available across your projects.

The installer is the open-source [Skills CLI](https://github.com/vercel-labs/skills). Its [supported agent list](https://github.com/vercel-labs/skills#supported-agents) includes Codex, Claude Code, Cursor, GitHub Copilot, and other agents. Installation support does not guarantee that every agent provides the browser, PDF, or terminal tools needed for the full workflow.

### Install directly for your agent

These commands install globally and skip interactive prompts:

| Agent | Command |
| --- | --- |
| Codex | `npx skills add kingsrv18/coding-agent-context-docs-skill --skill prd-project-scaffold --agent codex --global --yes` |
| Claude Code | `npx skills add kingsrv18/coding-agent-context-docs-skill --skill prd-project-scaffold --agent claude-code --global --yes` |
| Cursor | `npx skills add kingsrv18/coding-agent-context-docs-skill --skill prd-project-scaffold --agent cursor --global --yes` |
| GitHub Copilot | `npx skills add kingsrv18/coding-agent-context-docs-skill --skill prd-project-scaffold --agent github-copilot --global --yes` |

Remove `--global` to install into the current project. If your system cannot create symbolic links, add `--copy`.

## Included skill

### prd-project-scaffold

The skill studies your inputs, clarifies consequential decisions, and asks you to confirm a decision brief before creating the final deliverables:

- An editable canonical PRD and a reviewed PDF snapshot.
- A real project folder with a README, task-routed AGENTS.md, and product-specific context documents.
- Product, architecture, data, security, and delivery decisions at the depth your application needs.
- A minimal implementation skeleton for the agreed stack, or a documentation-only handoff if you choose it.
- A disk/Git handoff report distinguishing installed tools and generated files from files eligible for version control.

It is intended for planning a new application before coding. See the [skill instructions](.agents/skills/prd-project-scaffold/SKILL.md) for the complete workflow.

## Use it

After installation, start a new agent session if the skill has not appeared. Ask your agent to use `prd-project-scaffold`; agents that support `$skill-name` invocation can use `$prd-project-scaffold` directly.

Example prompts:

```text
Use prd-project-scaffold to plan a booking app for independent tutors.
Students should find tutors, book sessions, and track upcoming lessons.
Start by helping me decide the first release scope.
```

```text
Use prd-project-scaffold with these reference URLs: <URLs>.
Study the relevant workflows and help me adapt them for my product.
```

```text
Use prd-project-scaffold. I have opened an inspiration app in my browser.
Study its scheduling workflow and help me plan a version for my business.
```

```text
Use prd-project-scaffold to turn the attached requirements document into
an agreed PRD PDF and an implementation-ready project folder.
```

For browser analysis, identify or share the target tab through your agent's browser integration. The agent needs access to that browser session; opening a tab alone does not grant access in every coding agent. When browser tools are unavailable, provide page content or a walkthrough. The skill records observed behavior separately from inferred rules and asks which reference features your product should adopt.

## Tools needed for the full workflow

The skill is instructions, not an application runtime. Your agent needs local file and terminal access to create the project folder, web access to study URLs and verify current technical claims, and browser tools to inspect interactive apps. PDF generation also needs a renderer and a way to inspect rendered pages; use your agent's available PDF/document tools. Python 3 is needed for the included package checker. Build tools depend on the stack agreed during discovery.

The skill guides tool use but does not install browser integrations or PDF tools automatically. Your agent should report inaccessible inputs and unverified setup rather than claim they were checked.

## Manage your installation

List the skills available in this repository without installing:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill --list
```

Update a global installation:

```sh
npx skills update prd-project-scaffold --global --yes
```

Remove a global installation:

```sh
npx skills remove prd-project-scaffold --global
```

For project installations, run management commands from that project and omit `--global`.

## Repository layout

```text
.agents/skills/prd-project-scaffold/
  SKILL.md                  Skill entry point
  agents/openai.yaml        Codex display metadata
  references/               Discovery, PRD, and context-package guidance
  scripts/check_package.py  Generated-package reference checker
  scripts/audit_size.py     Read-only disk usage and Git ignore audit
```

The complete folder is installed, including the supporting references and checker. No npm package needs to be published for installation from GitHub.

## Related skills

This project was developed with skills from [mattpocock/skills](https://github.com/mattpocock/skills). Those skills are maintained upstream and can be installed separately:

```sh
npx skills add mattpocock/skills --skill writing-for-agents grilling
```

## Contributing

Open an issue with a concrete use case or submit a pull request. Keep requirements traceable, distinguish observed reference behavior from product decisions, and keep instructions consistent across the entry point and supporting references.

## License

[MIT](LICENSE).
