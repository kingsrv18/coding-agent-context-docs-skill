# Design-and-build workflow handoff

Project preparation creates this project spec from the agreed implementation plan, PRD, relevant product specs, and actual scaffold. It explains how an agent follows the plan and works with the user. The implementation plan remains authoritative for phases, slices, dependencies, checkpoints, progress, evidence, feedback, and approval history.

## Create the project spec

Reuse an existing authoritative workflow document or create `docs/build-workflow.md`. Populate it with project-specific conventions so another coding agent can follow it without any skills installed. Link the actual plan, product/technical specs, design sources, and preview/setup instructions. Keep product-specific screen and state rules in their UI/domain authority and reference them.

Explain preparation versus feature implementation and the verified baseline. Record actual preview commands, provider/mock boundaries, safe fixtures, approval ownership, and known access/setup blockers. Preserve unknowns as explicit inputs needed before dependent work.

## Follow the plan and obtain design inputs

At each session, read project agent instructions, current plan, workflow spec, and the relevant source docs. Check actual files and verification evidence before trusting recorded progress. Select the next ready slice or flow whose dependencies and previous approval gates are satisfied.

For design-dependent work, locate the relevant named flow/module in the plan and its linked design source. If a linked design tool is accessible, inspect the relevant frames, screens, transitions, components, and states directly through available tools. Use existing supplied design material when it covers the flow; avoid asking the user to resupply accessible inputs. Record the source/version or frame identity used.

If the relevant flow is missing, unclear, or inaccessible, ask the user to provide the next flow's design/screens or accessible tool link, or resolve the specific gap. Leave design-dependent work blocked until the input or an explicitly accepted alternative is available. Do not invent an approved design. Apply this design step to work that needs it; setup, backend-only work, and non-UI modules use their applicable contracts.

## Implement, verify, and review

Mark the selected work in progress, read its inputs, implement the bounded slice, and run its planned checks. Failed checks keep the work unfinished. Record actual outputs, verification commands/results, limitations, blockers, and next action in the implementation plan.

At each completed UI flow or module checkpoint, launch and verify an accessible working demonstration and show it to the user. Provide preview access and a short walkthrough, with safe representative mock/test data, usable navigation, and relevant states and edge cases. Screenshots supplement the demonstration. Non-UI modules use a working product view, runnable API, CLI, or other appropriate demonstration. Identify what is mocked and what is connected; mock approval does not approve an unshown real integration.

Ask the user to review the demonstrated flow/module. Record feedback as concrete revision work linked to its checkpoint, implement and verify revisions, then show the updated demonstration. Obtain explicit approval of the demonstrated version and scope before closing the checkpoint and advancing past its gate. Passing tests, silence, or elapsed time do not establish user approval. An inaccessible preview leaves the checkpoint pending with its blocker.

## Progress and resumption

Use the plan's stable identifiers and conventions. Distinguish planned, ready, in-progress, blocked, awaiting-approval, complete, and superseded work, and pending, in-review, changes-requested, and approved checkpoints, or the project's equivalent states. Readiness requires inputs, predecessor work, and earlier approvals; completion requires technical checks and applicable user approval.

Keep one progress record per ID in the plan. Record checkpoint scope, demonstrated revision/environment/date, verification and preview access, limitations, feedback/revisions, and explicit approval with its source conversation/date. Preserve earlier records as history. Store no credentials in access details.

Before ending a session, record the active slice/checkpoint, last verified result, pending decisions/feedback, next action/readiness, and preview launch/access details. Pause progression past pending review gates and keep the preview accessible when feasible. On resumption, verify that prior approvals cover the current implementation.

When requirements, designs, or implementation change, update affected authoritative specs and plan work together; reopen checkpoints when prior approval no longer covers the behavior. Resolve consequential contradictions with the owner. External provisioning stays within user authorization; unavailable checks, design access, or provider setup remain concrete blockers rather than claimed evidence.

## Navigation and handoff checks

Route building, verification, review, and resumption from `AGENTS.md` to both the existing implementation plan and workflow spec. Explain the three-stage handoff in `README.md`. Link actual files rather than future nonexistent paths.

Before handoff, check that named flows/modules and gates match the approved plan, linked specs exist, design-access instructions cover accessible and missing inputs, demonstrations and approval rules cover UI and non-UI work, and readiness claims match performed checks. Record preparation results and the next ready action in the plan. This spec owns procedures, not a duplicate task list or progress record.
