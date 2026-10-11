---
name: project-preparation
description: Turn an agreed PRD and implementation plan into product-specific context docs, a design-and-build workflow spec, and a verified project scaffold. Use to prepare a new project for implementation or adapt an existing starter; not for initial PRD creation or detailed implementation planning.
---

# Project preparation

Prepare a real project folder from the agreed product requirements and implementation plan. Context documents explain the product and technical boundaries; the workflow spec explains how agents follow the plan and collaborate with the user. Preserve existing work and accepted decisions. Supplied examples are evidence, not templates to copy.

## 1. Ground the preparation

Read the canonical PRD, reviewed PDF, implementation plan, available specs/design references, project instructions, and actual source/configuration. Identify accepted choices, open decisions, preparation tasks, and the verified baseline. If no implementation plan exists, identify planning as the prerequisite; `implementation-plan-workflow` or equivalent planning can provide it. Keep accepted source artifacts and their authority intact when assembling the folder.

Choose the documentation map using [context-package.md](references/context-package.md). Give each document a distinct purpose and authority. Confirm consequential gaps or changes with the owner; do not repeat discovery for settled decisions. Show the proposed folder/document map and preparation boundaries, reusing prior approval when it covers them. An executable starter is the default; a documentation-only handoff is an explicit owner choice.

Completion: source authorities, preparation scope, document map, and blockers are clear, with no consequential choice silently treated as settled.

## 2. Create context and workflow documents

Create populated product-specific context docs at the depth required for UI, domain/data, API, security, integrations, operations, setup, and engineering memory. Combine concerns when separate files would only duplicate the PRD. Each rule has one authoritative home. Reference the implementation plan for phases, slices, dependencies, checkpoints, and progress rather than generating another plan or plan-summary context document.

Read [build-workflow-handoff.md](references/build-workflow-handoff.md). Create or adapt the authoritative project design-and-build workflow spec, defaulting to `docs/build-workflow.md`, from the approved plan and actual project conventions. Include design-tool lookup or user-supplied flow inputs, relevant design readiness, verification, working demonstrations, user feedback and approval gates, and session resumption. Keep status, evidence, feedback, and approval records in the plan; the workflow spec defines how those records are maintained.

Create a navigable `README.md` and concise task-routed `AGENTS.md`. Route build, verification, review, and resumption to the plan and workflow spec, and product/technical tasks to the relevant authoritative docs. These project documents must remain usable without any skill installed.

Completion: every context file has product-specific substance, the workflow spec covers the project's delivery loop, and navigation links resolve to real authorities.

## 3. Scaffold and verify

Create the minimal source, test, and configuration skeleton for the agreed stack and the plan's preparation tasks. Preserve and adapt an existing repository. Document configuration, safe example values, prerequisites, actual setup/start commands, and outstanding provider setup. Create appropriate ignore rules before installing dependencies. Run the startup or smoke checks described in [context-package.md](references/context-package.md#scaffold-readiness-evidence). Record what was actually exercised, including mock/provider limits.

For a documentation-only handoff, describe initialization still needed and mark executable readiness unverified. Distinguish planned paths, services, tests, and deployments from actual files and verified behavior. If preparation exposes an incompatible assumption, record the evidence and update affected plan references/readiness within accepted scope; consequential changes return to the owner. Successful preparation does not require replanning.

Completion: the skeleton is verified within stated boundaries, or concrete blockers and remaining initialization work are recorded honestly. Feature implementation remains the subsequent build task.

## 4. Reconcile and hand off

Compare the package with the agreed PRD and plan for vocabulary, scope, permissions, state transitions, data ownership, stack, security, open decisions, and review/release gates. Check every promised artifact and local reference; retire references to intentionally removed documents. Run `python <skill-directory>/scripts/check_package.py <project-folder> --pdf <relative-pdf-path>` and inspect plain-text references the checker may miss.

Complete housekeeping and Git review in [context-package.md](references/context-package.md#local-files-and-git-handoff), then run `python <skill-directory>/scripts/audit_size.py <project-folder>`. Resolve or explain flags, preserve useful dependencies and unresolved failure evidence, and report local size separately from Git-eligible size and repository status.

Record preparation evidence and the next ready work in the existing plan. Finish with the project, PRD, plan, workflow-spec paths, verified readiness, and outstanding decisions/setup. Keep performed checks separate from future release evidence.
