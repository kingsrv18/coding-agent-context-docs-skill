# Product-shaped context package

Create a real folder whose documents answer the questions a coding agent will face for **this** application. Read the agreed PRD and implementation plan before choosing the documentation map. The supplied reference folders illustrate different product needs; neither is a file checklist. Explain the map as part of preparation, preserving prior decisions.

## Stable handoff

The package contains a navigable `README.md`, a concise task-routed `AGENTS.md`, the existing editable canonical PRD source and reviewed PDF, the existing implementation plan, a populated design-and-build workflow spec, and enough context docs to implement the agreed first release. Preserve source authority when bringing existing artifacts into the folder. File names and category folders beyond that follow the product. A separate document earns its place when it has a distinct authority, reader, update cadence, risk boundary, or task trigger. Otherwise keep the content with its nearest authoritative topic. Reference the plan rather than creating a separate phase/task-summary context document.

For each proposed file, answer:

1. What implementation decision or workflow does it make clearer?
2. Which tasks should load it, and which document points to it?
3. Which facts does it own that should not be repeated elsewhere?
4. Will it contain product-specific substance on handoff day?

Remove a proposed file when these answers are weak. Add a file when a single document becomes too broad for reliable task routing.

## Select documents from the product

| Product characteristic | Context that may deserve its own document |
| --- | --- |
| Many actors, approvals, or exceptions | Actor journeys, permission and record-scope matrix, state transitions, correction paths. |
| Complex domain or calculations | Canonical vocabulary, entity ownership, invariants, formulas, versioning and worked examples. |
| Sensitive or regulated data | Data classification, threat model, authorization, audit, retention, key and access controls, release evidence. |
| Multiple tenants or organizations | Tenant boundary, identity/membership model, isolation and cross-tenant test cases. |
| Heavy imports, files, or integrations | File lifecycle, mapping/validation, external contracts, failure and retry behavior, dependency/setup register. |
| Important reports or exports | Data provenance, calculation grain, snapshots, permissions, reconciliation and acceptance fixtures. |
| Large or designed UI | Shared interaction rules, navigation, screen states, design-source authority and accessibility. |
| Several deployable parts or demanding operations | Runtime topology, environments, secrets, observability, backup/recovery and deployment plan. |
| Long-lived modular codebase | Module ownership, codebase map, engineering memory and maintenance rules. |
| Agentic development with user review gates | Build-workflow spec, design/preview inputs, checkpoint approval and resume rules; see [build-workflow-handoff.md](build-workflow-handoff.md). |

These are prompts for selection, not automatic files. A small application may cover several rows in one architecture note. A larger product may split one row across modules or workflows. Preserve the user's current design and delivery workflow; no screen catalogue is required by this package.

## Agent navigation

`AGENTS.md` should point to the **actual authoritative documents** by task trigger: product behavior, interface, domain/API, data, access/security, integration, testing or release as applicable. Route build, verification, review, and resumption to both the implementation plan and design-and-build workflow spec. State source precedence and how to raise an unresolved contradiction. Keep it short enough that an agent can find the relevant source quickly. Do not duplicate the PRD or cache facts visible in configuration.

The `README.md` should show what exists now, the chosen folder tree, how to start work, and where to find the PRD and context docs. Links must resolve. Keep an open-decision register when material choices remain; it may live in the PRD or in a separate file. Keep requirement sources and owner clarifications traceable; a separate source register is useful when the input set is large or conflicting.

## Planned versus implemented

Match source, test and configuration directories to the selected stack and module ownership. Include only code/configuration that can be maintained and verified at this stage. A documentation-only handoff is an explicit owner choice. Mark paths, services, tests and deployments **planned / not implemented** until they exist; never let a context document imply a build or integration has passed because it was specified. Add living engineering memory, a codebase map or dependency register when they will help maintain real implementation facts; seed them honestly and update them alongside code.

### Scaffold readiness evidence

Document required configuration, purpose, safe example values and how to obtain external credentials without storing secrets. Distinguish public client configuration from server secrets, and separate local/test and production resources where applicable. Include startup validation appropriate to the stack for missing or invalid required settings, with actionable errors. Provide actual setup and start commands for the created files, prerequisites and external provisioning still needed. Verify claimed build paths and run a startup or smoke check that exercises the available skeleton; record commands, outcomes and boundaries exercised. A process starting with mocked providers establishes only that limited result. If startup cannot be verified, name the blocker and leave readiness unverified. Documentation-only handoffs identify initialization steps instead of claiming executable readiness.

### Local files and Git handoff

Prefer compatible tools already installed or supplied by the agent environment, and use standard shared package/tool caches where available. If a project-local tool or PDF virtual environment is needed, keep it in a named ignored location and document how to recreate it. Record prerequisites in setup instructions rather than bundling runtimes into the portable handoff. Preserve installed dependencies needed to start development.

Create stack-appropriate `.gitignore` rules before installation and verification. Cover dependency folders, build caches/output, portable tools, virtual environments, render scratch, test reports and local secrets while keeping manifests, lockfiles, source, configuration examples, canonical documents and reviewed PDFs eligible. Choose rules from actual generated paths; an ignored directory can still contain already-tracked files.

After verification, remove installation archives created by this run once checksum verification (where supplied), extraction and a tool invocation have succeeded, unless an offline handoff needs the archive. Remove disposable page renders and transient build/test output created by this run when they are reproducible and no longer needed for review or debugging; retain concise verification results and final deliverables. Preserve existing project files, useful installed tools/dependencies, and unresolved failure evidence. Before recursive cleanup, resolve and check the absolute target inside the intended scratch directory, and avoid following directory links or junctions. Document what was retained and how to regenerate cleaned output.

Run `scripts/audit_size.py` from the skill against the project after housekeeping. It reports logical file bytes (excluding Git metadata), largest top-level folders/files, and files eligible under project `.gitignore` rules, using Git's matcher in a temporary repository when necessary. It skips directory links/junctions to avoid counting workspace dependencies twice; skipped paths and unreadable files are disclosed. Machine-wide ignore rules are deliberately excluded so another machine receives the same handoff. In an existing repository, currently tracked files remain eligible even when ignored; review those flags without automatically changing the index. History and remote contents require separate inspection when relevant.

The audit flags eligible files of at least 50 MiB by default (`--large-mib` adjusts the review threshold), generated folders missing ignore coverage, and tracked files matching ignore rules. Review historical PDFs, diagrams and backup archives for their purpose rather than excluding all binary files. These are review flags, not automatic deletion instructions or a universal hosting limit. Missing Git or unreadable paths leave the audit incomplete; disclose the limitation. The script's exit codes are 0 for no flags, 1 for review flags, and 2 for incomplete measurement/classification; `--json` emits the full report.

Include local size, Git-eligible size, largest disk consumers, ignore coverage and repository status in the handoff. Explain retained local bulk and any unresolved flags. A documentation-only handoff still gets the audit, with initialization steps stated explicitly.

### Acceptance checks, tests and release evidence

Use the PRD's acceptance criteria and the existing plan's completion checks: for example, an authorized user creates and retrieves a record while another tenant is denied, rather than merely creating an endpoint file. Prepare the procedure for following that plan using [build-workflow-handoff.md](build-workflow-handoff.md). Context specs may clarify product-specific verification contracts; phases and task sequencing remain in the plan. Identify business-logic, persistence/integration and end-to-end checks from the risks; cover critical journeys without imposing a universal coverage percentage or testing tool. Include integration tests at real boundaries where those boundaries determine correctness. Review whether a broken behavior would fail a test and whether mocks bypass the rule being tested. When changing tests, explain the requirement or defect that justifies the change and preserve intended behavior unless the owner has changed it.

Record checks performed and their results separately from checks planned for implementation or release. Disclose failures, skips, mocks, stubs, assumptions and external setup so another agent can assess what the evidence supports. Specify applicable automated checks that gate merges or deployments and how migration failures affect rollout. Backup restores, rollback exercises, an error reaching its tracker, alert delivery and expected-load tests remain planned until actually performed; for applicable release gates, identify an owner, environment, procedure and pass criterion. A written recovery procedure or configured alert is not evidence that recovery or delivery worked. Performance changes should have before/after measurements when their benefit is claimed.

## Reconciliation

Compare every created document with the canonical PRD for vocabulary, scope, actor access, state transitions, data ownership, stack, security controls, open decisions and release gates. Check only the topics that apply to the product, but check all of those thoroughly. When a document is intentionally removed, retire or redirect its references. Confirm that every file named by `README.md` or `AGENTS.md` exists and that every created context file has a clear reason to remain.

Then review skeptically: could an implementer still need to invent a business rule, failure path or security boundary? Which assumptions lack evidence or owner acceptance? Which components or documents add complexity without serving confirmed requirements? What claimed readiness exceeds the checks actually performed? Resolve material gaps, simplify unsupported choices and qualify unsupported claims before handoff; return owner decisions to the open register rather than silently choosing them.
