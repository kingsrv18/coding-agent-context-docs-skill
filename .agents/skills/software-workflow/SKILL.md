---
name: software-workflow
description: Coordinate application discovery, PRD creation, implementation planning, and project preparation in order using the three focused skills. Use for an end-to-end idea-to-prepared-project workflow or resuming that workflow; use the individual skills for a single stage.
---

# Software workflow

Run the focused skills in order, carrying each stage's actual artifacts and accepted decisions into the next. This skill coordinates the handoffs; the stage skills own their detailed procedures and validation.

## Establish the starting point

Read the user's inputs and any existing project instructions, PRD artifacts, implementation plan, and preparation evidence. Identify the requested endpoint and earliest incomplete or stale prerequisite stage. Preserve usable existing work rather than regenerating it merely to run every stage. For a new application, the default endpoint is a prepared project with context docs, workflow guidance, and a verified starter. A request limited to requirements or planning ends at that requested stage.

Locate the three focused skills by name in the available skill catalog, or use the sibling entry points below when available. Read each skill and its applicable references when reaching that stage, resolving its resources relative to that skill's directory. If a required skill is unavailable, identify it and the installation needed; keep completed artifacts and stop the affected stage rather than silently substituting an abbreviated workflow. Install this coordinator alongside the three focused skills.

## Run the stages

| Order | Skill to read and follow | Inputs and completion boundary |
| --- | --- | --- |
| 1 | [prd-creation](../prd-creation/SKILL.md) | Start with the idea and supplied references. Complete discovery and owner decision confirmation, then create and visually review the editable PRD, PDF, and architecture artifacts. |
| 2 | [implementation-plan-workflow](../implementation-plan-workflow/SKILL.md) | Use the agreed canonical PRD and available specs/designs. Run its planning steps, producing phases, slices, dependencies, preparation work, applicable environment/operations/document/launch work, checkpoints, and readiness/blockers. A scaffold is not required. |
| 3 | [project-preparation](../project-preparation/SKILL.md) | Use that PRD and plan to create context docs, the design-and-build workflow spec, project navigation, and starter. Complete package checks, startup verification within stated limits, and disk/Git audit; record preparation evidence in the existing plan. |

Use one agreed output/project location through the stages. Carry real source paths and decision status forward; preserve canonical authority if preparation relocates artifacts. Present a short stage transition with completed outputs and the next outcome. A focused skill's stage-only handoff marks that stage complete; when the user requested the full workflow, continue to the next authorized stage.

Honor each stage's clarification, decision, and verification gates. Reuse applicable prior acceptance; do not add a separate coordinator approval ceremony. Continue across completed stages without asking permission again for already requested work. Pending owner decisions or failed mandatory checks remain unresolved; perform independent work where useful and record the blocked handoff. Never treat silence or elapsed time as acceptance.

Project preparation owns the generated workflow spec, including linked-design lookup or requests for missing flow designs, working demonstrations, feedback revisions, user approval checkpoints, and resumption rules. Keep detailed workflow procedures there and tasks/progress in the implementation plan.

## Finish or resume

Check that completed outputs agree, their links resolve, and readiness claims match performed checks. Deliver the PRD source/PDF, plan, project folder, and workflow-spec paths as applicable, with verified limits, unresolved setup/decisions, and the next ready action. Do not create a second coordinator plan or progress document: before the implementation plan exists, record the current stage and pending input in the handoff; afterward use the plan's preparation/progress and resume records.

On resumption, inspect actual artifacts and evidence before selecting the earliest stage needing work. If an upstream requirement changes, revise its authority and affected downstream plan/context together, preserving unrelated completed work and approval history.

The default workflow ends after project preparation. If the user also explicitly requests feature implementation, continue through `implementation-plan-workflow`'s authorized build loop using the prepared plan and workflow spec, preserving every applicable flow/module review gate. Preparation alone does not start feature development, provisioning, or publishing.
