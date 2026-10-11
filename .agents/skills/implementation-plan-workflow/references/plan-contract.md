# Plan and project workflow contract

The implementation plan tells the agent what to do next and owns live progress. Project preparation subsequently creates the design-and-build workflow spec defining how agents follow the plan, acquire design inputs, and conduct reviews. Both remain usable without installed skills; planning itself requires only the agreed PRD and available inputs.

## Implementation plan

Start with the release goal, authoritative source links, current implementation baseline and verified limits, followed by a phase/slice overview. Show stable IDs, outcomes, dependencies, status, and checkpoints in a compact table or equivalent navigable structure. Include a flow/module-to-slice-and-checkpoint mapping so UI delivery and module reviews are visible without reading every task. Identify applicable release work such as integration verification, migration or deployment readiness from the actual product risks.

Each phase names its outcome and exit conditions. Each executable slice contains:

| Field | Required substance |
| --- | --- |
| ID and outcome | Stable identifier, work type, and one bounded observable result. |
| Requirement and scope | Source requirement/spec links, exact behaviors or artifacts covered, and a boundary where confusion is likely. |
| Inputs and readiness | Prerequisite slice/checkpoint IDs, relevant files/contracts, design source/access method, configuration or user decisions needed. |
| Actions | Concrete ordered work, including relevant screens, transitions, business rules, integration boundaries, or setup operations. Reference authoritative details instead of repeating them. |
| Outputs | Expected artifacts or behavior and target locations grounded in the project; distinguish proposed paths from existing files. |
| Verification | Applicable commands or procedures, fixtures/scenarios, expected results, and evidence needed to prove the outcome. Determine actual stack commands before execution when initialization is still pending. |
| Review gate | Associated checkpoint ID and what must be approved, or a link to the containing flow/module checkpoint. Non-UI module checkpoints demonstrate the observable module result. |
| Progress | Current status, evidence/limitations, blockers, and next action; initially planned and unverified. |

Subslices have their own outcomes and checks when they are independently tracked. A parent completes only when required children and its checkpoint are complete. Keep a single canonical progress record for each ID.

Avoid tasks such as "build frontend" or "implement backend" without named behavior. Split shared UI foundations from named user flows; foundations support the flows rather than replacing their slices. For every flow, show its UI work, corresponding backend behavior, integration, and review dependencies. A mock UI review can occur before real backend integration if the plan explicitly names that milestone and schedules a later connected-flow review. Mock approval does not approve an unshown real integration.

### Example: onboarding with UI first

Adapt this shape to the product rather than prescribing this order for every flow:

| ID | Outcome | Depends on | Completion |
| --- | --- | --- | --- |
| S-01 | Prepare context docs, workflow spec, project navigation, and the starter. | Agreed PRD and implementation plan | Preparation evidence recorded; executable readiness verified before dependent feature work. |
| S-02 | Confirm onboarding design inputs, screen order, and field rules from the linked design/spec sources. | S-01 and agreed onboarding scope | Sources accessible and consequential gaps resolved. |
| S-03 | Build onboarding UI with deterministic fixtures, navigation, and agreed state/edge-case demonstrations. | S-02 and needed UI foundations | UI checks pass; CP-01 pending. |
| CP-01 | User tries onboarding UI and approves its demonstrated version. | S-03 | Feedback resolved and explicit approval recorded. |
| S-04 | Implement onboarding persistence and access/validation rules from the domain/API specs. | CP-01 and required data/provider setup | Boundary checks prove save, retrieval, and relevant rejection/failure cases. |
| S-05 | Connect onboarding UI to that backend and verify the complete journey. | S-04 | Integration checks pass; CP-02 pending. |
| CP-02 | User tries the connected onboarding flow with safe test/mock fixtures. | S-05 | Feedback resolved and explicit approval recorded; flow complete. |

UI and backend may instead be subslices of a single flow slice. Their dependencies and checkpoint still need to be explicit. Each other completed module receives its own checkpoint, or shares a checkpoint that explicitly covers it and its approval.

## Preparation dependency and progress

For a project without a prepared baseline, include a preparation slice before feature work. Its outputs are context docs, the design-and-build workflow spec, agent/index navigation, and verified scaffold readiness or an explicitly chosen documentation-only handoff. Require initialization before dependent executable work in the latter case. Proposed locations and checks remain planned until preparation determines actual files and commands. Existing prepared projects can satisfy this dependency with verified evidence.

Name the expected workflow-spec location as a preparation output without linking a nonexistent file. Project preparation authors its procedures from the plan and product sources, including relevant linked-design lookup, user requests for missing flow designs, working demonstrations, feedback/approval gates, and session resumption. The plan supplies IDs, dependencies, checkpoint scopes, and progress records; it does not duplicate the workflow spec's procedure text.

Default slice states are `planned`, `ready`, `in-progress`, `blocked`, `awaiting-approval`, `complete`, and `superseded`. Existing project states can be retained if they distinguish technical verification from human approval. A slice becomes ready when its required inputs, predecessor work, and earlier approval gates are satisfied. A verified slice with a required checkpoint enters awaiting-approval. Complete requires its checks and applicable approval. Blocked records the reason, responsible party, and condition for resumption.

Keep checkpoint states `pending`, `in-review`, `changes-requested`, and `approved`, or equivalent existing states. Feedback creates concrete revision tasks linked to the checkpoint; the checkpoint returns to review only after the revised preview and checks are ready. Record user-approved deferrals explicitly and ensure they do not hide a requirement essential to the shown flow or release.

## Review checkpoint contract

Each checkpoint specifies the flow/module and slice IDs it covers, prerequisite checks, working preview access, navigation/walkthrough, representative fixtures, relevant states and edge cases, and approval criteria. For a non-UI module, expose the result through a working product view when applicable; otherwise use a runnable API, CLI, or other appropriate demonstration. Identify mock and real boundaries in either case.

Select cases from the product rules and risks. For example, onboarding may need invalid fields, duplicate identity, expired invitation, denied access, retry after network failure, repeated submission, and resumed partial progress. Include loading, empty, error, and success states where meaningful. Justify a state as not applicable instead of constructing unrelated states. Make important cases reproducible using fixtures or an appropriate local/test mechanism; keep demonstrations out of production user flows unless the product actually requires them.

Record the demonstrated revision (commit or equivalent identifiable snapshot), environment, verification results, preview access and demonstration date, unresolved limits, feedback, revision work, and the user's explicit approval of that version/scope. Store an accurate short approval record with its source conversation/date; never manufacture an approval or require a special phrase. User requests that change behavior are feedback unless they clearly approve the relevant scope. Ask only when the approval's scope is ambiguous.

## Resume and change control

Keep a concise resume entry in the plan: active slice/checkpoint, last verified result, pending decisions/feedback, next action and readiness, and preview launch/access instructions. Check actual files and evidence before trusting old status. If a source or implementation changed since approval, identify affected slices and reopen the relevant checkpoint when its approval no longer covers the behavior. Preserve prior approval and evidence as history.

For inaccessible designs, identify the missing source and ask for accessible material or an explicitly accepted alternative before design-dependent work. For external setup, record required access, owner, safe configuration names, and a verification step without secrets. Perform setup only within user authorization; pending provisioning or payment keeps dependent work blocked. If checks or preview tools are unavailable, report what remains unverified and keep the corresponding gate open.

## Plan validation before handoff

Check requirement coverage, named UI-flow coverage, module checkpoints, unique IDs, resolving existing document/ID references, dependency order without cycles, approved-gate placement, concrete completion evidence, and honest baseline/progress claims. For a PRD-only start, verify that preparation precedes feature work and future files are named outputs rather than broken links. Walk through the next slice using its available sources to confirm another agent can execute it. Once preparation exists, verify that project agent instructions route build/resume work to both workflow and plan documents. Report blockers rather than claiming every slice is ready.
