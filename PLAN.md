# Plan

## Objectives (per PRD)
- Web app that helps couples interpret emotional/psychological changes together during pregnancy and postpartum.
- Reduce misinterpretation of emotional changes as lack of care or relationship failure via a shared framework.
- Provide neutral, non-judgmental individual reflection spaces with regular depression screening to surface early signals.
- When risk is detected, enable a group conversation supported by an AI counselor (and optional therapist) using non-clinical language and strong privacy.

## Non-Goals (per PRD)
- No diagnosis, treatment, or crisis intervention.
- Not a replacement for therapy or medical care; no deep relationship counseling.
- No prescriptive behavioral advice; output is understanding, not action plans.

## Audience
- Primary: Couples in pregnancy/postpartum experiencing emotional or relational strain who want clarity and mutual understanding.
- Secondary: Therapists who join occasionally (when risk is flagged) to facilitate shared understanding alongside the AI counselor.

## Constraints
- MVP is web-based.
- Each partner uses a private chat flow individually.
- Regular depression screening for each partner; monitored over time; strictly non-diagnostic language.
- Escalation is triggered and occasional (AI counselor-led, therapist optional), not continuous.
- High standards for privacy, neutrality, and emotional safety.

## Key Use Cases to Deliver
- Individual emotional reflection by each partner with contextualized prompts.
- Regular depression screening and monitoring over time.
- Interpretation of emotional changes with a shared framework and summaries to restore alignment after misalignment.
- Detection of emotional risk or depression signals.
- Escalation to a group chat supported by an AI counselor (therapist involvement when indicated).

## Scope (MVP)
- Partner account/linking with private chat experiences and empathetic, neutral prompts.
- Screening scheduler and delivery for each partner; risk flagging (non-diagnostic) with longitudinal view.
- Shared interpretive summaries/mental models to reduce misinterpretation (clarity, not advice).
- Escalation workflow into an AI counselor-supported group chat, with optional therapist view/participation and necessary context.
- Privacy/consent flows and language safeguards to keep interactions neutral and non-clinical.

## Out-of-Scope (MVP)
- Emergency/911-style workflows or live crisis support.
- Continuous therapist involvement outside triggered sessions.
- Prescriptive behavioral or relationship advice; deep counseling features.

## Success Criteria
- Partners report clearer mutual understanding and fewer misinterpretations (>75% positive surveys).
- Regular screenings completed weekly by both partners (>70% adherence).
- Faster recovery of shared understanding after misalignment (self-reported 30% improvement).
- Reliable escalation flow into AI counselor-supported group chat; therapist joins when flagged; privacy upheld.

## Milestones & Deliverables
- M0: Requirements/PRD alignment finalized (current state).
- M1: Experience map + IA for individual chat, screening cadence, shared summaries, risk detection, and escalation.
- M2: Content guidelines (neutral, non-clinical) + UX prototypes for chat, screening, shared summaries, and AI counselor/therapist entry.
- M3: Technical spike for secure chat, screening delivery, risk flagging, AI counselor orchestration, and privacy/safety controls.
- M4: MVP build: auth + partner linking, private chats, screening scheduler, interpretive summary generator, risk-triggered AI counselor group chat, therapist access path.
- M5: Safety/privacy review; red-team non-clinical language; AI counselor prompt/policy hardening; therapist workflow polish.
- M6: Pilot (5–10 couples, 1–2 therapists); capture adherence, clarity, trust, and escalation latency; iterate post-pilot.

## Workstreams
- Product/UX: Flows for individual chats, screening cadence, shared summaries, and escalation.
- Content/Behavioral: Non-judgmental prompts, shared emotional language, non-clinical phrasing.
- Data/Safety: Screening logic, risk thresholds (non-diagnostic), privacy/consent, auditability.
- Engineering: Web app, auth + partner linking, chat infra, scheduler/notifications, risk detection, escalation routing, AI counselor integration, therapist view.
- Therapist/AI Counselor Experience: Lightweight console for context and group chat participation within triggered sessions; AI counselor prompt/policy management.

## Risks & Mitigations
- Perception of diagnosis → Strict non-clinical language, disclaimers, content reviews.
- Low screening adherence → Low-friction prompts/reminders; flexible timing.
- Privacy/trust concerns → Transparent consent, data minimization, access controls.
- Therapist availability when needed → Scheduled on-call windows; async intake while waiting; AI counselor handles first contact.
- AI counselor missteps or harmful responses → Policy/prompt hardening, red-teaming, fallback escalation to human reviewer in pilot.
- Misaligned summaries causing harm → Conservative summarization; human-in-the-loop during pilot.

## Metrics (early)
- Adoption: Linked partner accounts; onboarding completion.
- Engagement: Weekly screening completion per partner; chat sessions per week.
- Understanding: Clarity/misalignment scores; reduction in “misunderstood” reports.
- Safety: Risk flag rates, false positives/negatives (qualitative in pilot), escalation latency to AI counselor and therapist.

## Pilot Plan
- Recruit 5–10 couples (first-time parents with reported emotional disconnect) and 1–2 therapists.
- Run 4–6 weeks with weekly screenings and shared summaries; track misalignment recovery.
- Trigger therapist group chat on risk flags; measure latency and satisfaction.
- Post-pilot debrief on clarity, safety, and trust before scaling.
