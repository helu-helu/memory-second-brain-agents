# Feature Specification: Candidate Review Workflow

**Feature Branch**: `007-candidate-review-workflow`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Continue the second-brain plan after experience extraction by adding a governed workflow to review, approve, reject, and activate generated lesson and skill candidates."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Review Candidate State (Priority: P1)

As the user or an agent acting for the user, I want to inspect pending lesson and skill candidates with evidence, status, confidence, and warnings so I can decide what is safe to promote.

**Why this priority**: Extraction creates candidates, but the system is not trustworthy until unreviewed artifacts are easy to audit.

**Independent Test**: Given candidate artifacts, listing pending candidates shows their metadata and evidence without modifying any files.

**Acceptance Scenarios**:

1. **Given** one candidate lesson and one candidate skill, **When** the review list is requested, **Then** both appear with id, type, status, confidence, title/name, and evidence count.
2. **Given** an artifact that is already active or rejected, **When** pending candidates are listed, **Then** it is excluded unless all statuses are explicitly requested.

---

### User Story 2 - Approve or Reject Candidates (Priority: P2)

As the user, I want to approve or reject a candidate with a reason so durable memory changes only happen after an explicit lifecycle decision.

**Why this priority**: Candidate-only extraction needs a controlled transition path into approved memory or rejected memory.

**Independent Test**: A candidate can be approved or rejected by id, the artifact status changes, and a review decision record is created.

**Acceptance Scenarios**:

1. **Given** a candidate lesson, **When** it is approved with reviewer and reason, **Then** its status becomes approved and the decision record links to the artifact and evidence.
2. **Given** a candidate skill, **When** it is rejected with reason, **Then** its status becomes rejected and it remains outside active skills.
3. **Given** an active artifact, **When** approval is requested again, **Then** the system refuses the transition and records no duplicate approval.

---

### User Story 3 - Activate Approved Artifacts (Priority: P3)

As the user, I want to activate approved lessons and skills only after review so agents can safely use them as personal memory or reusable skills.

**Why this priority**: Approval and activation should be separate to keep review decisions reversible before agent-facing use.

**Independent Test**: An approved lesson can be activated in place, and an approved skill candidate can be copied into the active skill area while preserving provenance.

**Acceptance Scenarios**:

1. **Given** an approved lesson, **When** activation is requested, **Then** status becomes active and activation metadata is recorded.
2. **Given** an approved skill candidate, **When** activation is requested, **Then** an active skill folder is created and the original candidate remains traceable.
3. **Given** a candidate that has not been approved, **When** activation is requested, **Then** activation is refused.

### Edge Cases

- Candidate frontmatter is missing required fields.
- Candidate id is duplicated across lessons and skills.
- Review reason is empty.
- Status transition is not allowed for the current lifecycle state.
- Active skill destination already exists.
- Review record write fails after artifact update is attempted.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST list lesson and skill candidates with artifact id, type, path, status, confidence, title or name, evidence count, and last modified time.
- **FR-002**: System MUST support filtering review listings by status.
- **FR-003**: System MUST approve a candidate only from candidate or draft status.
- **FR-004**: System MUST reject a candidate only from candidate, draft, or approved status.
- **FR-005**: System MUST activate only approved artifacts.
- **FR-006**: System MUST refuse invalid lifecycle transitions without modifying the artifact.
- **FR-007**: System MUST require reviewer and reason for approve, reject, and activate decisions.
- **FR-008**: System MUST write a review decision record for every successful lifecycle transition.
- **FR-009**: Review decision records MUST include artifact id, artifact type, previous status, new status, reviewer, reason, timestamp, artifact path, and evidence links.
- **FR-010**: Active skill promotion MUST preserve the original candidate as provenance instead of deleting it.
- **FR-011**: Durable memory or skill artifacts MUST include provenance, status, confidence, scope, and version metadata when the feature creates or changes long-term artifacts.

### Key Entities *(include if feature involves data)*

- **ReviewableArtifact**: A lesson or skill candidate with lifecycle status and evidence.
- **ReviewDecision**: An audit record of an approve, reject, or activate transition.
- **LifecycleTransition**: A requested status change and validation result.
- **ActiveSkill**: A reviewed skill made available in the active skills area.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can list pending candidates and see enough metadata to choose a review action in under 10 seconds for 100 local artifacts.
- **SC-002**: 100% of successful approve, reject, and activate actions create a decision record.
- **SC-003**: 100% of invalid lifecycle transitions are refused without changing artifact status.
- **SC-004**: No candidate skill becomes active unless it first reaches approved status.
- **SC-005**: All generated review records remain readable as standalone files with source artifact links.

## Assumptions

- Review is local and personal-first; multi-user permissions are out of scope.
- The initial interface is a deterministic CLI/script that can later be wrapped by API/MCP.
- Candidate artifacts use Markdown with YAML frontmatter from previous features.
- Approved lessons may be activated in place; skill candidates are promoted by copying to an active skill folder.
