# Wetiko Safety for AI

**Purpose:** Offer AI developers, researchers, and communities a practical, vendor-agnostic framework to recognize, prevent, and remediate *wetiko-like* failure modes in socio-technical systems: projection loops, shadow amplification, scapegoating dynamics, and deceptive self-reinforcement.

> TL;DR: This repo treats *wetiko* as a metaphor for a convergent class of risks: collective delusion, blame externalization, and self-amplifying harm. We translate the metaphor into testable checks, guardrails, and incident playbooks.

## What’s inside
- **Policies**: Wetiko Risk Policy, Human-in-the-Loop, Compassion Protocol.
- **Tooling**: Simple static rules (`wetiko_scan_rules.yaml`), self-test harness, red-team prompts, eval runner.
- **Docs**: Glossary, red-team prompts, countermeasures, case studies, implementation checklists, research agenda, ethics & governance, FAQ.
- **GitHub glue**: Incident report template + CI to run basic scans.

## Quick start
```bash
# 1) Run static rule scan on prompts & policies
python3 tests/evals/run_eval.py --scan

# 2) Run dynamic self-test (heuristics + assertions)
python3 src/tooling/wetiko_self_test.py

# 3) Evaluate red-team prompts against your model endpoint (stub provided)
python3 tests/evals/run_eval.py --model-endpoint http://localhost:8000/infer
```

## Scope
- We **do not** diagnose humans; we analyze artifacts (prompts, policies, outputs, training data) for patterns indicative of projection, othering, dehumanization, and denial-of-agency.
- We **assume pluralism**: multiple worldviews can align on the same safety invariants (dignity, reciprocity, transparency, corrigibility).

## Contribute
See [CONTRIBUTING.md](CONTRIBUTING.md). Code of conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
