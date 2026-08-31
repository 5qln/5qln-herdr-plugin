---
title: "Fractal Herdr — Architecture (the firmware ↔ soft-layer correspondence)"
created: 2026-08-30
entry_type: architecture
status: "CANDIDATE — the machine wrote it; Amihai's to correct, rename, or extend. Status words are binding: ATTESTED needs a non-author execution record; DECIDED is his word; everything else is candidate."
canon_home: "5qln/5qln-herdr-plugin — docs/fractal-herdr/ARCHITECTURE.md (canon; every other copy is a mirror)"
---

# ARCHITECTURE — the firmware ↔ soft-layer correspondence

*Written 2026-08-30, after the soft-mode desks were constituted (S = conductor + x-articulator, all five desks Pi).*
*This is the clear record of how the two-day core relates to the agent configuration. It is a diagram, not a new contract; it changes no status.*

*Status words are binding. Where a thing is **ATTESTED**, an execution record written by the non-author exists. Where it is **DECIDED** by Amihai, it is his word. Everything else is **CANDIDATE** until he touches it.*

---

## 1. The layering — where the core ends and the config begins

```
                  YOU — plant · attest · correct · name
                       │   (TTY only · cell-plant / cell-attest)
                       ▼
        ┌────────────────────────────────────────────────┐
        │  PODIUM — the formation train (READ-ONLY)      │
        │  his acts + the desks' events, one chain:      │
        │  plant → S → gate x → … → ∞0′ → plant          │
        └────────────────────────────────────────────────┘

   HARD CORE — sealed · frozen · attested      SOFT CORE — plain files · cultivated
   ┌──────────────────────────────────────┐   ┌──────────────────────────────────────┐
   │  ASIC · the Codex + Appendix D       │   │  desks/{S,G,Q,P,V}/ — SYSTEM.md       │
   │         held · hashed · pinned       │   │   + AGENTS.md · .pi/settings.json     │
   │              │  (loyalty · D14)      │   │   + skills · prompts · scenarios      │
   │              ▼                       │   │   + soft.json (budget/hold/poll)      │
   │  FIRMWARE · the engine               │   │                                      │
   │   B0 ledger · B1 walker · B2 driver  │   │  ACTIVATES the firmware —             │
   │   step-mode · bundles · B3 descent   │   │  NEVER modifies it                    │
   │   B4 run · Grammar · bridge · R06    │   │                                      │
   └───────────────────┬──────────────────┘   └───────────────────┬──────────────────┘
                       │                                          │
                       │        THE SEAM — two directions          │
                       │   ┌────────────────────────────────────┐  │
                       │   │  firmware READS soft core          │  │
                       │   │   (softconfig.py · read_materialized)│ │
                       │   │  soft core INVOKES firmware        │  │
                       │   │   (/conduct /word /plan /materialize│ │
                       │   │    /config /states /trail /descent) │ │
                       │   │   → points only · never drives      │  │
                       │   └────────────────────────────────────┘  │
                       │                                          │
                       │  B2 Instrument — the ONE wire path        │
                       │  (agent.prompt = the only write, frozen)  │
                       ▼                                          │
   ┌────────────────────────────────────────────────────────────────────────────┐
   │  HERDR — the cell substrate                                                  │
   │  herdr.sock · the-cell (6 panes) · plugin cell.fiveqln                       │
   │  ledger gates.jsonl · trail · plant/attest TTY guards                        │
   └───────────────────────────────────────┬───────────────────────────────────────┘
                                           │  agent.prompt → pane.wait_for_output(⟦END …⟧)
                                           ▼
   ┌────────────────────────────────────────────────────────────────────────────┐
   │  PI — the five desks, seated in herdr panes                                  │
   │  S (conductor + x-articulator) · G · Q · P · V                                │
   │  ONE cell, always — zoom = rename, never pane split                          │
   └────────────────────────────────────────────────────────────────────────────┘
```

*The invocation seam above (`/conduct` etc.) is built and attested — R07 integration, 2026-08-31, "attest it". The live drive through it is still pending; §3 states both halves plainly.*

**The one-sentence reading:** four actors. The **hard core** is author-agnostic machinery — the ASIC (codex, held) + the firmware (ledger, walker, driver, descent, run, grammar, bridge, orchestration). The **soft core** is where the *personality* lives — the five desk constitutions — **cultivated, never authored once**. The **herdr** cell is the substrate that seats the desks and carries the run; the **Pi** desks are the five seats. Two channels join hard and soft: the firmware *reads* the soft core at runtime (`softconfig.py`), and the soft core *points* at the firmware through slash commands — never holding driving logic. That second channel is the attested integration seam (R07, 2026-08-31).

**The ASIC/firmware/soft-layer three-way reading is DECIDED** (his D8 answer, 2026-08-29, canon `REVERSE-ENGINEERING.md`). The five desk constitutions are **CANDIDATE** — they are seeded from his own sealed words ("perfect, use it") but the cultivation loop refines them; they are never authored once.

## 2. The live cell — what the correspondence runs as

```
                 YOU (plant · attest · correct · name)
                      │ plant/attest (TTY only · cell-plant / cell-attest)
                      ▼
        ┌─────────────────────────────────────────────┐
        │  PODIUM — the formation train  (READ-ONLY)  │
        │  one interleaved chain, human + desks:      │
        │  plant → S's turn → gate x → … → ∞0′ → plant│
        └─────────────────────────────────────────────┘
                      │ read
                      ▼
        ┌─────────────────────────────────────────────┐
        │  S — CONDUCTOR + x-articulator  desks/S/    │
        │  holds ∞0, names ?, drives the walk         │
        │  (conduction = call /conduct — never        │
        │   re-derive the walk)                       │
        └─────────────────────────────────────────────┘
               │         │         │         │
               ▼         ▼         ▼         ▼
        ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
        │   G    │ │   Q    │ │   P    │ │   V    │
        │ α≡{α′} │ │ φ⋂Ω   │ │δE/δV→∇ │ │→B″,∞0′ │
        └────────┘ └────────┘ └────────┘ └────────┘
          each = one SYSTEM.md seat (soft core)

   one cell · 5 agents · all Pi · ONE cell always — zoom = rename, never pane split
```

**DECIDED 2026-08-30 (his word):** all five desks are Pi, S is Pi too — reversing the earlier D9 (S = Hermes). S is both the x-articulator and the conductor. Work happens in the herdr cell, not in chat. **DECIDED 2026-08-31 (his word):** the podium is the formation train — read-only (§4.1) — and the cell never spawns a pane: descent renames, it does not split (§4.2).

## 3. The one honest seam (current state, not a claim of completion)

The seam itself is now **built and attested** (R07 integration, 2026-08-31, "attest it"): `cellctl` — the thin, logic-free slash commands over the engine — with the enforcement suite proving "no driving logic in the soft layer" as a structural, mechanically-checkable fact. The first channel in the diagram above (the soft core *invokes* the firmware through slash commands) is therefore **real code, not a proposal**.

What is still **direct** — stated plainly, never claimed done — is the **live drive**:

- The desks still boot **soft-mode direct**: they read `SYSTEM.md` standalone and do **not** yet route through the firmware's `softconfig.py` read-path, and no live desk speaks its §3.6 surface yet (H-INT-5, W3).
- The improvised tooling the enforcement suite *caught* — the desks' `herdr_send_prompt` guides, the plugin's `_cell_api.py` socket client — is not yet retired or re-pointed onto `cellctl` (L1/L2 findings, W3/W5).
- The first real `/conduct` over the five desks — the paid turn deferred since the bridge — is Amihai's alone to authorize (H-INT-1, W4).

So the diagram above is the *architecture*: the firmware is in the loop for the invocation seam, and the live desks are not yet driven through it. Both halves are stated, neither is papered over.

## 4. Two interface decisions (2026-08-31, his word)

1. **The podium becomes the membrane's formation train — a ledger index, not a dashboard.** The podium
   panel "made no sense" as it was (his word, 2026-08-31): it is repurposed into the **smart log
   attestation of the membrane**. It logs the five desks' (S/G/Q/P/V) total activity as a running ledger
   — the **fractal formation train at membrane level**, human and AI activities interleaved as one chain:
   his plant/attest/correct/name on the ∞0 side, the desks' decode/compile/gate/hold on the K side
   (`plant → S's turn → gate x → … → attestation → fruit → ∞0′ → next plant`). It is the membrane's
   attestation of the **flow** — if it does not do that, it has no reason to exist. The alternative — a
   full dashboard for orchestration settings — is ruled out (too big a scope; agreed).

   Two boundaries, both already drawn by the built firmware:
   - **Events level, not the raw thread.** Each desk's turn is *one* event (what it decoded to, what gate
     it produced) — never the agent's internal transcript. The raw stays inside each desk's pane; the
     formation trail records events by design (D12: what the context decoded *to*, never the context
     itself).
   - **Read-only.** The seal holds — no machine write path to the centre. The podium *reads* the flow;
     plant/attest stay human TTY acts.

   **The use (critical):** the train is how we **learn which orchestration methods work and which don't**
   — which pattern, sign-walk, or scenario word closed honestly, held honestly, returned a live ∞0′ — so
   the winners get built as **new skills, tools, recipes** and fed back into the soft layer (D8, "output
   is input," at the orchestration level: the soft layer grows *out of* the runs). The recording already
   exists (trail events, holds, attested gates, ∞0′); the learning layer on top of it is **not yet
   built**. The visual rendering is **open** — pending Amihai's herdr GUI / look-and-feel research (in
   progress, 2026-08-31).
2. **One cell, always.** Zoom (descent) never spawns a pane: the seats re-form as the child cell — the same
   4+1, tagged by address, coloured by depth. Descend by rename, never by `pane split`. (This names the
   cause of the 2026-08-30 descent's window multiplication: spawned panes, not a navigated cell.)

## 5. The four actors — how they speak (one line each)

| Actor | What it is | How it speaks |
|---|---|---|
| **HARD CORE** | ASIC (the Codex + Appendix D, held · hashed · pinned) + the firmware (the engine — B0–B4, step-mode, desk bundles, descent, run, Grammar, bridge, R06 — sealed, attested) | READS the soft core at runtime (`softconfig.py` · `read_materialized`); drives the desks through the ONE wire path (B2 `Instrument` — `agent.prompt` is the only write, frozen) |
| **SOFT CORE** | the plain-file constitutions (`desks/*/SYSTEM.md`, `AGENTS.md`, `.pi/settings.json`, skills, prompts, scenarios, `soft.json`) | POINTS at the engine through slash commands (`/conduct /word /plan /materialize /config /states /trail /descent`) — never holds driving logic |
| **HERDR** | the cell substrate — socket, panes, plugin (`cell.fiveqln`), ledger, trail | carries the engine's `agent.prompt` to the desks and the desks' output back to the `⟦END …⟧` fence; plant/attest stay human-TTY |
| **PI** | the five desks S·G·Q·P·V, seated in herdr panes, one cell always | answers through its §3.6 surface; descent = rename, never pane split |

**The rule the seam enforces:** the soft core may *point* at the engine and *supply data* to it; it may never *drive* a desk itself. The only thing that ever sends `agent.prompt` is the firmware, and every prompt is provably the engine's (the sender audit in `verify-integration.sh`). Both writers of the soft core — Amihai by hand (developer mode) and Hermes from his intent (usability mode) — touch only these files; neither touches the hard core.

---

*This record is CANDIDATE — the machine wrote it, Amihai's to correct, rename, or extend.*
