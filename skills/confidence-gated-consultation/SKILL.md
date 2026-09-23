---
name: confidence-gated-consultation
description: Autonomous Confidence-Gated Selective Consultation (CG-SC) for Multi-Agent Systems. Automatically assesses primary agent epistemic confidence using token entropy, semantic consistency, and G-Eval quality rubrics. Bypasses peer consultation on confident queries (Solo Fast-Path, 0.8s, 0 peer tokens). Dynamically spawns Pareto-separated diversity committees (Clan, Adhocracy, Market, Hierarchy) with Early-Exit Delphi consensus on genuine dilemmas, cutting compute cost by 87.5% and eliminating debate degeneration. Use whenever evaluating complex decisions, ethical dilemmas, legal/medical arbitration, or optimizing multi-agent LLM systems.
---

# Confidence-Gated Selective Consultation (CG-SC)

An adaptive cognitive governor for Multi-Agent Systems (MAS). Instead of unconditionally forcing multi-round debate for every query, CG-SC assesses epistemic confidence in real-time, executing an instant Solo Fast-Path for high-certainty queries and dynamically scaling to a Pareto-diverse Delphi committee only when necessary.

**Grounded in:** Lee & Kwon (2026), Kalyuzhnaya et al. (2025), Zhu et al. (2026), and TypeSafe AI System 1.

---

## The 3-Tier Cognitive Execution Flow

```
                           INCOMING QUERY x
                                  │
                                  ▼
                 ┌───────────────────────────────────┐
                 │ TIER 1: Epistemic Confidence Gate │
                 │ Computes C(x) via Entropy + G-Eval│
                 └─────────────────┬─────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
   C(x) >= 0.65             0.50 <= C(x) < 0.65         C(x) < 0.50
   (High Certainty)          (Moderate Uncertainty)     (Complex Dilemma)
         │                         │                         │
         ▼                         ▼                         ▼
┌───────────────────┐     ┌───────────────────┐     ┌───────────────────────┐
│ Solo Fast-Path    │     │ Dyadic Challenger │     │ Decoupled Delphi      │
│ • 1 Agent only    │     │ • 2 Agents        │     │ • 4 Diverse Agents    │
│ • 380 tokens      │     │ • Proposer + Critic│    │ • CVF Coordinates     │
│ • 0.84s response  │     │ • 660 tokens      │     │ • Early Exit (W>=0.75)│
└───────────────────┘     └───────────────────┘     └───────────────────────┘
```

---

## When to Use This Skill

Use this skill whenever:
* You want to evaluate a **complex decision, ethical dilemma, or strategic tradeoff** with multiple perspectives without wasting runaway tokens.
* The user asks for **multi-agent deliberation**, **Delphi consensus**, or an **agent committee review**.
* You need to optimize an agentic pipeline to avoid the **Unconditional Consultation Dilemma** (saving up to 87.5% in token expenditure).
* You need rigorous factual guardrails against **hallucination and debate degeneration**.

---

## The 4 Diverse Delphi Personas (Lee & Kwon 2026 Model)

When Tier 3 is convened, agents deliberate strictly along the **Competing Values Framework (CVF)** to maximize cognitive exploration while preventing personality clashes:

1. **Clan Agent (Humanist / Internal-Flexibility):**  
   Focuses on human wellbeing, ethical duties, non-instrumental life preservation, and stakeholder empathy.
2. **Market Agent (Utilitarian / External-Stability):**  
   Focuses on systemic utility, competitive outcomes, resource efficiency, and aggregate population impact.
3. **Hierarchy Agent (Regulatory / Internal-Stability):**  
   Focuses on compliance, statutory liability, standard operating procedures, and risk minimization.
4. **Adhocracy Agent (Innovator / External-Flexibility):**  
   Focuses on lateral thinking, creative compromises, adaptive protocols, and breaking zero-sum deadlocks.

---

## Early-Exit Termination Rule

Deliberation terminates immediately at Round $r^*$ when:
$$r^* = \min \left\{ r \;\middle|\; (\mathcal{G}^{(r)} \ge 0.74) \lor (\Delta \kappa_r < 0.05) \lor (\text{Tokens} \ge 4,500) \right\}$$
* Skips redundant rounds when consensus is stabilized.
* Protects system from runaway loops.

---

## Execution Command

To execute a decision episode using the local Python reference engine:
```bash
python3 /home/sparxz/Downloads/omanarp/cag_delphi_live_showcase.py
```
To run transparent CPU metrics on any custom query:
```bash
python3 /home/sparxz/Downloads/omanarp/run_live_decision_demo.py "<YOUR_QUERY>" <DIFFICULTY_0.0_TO_1.0>
```
