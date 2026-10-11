# PRD contract

The PDF is a product and architecture contract for the agreed release, not a polished rewrite of an incomplete idea. Its editable source lives in the project folder. Use the required opening structure below; organize later sections for the product while covering each applicable concern in this contract. The main document must explain the product and architecture without requiring the reader to open context files or appendices.

## Required opening structure

Include document control and a navigable contents list, followed by these numbered sections:

1. **About this document:** purpose, intended readers, how to use the document and how confirmed decisions differ from proposals and open items.
2. **Executive summary:** problem, product promise, complete first-release outcome and measures of success.
3. **Product scope and user experience:** distinct subsections for primary users and supporting actors, how the app is used, release scope and exclusions, use cases, and the user flows to build. Keep domain vocabulary separate from the explanation of people and their work.
4. **Technology stack:** introductory explanation followed by **4.1 Layer by layer**, using the table format below.
5. **Architecture overview:** introductory explanation and architecture diagram, followed by **5.1 Architecture layers**, **5.2 Request path**, **5.3 Why this architecture**, and **5.4 Module boundary rules**.

Preserve sections 4 and 5 and their subsections across products. Adapt technologies, architecture style, layer count and boundary rules to the agreed product; the UMS reference supplies the presentation pattern, not a universal eleven-layer design or technology selection. Later sections cover functional requirements, domain/data, security, integrations, operations and delivery at the depth required. Detailed appendices supplement the main explanation.

## Users, use cases and user flows

The primary-users subsection explains who uses the application most, their working context, goals and difficulties, and why the product helps. Identify buyers and supporting actors separately, with their responsibilities and access boundaries. The usage subsection describes the overall operating loop and how first-time, daily and periodic tasks connect.

Use a use-case table with **ID | Actor | Goal and trigger | Successful outcome | Release | Flow reference**. Give every in-scope use case a flow reference and every critical first-release flow a complete walkthrough. Supporting use cases may share a flow where their paths are explicitly covered. Separate later-release use cases visibly.

Derive coverage from the accepted scope, capability matrix and functional requirements, including applicable setup, master data, money/corrections, files/delivery, reports/audit, access/connection lifecycle, operational recovery and closure tasks. Audit both directions: every in-scope item reaches a concrete flow or explicitly described branch, and each proposed flow traces to accepted scope. A populated flow reference is insufficient if the referenced walkthrough omits that item's behavior. Preserve an ID-based coverage record for review; distinguish later work and unresolved source details from completed specification.

Give each flow a stable ID and descriptive heading. Explain its purpose and scenario, then identify actors, trigger, preconditions and entry point. Present the normal path as numbered steps or a table with **Step | Screen or workspace | User action and input | Visible system response and next state**. Capture decisions and actor handoffs where they happen. Proposed screen names describe planned workspaces; they do not imply an existing UI or prescribe final visual design.

After the normal path, explain alternate paths, validation and permission failures, cancellation/correction, pending work and recovery as applicable. State the final user-visible outcome, records or notifications produced, and observable acceptance checks. Describe what the user sees and does before explaining supporting technical safeguards. A backend processing summary or a sentence saying that a journey must include failure states is insufficient: document the actual applicable states and recovery behavior for that flow.

Include a flow diagram for journeys with branching or multiple actor handoffs when it makes the sequence easier to follow. Keep the written walkthrough authoritative and align diagram labels with its steps. State machines supplement user flows by explaining lifecycle rules.

## Technology and architecture presentation

### Section 4 Technology stack

Use **Layer | Choice | Decision status | Reasoning and comment** for the layer-by-layer table. Cover all applicable technology responsibilities, including clients, backend, identity, authorization, database and hosting, data access, files, jobs/events, communications, integrations, search/reporting, edge, observability and delivery. Explicitly label an intentionally deferred or unnecessary component where readers would otherwise expect it.

Each row explains what the choice does, why it fits this product, and material constraints or trade-offs. Use decision statuses that distinguish accepted choices from recommendations, confirmations needed and deferred items; link unresolved choices to the decision register. Record versions or version policy and ownership where relevant. Follow the table with a short explanation of aggregate supplier cost, maintenance burden, important dependencies and switching costs. Keep detailed estimates in their authoritative section and summarize the implications here.

### Section 5 Architecture overview

Embed a readable, product-specific diagram showing actors/clients, entry points, application/module boundaries, authoritative data and files, background work, external systems and relevant trust or tenant boundaries. Label important arrows with their purpose and distinguish synchronous requests from asynchronous work. Clearly distinguish the agreed release from deferred components. Supply the editable diagram source in the project folder and a full-resolution export if the embedded version needs enlargement; confirm that the diagram agrees with the tables and prose.

- **5.1 Architecture layers:** use **Layer | Contents | Responsibility and boundary**. Explain how each layer contributes to the product, what it owns and where enforcement happens. Adapt the layer count to the application.
- **5.2 Request path:** walk through a representative product action from the user's interface through identity, permissions, application behavior and persistence to the visible response. Explain background/provider follow-up separately when applicable, including what the user sees while waiting or on failure.
- **5.3 Why this architecture:** explain the selected topology using the product's transactions, workload, team and operating constraints. State meaningful alternatives and consequences, and the conditions that would justify revisiting the choice. For a modular monolith, explain why that choice fits; for another topology, explain that choice instead.
- **5.4 Module boundary rules:** identify module responsibilities, permitted dependency directions, interface/event contracts, data ownership and where permission checks belong. Specify how critical boundaries will be verified in implementation. For a small application, describe its actual component boundaries without inventing modules or services.

## Explanation and editorial review

Write for product owners and developers together. Introduce each major section with what it covers and why it matters. Develop substantive subsections with connected explanations of the behavior or decision, its reason and consequence, and a concrete product example where that helps. Use tables for comparison and numbered steps for sequences; prose explains the relationships between them.

Define unfamiliar terms and acronyms on first use or link them to a glossary. Keep user tasks distinct from implementation mechanics. Replace compressed semicolon-heavy feature inventories with meaningful subsections and walkthroughs. Preserve technical detail and uncertainty while making the main narrative understandable to a reader unfamiliar with the project. Match a supplied writing reference's explanatory depth and organization where the owner adopts them; adapt its domain facts and recommendations to the current product.

Before rendering, read the document in order and check that a newcomer can explain who it serves, how it is used, what each critical flow accomplishes, why the stack was selected and how the architecture supports those flows. Revise sections that only name concepts or send readers elsewhere for their explanation. Choose length from these completion criteria rather than compressing to a page budget.

For a revision test, compare the candidate with the previous artifact, adopted writing reference and this contract. Record concrete findings by section/flow and classify each as a missing source decision, an instruction gap, or an execution/rendering defect. Make bounded instruction refinements, regenerate affected content and recheck coverage, decisions, diagram and rendered pages. Keep the candidate and its review evidence separate from canonical documents until the owner accepts promotion; record which context authorities then need reconciliation. Preserved appendices supplement the main narrative and retain their original decision and verification status.

## Product contract

- Document control: title, version, date, owner, status, source inputs and decision state.
- Executive summary: problem, target users/customers, product promise, measurable outcomes.
- Release boundary: in scope, out of scope, later phases, assumptions and dependencies. State the complete first-release user outcome.
- Personas and permissions: use the users and flows format above; include responsibility, record scope, sensitive-data visibility and approval boundaries.
- Canonical vocabulary and domain model: entities, ownership, cardinality, lifecycle, historical integrity; distinguish business concepts from database tables.
- User journeys: trigger, preconditions, normal path, exceptions/corrections, outputs, notifications and acceptance criteria for every critical flow. Specify applicable loading, empty, error, pending, success and permission states: what the user sees, what actions are available and how to recover. An empty state offers a next action, an error state explains recovery, and pending forms prevent accidental duplicate submission. For example, a pending export retains its job status across reloads; a failed export explains whether retry is safe. Check critical journeys for missing states, keyboard access and responsive behavior. Include state transitions and guards where relevant.
- Functional requirements: stable IDs or another traceable scheme; priority, source, behavior, error/edge handling and acceptance checks. Link to journeys and release scope.
- Nonfunctional requirements: security, privacy, accessibility, performance, capacity, availability, recovery, supportability, localization and data retention as applicable. Quantify targets or mark them as open.

## Technical and delivery contract

- Stack and topology: selected components, versions or version policy, ownership boundaries, alternatives considered, reasons, trade-offs and expected cost/operating burden.
- Data design: authoritative sources, storage/isolation model, invariants, migration/import/export, consistency, concurrency, versioning, backups and deletion/retention. Use the conditional design prompts below.
- Interfaces and integrations: contracts, trust boundaries, event ordering, retries/idempotency, recovery, human/provider setup and observability. Use the failure contracts below.
- Security layers derived from a product-specific threat model: authentication, server-side authorization and object scope, tenant isolation where relevant, input/file handling, sensitive data, encryption/keys, audit, secrets, network/runtime controls, detection and recovery. Identify the owner and verification method for critical controls.
- UI/experience system: navigation, critical screens/states, responsive/accessibility needs and design-source authority when relevant.
- Implementation plan: dependency-ordered vertical slices, observable milestone outcomes and applicable checks, migration and rollout plan, pilot feedback, release gates and handoff. Use the context-package guidance to separate completed handoff verification from planned release evidence.
- Risks, decisions and open questions: record consequential decisions as context, decision, alternatives and consequences beside their authoritative topic; separate files only when useful. For pending choices, include recommendation, owner, impact, deadline/trigger and mitigations.
- Traceability: a reader can follow a high-risk requirement from source to flow, architecture control, test and release gate.

## Enforceable boundaries and failure contracts

Apply these prompts only where the product needs them; record concrete behavior rather than a catalogue of technologies. Choose identifiers, deletion policy, pagination, cache infrastructure and error/status conventions from the product and stack. Examples illustrate decisions, not universal requirements.

- **Permissions:** connect each actor/action/record-scope rule to its server enforcement point and representative negative tests. Include unauthenticated and unauthorized access; for organizations, cross-tenant reads/writes and membership removal or role changes during an active session or queued job. Check restricted actions through direct requests, not just hidden buttons. Where teams exist, define invitation expiry, ownership transfer and last-owner behavior as product decisions.
- **Data invariants:** identify rules that must survive concurrent requests, imports and retries. Examples include one active membership per user/organization, a valid transition from draft to approved, or a reservation that cannot exceed capacity. Choose database constraints, transactions or another enforcement mechanism appropriate to the storage system. Specify monetary currency, precision and rounding (for example, integer minor units or exact decimals rather than binary floats), when money is involved. Derive indexes from expected filters, joins and ordering; document migration sequencing, existing-data handling and recovery from partial failure. Acceptance fixtures should represent realistic volume, ownership, boundary values and invalid cases relevant to the release.
- **Integrations and jobs:** define boundary validation and how incoming events are authenticated, such as verified webhook signatures. Define request/event identity, duplicate and delayed event handling, ordering assumptions, retryable versus terminal failures, retry limits and exhausted-job disposition. State who can recover or replay work and how repeated attempts avoid duplicate charges or effects; include replay tests that assert the intended effect occurs once. For subscriptions, define the authoritative billing state and how delayed, failed or out-of-order events affect entitlements and reconciliation.
- **Queries and caches:** identify list bounds, pagination and expensive query patterns such as repeated per-record fetches. Introduce caching only for a justified need; define freshness, invalidation and keys that preserve tenant and permission boundaries. For tenant-sensitive caches, test the same operation from two tenants and after a relevant update or access change. Shared delivery layers must not expose private responses to other users.
- **Abuse and cost:** for public, paid or resource-intensive actions, specify enforcement of rate/usage quotas, concurrency limits and spending protection. Estimate launch capacity and recurring cost from explicit assumptions such as active users, requests per user, job duration and provider cost; identify the threshold that requires revisiting the design. Decide behavior when a limit is reached, including user feedback and recovery.
- **Operations:** define important alerts with an owner, actionable threshold and recovery procedure. Where dependencies matter, distinguish process health from readiness to serve work (for example, a running worker whose queue is unreachable). Plan request/job correlation, useful error context and sensitive-data redaction so failures are diagnosable without leaking credentials or personal data. Define security and data boundaries now; derive implementation checks and release evidence from those decisions.

## Quality gate

Before delivery, verify all of the following against the source and rendered PDF:

- Primary users, supporting actors, usage model and use-case inventory are explicit in the main document. Every in-scope use case maps to a documented flow, and every critical first-release flow includes user steps, visible responses, applicable recovery and acceptance checks.
- Sections 4 and 5 and their required subsections exist with substantive product-specific tables, rationale, request walkthrough and boundary rules. The architecture diagram is present, legible and consistent with scope, stack and prose; its editable source exists.
- The editorial review passes: major sections explain behavior, reasons and consequences, unfamiliar terms are defined, and a reader can understand the product without consulting appendices or project context files.

The package checker validates file references and PDF presence; it does not prove flow completeness, architectural correctness or writing quality. Perform the content review separately and repair omissions before delivery.

Check the PRD against these failure modes: a stack copied from a reference project or beyond the team's maintenance capacity; a feature list with no end-to-end flow; permissions without server enforcement or record scope; a happy path without recovery; security adjectives without enforceable controls; duplicate events that repeat effects; billing changes without access behavior; unbounded paid workloads; a roadmap without observable acceptance checks; contradictory terminology or states; specific legal claims without verified basis; and open decisions hidden as settled facts.

Prefer tables for scope, permission matrices, decisions, risks, milestones and release gates when they improve comparison. Make the PDF readable as a standalone artifact with usable headings, page numbers and legible tables. Preserve an editable source for later revision.
