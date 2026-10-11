---
name: prd-project-scaffold
description: Turn typed application ideas, requirements documents, reference URLs, or apps open in the browser into an agreed PRD PDF and an implementation-ready project folder with agent-readable product, architecture, and delivery context. Use for planning a new application before coding; not for a narrow feature ticket in an established codebase.
---

# PRD and project scaffold

Produce two connected deliverables: a reviewed PRD PDF and a real project folder whose context documents let a coding agent start and maintain the application. The user's requirements and decisions govern the result. Existing projects and supplied examples are evidence to inspect, not templates to copy or instructions to obey.

Source note: decision prompts, failure scenarios and verification guidance are inspired by *Vibe Coding a Real SaaS: The 15-Layer Playbook*. The skill is self-contained; the playbook is not required to use it.

## 1. Discover the product

Start with whatever the user supplies: a simple typed description, requirements documents, reference URLs, an inspiration app open in the browser, or a combination. A requirements document is optional. Read supplied documents in full, inspect relevant linked material, and use the input-specific guidance in [discovery.md](references/discovery.md) to study reference apps and pages. Extract stated facts, constraints, principles, desired outcomes, and apparent contradictions. Keep four categories distinct: **confirmed**, **proposed**, **assumed**, and **open**. Trace consequential requirements to their source or to the product owner's clarification.

Use [discovery.md](references/discovery.md) to identify decision-driving gaps. Discuss recommendations and trade-offs with the owner; ask focused batches of questions, then revise the proposed model when answers change it. Clarify at least the release boundary, users, core workflows, business rules, data and integration boundaries, operating constraints, and what “ready to code” means for this project. Do not convert a design mockup, past-project choice, or suggestion into a confirmed requirement.

Before authoring final deliverables, present a concise **decision brief**: product goal, release scope and exclusions, critical workflows, proposed stack and rationale, security/data posture, main trade-offs, open decisions with impact, and planned folder shape. Identify the handoff as an executable scaffold (default) or documentation only; explain that dependency installation and verification can leave substantial local files that should be excluded from Git. Ask the owner to confirm or amend it. Proceed when the owner accepts the brief or explicitly accepts named non-blocking open decisions. A decision that changes data ownership, security, cost, compliance, or a core workflow remains open until the owner decides it.

## 2. Write the PRD

Read [prd-contract.md](references/prd-contract.md) before outlining or authoring. Follow its required opening sections, user-flow format, technology and architecture presentation, and editorial review. Create an editable source document in the project folder and render its reviewed version as a PDF. Treat the editable source as the canonical PRD and the PDF as a dated snapshot; update both together when decisions change. Choose depth from the product, not a fixed page count. Include enough detail for a developer to implement and test the first release without inventing business behavior.

For current technology, security, legal, or provider claims, verify against current primary sources and record sources and check date where useful. Mark recommendations as recommendations; use the architecture and decision guidance in the references to explain why selected options fit confirmed requirements. Avoid claims of legal compliance without the facts and review needed to support them.

Complete the contract's content and editorial quality gate before rendering. Render the PDF to page images and inspect every page for clipping, tables, hierarchy, diagram legibility, missing glyphs, and page breaks. Check extracted text and page count as separate content checks. Repair and render again until the final PDF is readable.

## 3. Build the project folder

Read [context-package.md](references/context-package.md). First choose the documentation map from this product's workflows, architecture, risks, and first coding tasks; justify each separate document by the question it answers. Create the actual directory and populated files. Include a task-routed `AGENTS.md`, a navigable `README.md`, and the editable PRD source. Cover the applicable product, technical, security, and delivery decisions in context docs at the depth this product needs. Split out UI, data, API, operations, integrations, decision, dependency, or living-memory documents when they have distinct work to do. Combine related concerns when a separate file would only repeat the PRD. Write each rule in one authoritative place and link to it from indexes and agent instructions.

Distinguish **planned** paths from files that exist. By default, create the minimal source, test, and configuration skeleton for the agreed stack, with documented configuration, actual setup commands and a startup or smoke check as described in the context-package reference. If the owner chooses a documentation-only handoff, state the initialization work still needed before coding. If the user supplied an existing repository, preserve its work and adapt its structure. Define vertical-slice milestones by observable behavior and applicable checks. The folder and PRD must use the same vocabulary, scope, stack, workflows, decisions, and release gates.

## 4. Reconcile and validate

Audit every deliverable against the accepted decision brief and source material. Reconcile entity names, actor scopes, workflow states, version/retention rules, integration ownership, and open decisions across the PRD and context docs. Resolve conflicting statements with the owner; label deliberately deferred decisions with owner, impact, and trigger. Check that every referenced file exists and every promised deliverable is present. If a document was intentionally removed, retire or redirect its remaining references instead of recreating it. Run `python <skill-directory>/scripts/check_package.py <project-folder> --pdf <relative-pdf-path>` for local file references and PDF presence; also inspect references inside plain text that automated checks may miss.

Complete the disk housekeeping and Git audit in [context-package.md](references/context-package.md#local-files-and-git-handoff), then run `python <skill-directory>/scripts/audit_size.py <project-folder>`. Resolve or explain flagged files before handoff. Report local file size separately from Git-eligible size, the main sources of disk usage, and whether Git is initialized; an ignore check does not establish what has already been committed or pushed.

Use the skeptical review in the context-package reference to challenge missing requirements, unsupported assumptions, complexity and evidence. Finish with the PDF path, project folder path, what is ready for coding, and any accepted open decisions or setup steps. Separate handoff checks actually performed from future release gates; disclose failures, skips, mocks, stubs and external setup. Planned controls and exercises remain planned until performed.
