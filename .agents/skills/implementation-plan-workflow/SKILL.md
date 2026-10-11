---
name: implementation-plan-workflow
description: Turn an agreed PRD and available specs, designs, or code into phased slices covering features, environments, operations, required documents, and applicable commercial launch, with user review checkpoints. Use after PRD agreement or to maintain the plan during a build; not for PRD creation or project preparation.
---

# Implementation plan and workflow

Create a plan that another agent can follow without inventing product behavior, then maintain it as the build progresses. Phases group outcomes; slices are small, independently verifiable units of work. A slice can be documentation, dependency setup, a pilot, provider configuration, testing, backend work, UI work, or a combination. Choose size by a clear outcome and verification boundary, not a fixed duration or file count.

## 1. Ground the plan

Read the agreed canonical PRD, available specs/design references, and any existing agent instructions, plan, workflow rules, and source/configuration. Identify what exists, what is verified, and what is still planned. An agreed PRD is sufficient to start: a scaffold, context package, and workflow spec are not prerequisites for planning. Preserve an existing project's verified work. This skill works with `prd-creation` output or equivalent sources without requiring another skill to be installed.

Trace planned outcomes to agreed requirements and inventory user flows, modules, design sources, integrations, setup blockers, and release constraints. Preserve accepted product decisions and completed work. Resolve missing decisions that affect the next work with the user; represent later unresolved decisions as explicit blocked slices or decision tasks rather than inventing answers. Planning alone authorizes creating the planning documents, not executing the build or provisioning external resources.

Completion: the plan's source documents and current implementation are identified, and consequential uncertainties have an owner and effect on readiness.

## 2. Write phases and executable slices

Read [plan-contract.md](references/plan-contract.md) and [launch-readiness.md](references/launch-readiness.md) before creating or revising the implementation plan. Reuse an existing authoritative plan or create `docs/implementation-plan.md`, adapting to the project's layout. For a PRD-only start, create the plan in the agreed document location and mark future source/configuration paths as proposed. Update existing indexes when available; project preparation creates the full README and task-routed AGENTS.md later. Link only actual files.

Include project preparation as prerequisite work before feature implementation when context docs, workflow guidance, or a starter are missing. Specify its outputs: populated product-specific context docs, `docs/build-workflow.md` or an equivalent workflow spec, agent/index navigation, and a verified starter or explicitly chosen documentation-only handoff. `project-preparation` or equivalent preparation creates these outputs from the PRD and plan; this planning step does not create the workflow spec or scaffold. Record design sources/access and later input tasks without requiring all designs before planning.

Plan all agreed release work, including enabling tasks and applicable release checks. Keep the phase overview readable and each executable slice specific about inputs, actions, outputs, dependencies, and completion evidence. Later blocked slices may name unresolved inputs; resolve them before execution. Assign stable phase, slice, subslice, and checkpoint identifiers. Split a task when its instructions or completion boundary become ambiguous.

Cover applicable work through market/commercial launch, including staging/production setup, backup and demonstrated restore, error tracking, uptime monitoring, product analytics, privacy/data policies and compliance-document drafting/review/publication, customer/commercial readiness, and launch operations. Use the launch-readiness assessment to identify necessary additional work. Give setup/document tasks owners, environment/access dependencies, concrete outputs, and verification or review gates. Preserve the agreed endpoint for prototypes/pilots and label later launch work; tool examples are not mandatory supplier choices.

Make each UI flow visible by name in the plan. Identify the design input and how the agent will access it; pair UI work with its corresponding backend and integration work, as subslices or explicit dependent slices. Schedule a user preview checkpoint at every completed UI flow or module. Define what the user will try, mock fixtures, navigation, relevant states and edge cases, and the explicit approval gate.

Completion: every agreed requirement has planned work and verification, every flow/module has a review checkpoint, dependencies are coherent, and the next slice can be executed from its instructions. Deliver the plan path, first ready slice, and unresolved blockers. For a new PRD-only project, preparation is the next stage. When only planning was requested, stop here.

## 3. Follow the build loop when implementation is authorized

Read the current plan and build-workflow spec at the start of each feature-build session. If preparation is incomplete, carry out authorized preparation using `project-preparation` or equivalent work first; its own verification establishes the initial baseline. Feature work requires the workflow spec and relevant context/readiness inputs. Reconcile recorded status with actual files and verification evidence. Select the next ready slice whose prerequisites and earlier checkpoint gates are satisfied. Follow the workflow spec's design-input procedure: retrieve the relevant flow from an accessible linked design tool or use supplied material; ask the user for missing/inaccessible inputs before design-dependent work. Report the chosen slice and intended outcome, mark it in progress, implement its bounded work, and run its applicable checks.

Record outputs, commands/results, limitations, and the next action in the plan. Failed checks keep the slice unfinished; fix within scope or record a concrete blocker. Completed automated checks establish technical verification; checkpoints also require human approval. Continue through ready work within the user's authorized scope until a review gate, a blocker, or a user instruction requires pausing.

At each flow/module checkpoint, launch and verify an accessible working preview and show it to the user using the environment's available preview/browser tools. Supply its URL or local launch/access instructions and a short walkthrough. Use safe representative mock data, usable navigation, and the relevant states and edge cases specified in the plan. State which behavior is mocked and which is connected to real backend/provider functionality. Screenshots may supplement a working preview; they do not replace it. If the preview cannot be accessed or demonstrated, record the blocker and leave the checkpoint pending.

Incorporate feedback as tracked revision work, verify the changes, and show the updated preview. Obtain explicit user approval for the demonstrated version before closing the checkpoint and proceeding past its gate. Silence, elapsed time, and passing tests are not approval. While awaiting feedback or approval, pause build progression past that checkpoint; record the resume point and leave the preview accessible when feasible. A technically verified flow/module remains awaiting approval until the user approves it.

Completion: the current slice's evidence and status are accurate; any required checkpoint is either approved or clearly pending with its feedback, blocker, and resume point recorded.

## 4. Maintain the plan through change and handoff

Keep workflow rules in the project build-workflow spec, planned work and live progress in the implementation plan, and product behavior in its existing authoritative specs. Link rather than duplicate them. When requirements, design sources, dependencies, or feedback change, update affected slices and specs together. Preserve stable identifiers and approval history; mark replaced work superseded and reassess dependent work. Reopen affected review checkpoints if a revision changes previously approved behavior or invalidates demonstrated evidence.

Before ending a session, record the current slice/checkpoint, actual evidence, pending feedback or decisions, next ready action, and preview access details without credentials. On resumption, verify that approvals still apply to the current implementation. Installation success, mocks, and a running process establish only the boundaries actually checked. Close the release plan only when required work, user checkpoints, and applicable release gates are satisfied; disclose remaining external setup or accepted deferrals.
