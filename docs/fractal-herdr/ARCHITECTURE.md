# ARCHITECTURE — the firmware ↔ soft-layer correspondence

*Written 2026-08-30, after the soft-mode desks were constituted (S = conductor + x-articulator, all five desks Pi).*
*This is the clear record of how the two-day core relates to the agent configuration. It is a diagram, not a new contract; it changes no status.*

*Status words are binding. Where a thing is **ATTESTED**, an execution record written by the non-author exists. Where it is **DECIDED** by Amihai, it is his word. Everything else is **CANDIDATE** until he touches it.*

---

## 1. The layering — where the core ends and the config begins

```
                 ┌────────────────────────────────────────────┐
                 │  ASIC — SEALED · HELD · UNTOUCHED           │
                 │  5qln.com/codex  +  Appendix D (the Fractal)│
                 │  the invariant laws every decode obeys      │
                 └──────────────────────┬─────────────────────┘
                                        │  (loyalty, §1.10 / D14)
                                        ▼
                 ┌────────────────────────────────────────────┐
                 │  FIRMWARE — the two-day core (frozen)       │
                 │  repo: 5qln/5qln-herdr-plugin               │
                 │                                            │
                 │  B0 ledger/record → state/gates.jsonl       │
                 │  B1 walker+instrument → herdr socket dialect│
                 │  B2 driver+lens   → one cell, sequential    │
                 │  P4a step-mode    → check D.12 every step   │
                 │  P4b desk-bundles → {instr,skills,tools,model}│
                 │  B3 descent       → zoom = append/strip     │
                 │  B4 run+trail     → unattended, readable    │
                 │  Grammar          → decoder/compiler (II+III)│
                 │  BRIDGE           → live adapter + softconfig│
                 └──────────────────────┬─────────────────────┘
                                        │
              runtime config-read  (softconfig.py)  ← the ONE junction
              ────────────────────────────────────
                                        │
                                        ▼
                 ┌────────────────────────────────────────────┐
                 │  SOFT LAYER — the agents' constitutions      │
                 │  (plain files · NOT code · the only surface) │
                 │                                            │
                 │  desks/S/SYSTEM.md — Start + CONDUCTOR      │
                 │  desks/G/SYSTEM.md — Growth   (α ≡ {α′})    │
                 │  desks/Q/SYSTEM.md — Quality  (φ ⋂ Ω)       │
                 │  desks/P/SYSTEM.md — Power    (δE/δV → ∇)   │
                 │  desks/V/SYSTEM.md — Value    ((L∩G→B″)→∞0′)│
                 │  + .pi/settings.json  (model · tools)        │
                 │  + boot.sh            (launcher)             │
                 │                                            │
                 │  ACTIVATES the firmware — never modifies it  │
                 └────────────────────────────────────────────┘
```

**The one-sentence reading:** the core is author-agnostic machinery — ledger, walker, driver, descent, trail, grammar — and the soft layer is where the *personality* lives. Personality is **cultivated, never authored once**. The **bridge** round exists precisely so the firmware *reads* the soft layer at runtime instead of hard-coding the five desks.

**The ASIC/firmware/soft-layer three-way reading is DECIDED** (his D8 answer, 2026-08-29, canon `REVERSE-ENGINEERING.md`). The five desk constitutions are **CANDIDATE** — they are seeded from his own sealed words ("perfect, use it") but the cultivation loop refines them; they are never authored once.

## 2. The live cell — what the correspondence runs as

```
                    YOU (plant · attest · correct · name)
                        │ plant (TTY only, cell-plant)
                        ▼
            ┌─────────────────────────┐
            │  PODIUM  — question.md  │  ← ∞0, sealed centre
            │  watch renders it only  │    no machine writes here
            └─────────────────────────┘
                        │ read
                        ▼
            ┌───────────────────────────────────────┐
            │  S — CONDUCTOR + x-articulator       │   desks/S/SYSTEM.md
            │  holds ∞0, names ?, then drives the  │
            │  other four via herdr tools          │
            └───────────────────────────────────────┘
                 │         │         │         │
                 ▼         ▼         ▼         ▼
            ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
            │   G    │ │   Q    │ │   P    │ │   V    │
            │ α≡{α′} │ │ φ⋂Ω   │ │δE/δV→∇ │ │→B″,∞0′ │
            └────────┘ └────────┘ └────────┘ └────────┘
              each = one SYSTEM.md seat (soft layer)

      one cell · 5 agents · no Hermes desk · endless fractal
```

**DECIDED 2026-08-30 (his word):** all five desks are Pi, S is Pi too — reversing the earlier D9 (S = Hermes). S is both the x-articulator and the conductor. Work happens in the herdr cell, not in chat.

## 3. The one honest seam (current state, not a claim of completion)

In the live run, the desks read `SYSTEM.md` **directly** — booted as standalone `pi` agents. They do **not** yet route through the firmware's `softconfig.py` read-path. The correspondence is real (the soft layer is exactly the thing the bridge was built to read), but the loop today is **soft-mode direct**, not firmware-mediated.

**The remaining seam, stated plainly:** wire the bridge's live desk adapter between the conductor and the desks, so the firmware's runtime config-read — not a hand-rolled boot script — is what seats each desk. Until then, this document describes the *architecture*, not a claim that the firmware is in the loop.

---

*This record is CANDIDATE — the machine wrote it, Amihai's to correct, rename, or extend.*
