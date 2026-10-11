# Coding Agent Context Docs Skills

Turn an application idea into an agreed PRD, create its implementation plan, then prepare a project folder that coding agents can use to build and resume work.

Three focused skills have distinct responsibilities and can be installed independently. They accept equivalent existing artifacts; no individual stage requires another skill to be installed. A fourth skill, `software-workflow`, coordinates all three in order through one invocation.

## Install

Install [Node.js](https://nodejs.org/) (including npm/npx) and [Git](https://git-scm.com/), then run:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill
```

Follow the prompts to choose skills, an agent, and project or global installation. The installer is the open-source [Skills CLI](https://github.com/vercel-labs/skills); its [supported agents](https://github.com/vercel-labs/skills#supported-agents) do not necessarily provide every tool needed by these workflows.

Install all three globally for Codex:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill --skill prd-creation implementation-plan-workflow project-preparation --agent codex --global --yes
```

For the coordinated workflow, install the coordinator and all three stage skills together:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill --skill software-workflow prd-creation implementation-plan-workflow project-preparation --agent codex --global --yes
```

To install an individual skill, specify its name with `--skill`. Replace `--agent codex` with `claude-code`, `cursor`, or `github-copilot` as appropriate. Remove `--global` for project installation; use `--copy` if symbolic links are unavailable.

These skills replace the former combined `prd-project-scaffold`. Existing generated project documents remain usable; use the focused skills for subsequent work. Previously installed copies of the combined skill should be removed when adopting the replacement skills. Repository changes become available through these GitHub commands after publication.

## Workflow and included skills

Use [software-workflow](.agents/skills/software-workflow/SKILL.md) to run the stages below in order. It carries accepted decisions and artifacts forward, preserves required gates, and resumes from the earliest incomplete stage. Its default endpoint is project preparation; feature implementation follows only when requested. The coordinator needs all three focused skills available and keeps their procedures in their existing homes.

| Stage | Skill | Deliverables |
| --- | --- | --- |
| 1 | [prd-creation](.agents/skills/prd-creation/SKILL.md) | Agreed product requirements, editable canonical PRD, reviewed PDF, and architecture diagram source. |
| 2 | [implementation-plan-workflow](.agents/skills/implementation-plan-workflow/SKILL.md) | Phases, small executable slices, preparation dependencies, named flow/module checkpoints, and persistent progress. |
| 3 | [project-preparation](.agents/skills/project-preparation/SKILL.md) | Populated context docs, design-and-build workflow spec, README/AGENTS navigation, and verified project starter. |

### PRD creation

Start with a typed idea, requirements documents, reference URLs, an inspiration app open in the browser, or a combination. A requirements document is optional.

The skill clarifies consequential decisions and confirms the product brief, then documents users, flows, business rules, release scope, acceptance criteria, stack, architecture, and relevant technical boundaries. It preserves an editable source and visually reviews the rendered PDF. Detailed implementation phases and project scaffolding belong to the following stages.

### Implementation planning and workflow

Plan directly from the agreed PRD and available specs/design references. Existing source and verified work are used when present; a scaffold and full context package are not prerequisites.

The plan includes small slices with inputs, actions, outputs, dependencies, and completion evidence. UI work is visible by named flow and paired with backend/integration work. Every completed UI flow or module has a working demonstration and user approval checkpoint. Missing designs can be explicit later readiness inputs.

For new projects, preparation precedes feature implementation. The plan owns live status, verification evidence, feedback, approval history, blockers, and resume information. During an authorized build, this skill follows and maintains the plan using the prepared workflow spec.

### Project preparation

Use the agreed PRD and implementation plan to choose product-specific context docs and create an executable starter, or a documentation-only handoff when explicitly chosen. Preserve accepted decisions and existing code. Verify startup within the available boundaries and report configuration/provider setup still needed.

The skill creates `docs/build-workflow.md` or adapts an equivalent authoritative spec. It tells future agents how to:

- Select the next ready flow/module from the plan and check prerequisites.
- Retrieve relevant designs directly from an accessible linked design tool or use supplied material; ask the user for the next flow's design when missing or inaccessible.
- Build and verify bounded work, then demonstrate a working preview with safe representative data, navigation, and relevant states.
- Obtain flow/module review, resolve feedback, show revisions, and obtain explicit approval before advancing past the checkpoint.
- Maintain evidence and progress in the plan and resume from the recorded state.

Non-UI modules use an appropriate runnable demonstration. Mock and real boundaries remain explicit. The workflow spec defines procedures; it does not duplicate the implementation plan. Generated project instructions link both documents so agents can work without these skills installed.

Preparation also checks local links and performs a disk/Git audit, separating installed dependencies and generated files from files eligible for version control.

## Use it

Start a new agent session after installation if the skills have not appeared. Agents supporting `$skill-name` can invoke them directly.

Run the full workflow:

```text
Use software-workflow to take my tutor booking app idea
through an agreed PRD, implementation plan, and prepared project.
Students should find tutors, book sessions, and track upcoming lessons.
```

You can still invoke any stage independently using the examples below.

Discover and specify:

```text
Use prd-creation to plan a booking app for independent tutors.
Students should find tutors, book sessions, and track upcoming lessons.
Help me agree the first release, then create the editable PRD and reviewed PDF.
```

Reference analysis:

```text
Use prd-creation with these reference URLs: <URLs>, or the inspiration
app I have opened in my browser. Study its workflows and help me decide
which behavior my product should adopt.
```

Identify or share the target tab through the agent's browser integration. Opening a tab alone does not grant access in every agent. When browser tools are unavailable, provide page content or a walkthrough. Observations and inferred rules remain distinct from agreed requirements.

Plan after PRD agreement:

```text
Use implementation-plan-workflow with this agreed PRD. Include project
preparation before feature work, small slices, named UI flows paired with
backend work, and working demonstration approval checkpoints.
```

Prepare the project:

```text
Use project-preparation with this PRD and implementation plan.
Create the context docs, design-and-build workflow spec, agent instructions,
and verified starter. Include linked-design lookup, requests for missing
flow designs, and user review/approval before advancing past each checkpoint.
```

Build or resume:

```text
Use implementation-plan-workflow to implement the next ready slice.
Follow the project's workflow spec, record progress and verification,
and show the working demonstration at the next approval checkpoint.
```

## Tools needed

Agents need file and terminal access, web/browser access for relevant references and current technical claims, and PDF generation/rendering tools with page-image inspection. Python 3 runs the package checker and size audit; build tools depend on the agreed stack.

The skills do not install browser integrations, design-tool connections, or PDF tools automatically. Building needs an accessible preview or an appropriate runnable demonstration for non-UI modules. Agents must disclose unavailable inputs, mocks, setup blockers, and unverified readiness.

## Manage installation

List available skills:

```sh
npx skills add kingsrv18/coding-agent-context-docs-skill --list
```

For example, update or remove a global installation:

```sh
npx skills update prd-creation --global --yes
npx skills remove prd-creation --global
```

Use the relevant skill name for the other skills. For project installations, run from the project and omit `--global`.

## Repository layout

```text
.agents/skills/software-workflow/
  SKILL.md                     Coordinates the three focused stages
  agents/openai.yaml
.agents/skills/prd-creation/
  SKILL.md
  agents/openai.yaml
  references/                  Discovery and PRD contract
.agents/skills/implementation-plan-workflow/
  SKILL.md
  agents/openai.yaml
  references/plan-contract.md   Slices, checkpoints, and progress
.agents/skills/project-preparation/
  SKILL.md
  agents/openai.yaml
  references/                  Context package and workflow-spec handoff
  scripts/check_package.py     Generated-package reference checker
  scripts/audit_size.py        Read-only disk usage and Git ignore audit
  scripts/test_audit_size.py   Behavioral audit tests
```

Complete skill folders are installed with their supporting resources. No npm package publication is needed for GitHub installation.

## Related skills

This project was developed with skills from [mattpocock/skills](https://github.com/mattpocock/skills), maintained upstream and installable separately:

```sh
npx skills add mattpocock/skills --skill writing-for-agents grilling
```

## Contributing

Open an issue with a concrete use case or submit a pull request. Keep requirements traceable, observed reference behavior distinct from product decisions, and responsibilities consistent across skill entry points and supporting references.

## License

[MIT](LICENSE).
