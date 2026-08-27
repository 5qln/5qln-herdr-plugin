---
title: "Fractal Herdr — Orchestration Proposals (the OPEN design surface)"
created: 2026-08-25
entry_type: proposals
status: MACHINE PROPOSALS (K) — not canon, not doctrine; await H's attestation, line by line
source: dsh session (workspace /home/deploy/Asdh5/fractal-herder) — body verbatim
canon_home: "5qln/5qln-herdr-plugin — docs/fractal-herdr/ORCHESTRATION-PROPOSALS.md (canon; every other copy is a mirror)"
links:
  - "[REQUIREMENTS.md](REQUIREMENTS.md)"
  - "`THE-GAP-2026-08-25`"
  - "`2026-08-25-gqpnv-window-agents`"
---

# Fractal Herdr — Orchestration Proposals (the OPEN design surface)

**Status:** MACHINE PROPOSALS (K). Not canon, not doctrine, not yet requirements. Each is a
concrete candidate for the four OPEN items named in `REQUIREMENTS.md` Part II/IV. The human
attests or strikes, line by line. Where a proposal cannot be settled by structure, the honest
limit is stated on it — resonance is human.

---

## P1 — The gate record: XYZAB handoff schema

**The problem.** O3 requires a durable, hash-chained handoff carrying structure-never-content,
but no schema is fixed. This is the concrete build seam between the dsh engine and the cell.

**Proposal.** Every gate handoff is one record, appended to the cell's ledger
(`state/gates.jsonl`, hash-chained):

```json
{
  "record_id": "sha256(prev_hash ‖ canonical(record))",
  "prev_hash": "…",
  "address": "SGQ",          // word over {S,G,Q,P,V} + sign, Appendix D
  "gate": "z",               // x | y | z | a | b
  "state": "held-pending",   // attested | held-pending | mechanical
  "mark": "emergent",        // emergent | mechanical  (aligner verdict)
  "payload_ref": "session:…/entry:…",  // durable reference, NEVER content
  "axis": { "field": { "mode": "inherited", "anchor": "…" }, "delta": ["…"] },
  "corruption": null         // L1 | L2 | L3 | L4 | V∅ | null
}
```

- `payload_ref` points at the artifact's place in the session log/trail; the record itself
  stores no reconstructable content (engine prohibition §5.3).
- `mark` is the learning-aligner verdict (emergent = the current carried it; mechanical = the
  agent forced it) — mandatory at every gate, so a missing Q entry is visible (the Q-skip fix).
- `axis` is the byte-exact inherited field + declared delta (engine §7/D7).

**Honest limit.** The schema is exact-pattern; it cannot tell a same-referent content drift
from a healthy move — the verdict is a testable claim, the felt lock is human.

---

## P2 — The conductor: a headless gate-walker

**The problem.** E3 requires a driver that walks the gate chain across Pi processes and herdr
panes, but its lifecycle is unspecified.

**Proposal.** The conductor is a small stateless-on-restart process owning a state machine:

```
IDLE → HOLDING_ORIGIN (wait human plant) → WALKING (cycle gates)
     → DESCENDING (zoom into a corner)   → BLOCKED (hold surfaced)
     → ATTESTED (gate closed by human)   → COMPOSING (V: B″ + ∞0′)
     → SEEDING (next S)                  → IDLE / DONE
```

- Persistence is the ledger (P1), never extension memory — Pi forks tear extensions down. On
  restart, the conductor re-arms from the ledger, not from RAM.
- One gate-loop per cell; the conductor fans out to many cells in parallel (P3).
- The conductor detects "needs a human" via three dialects — dsh `held-pending`, herdr
  `blocked`, Pi `terminate`/`ctx.ui.confirm` — and collapses them into one `BLOCKED` state
  with the gate record's `state: held-pending`. It surfaces; it never resolves.
- The conductor's own trace is the gate chain (traceability by construction — no reporting
  layer).

---

## P3 — The parallel scheduler: many cells, one center

**The problem.** O4 requires parallel and multi-dimensional modes; canon is silent on the
scheduler; the law forbids lateral edges ("every decision passes through the center").

**Proposal.** A **field** (the shared center question) owns a set of active cells, each with a
unique address word. The scheduler is a fair queue of independent gate-loops with exactly one
synchronization surface — the center:

- Each cell advances its own gate chain autonomously; no cell reads another cell's mid-chain
  state (lateral edges are forbidden by construction — the only shared object is the center).
- A cell that reaches V deposits its `B″ + ∞0′` to the **assembly** (the center's append-only
  log). A cell that needs a decision asks the center, which routes through the field.
- The center exposes one read: `peek-center` → only `attested` and `held` entries, never
  mid-chain internals. Cells read the field's current question and its attested fruit; nothing
  else crosses.
- Backpressure = the hold doctrine: if a parallel cell stalls, it is `held`, surfaced, and the
  others proceed; a MOVING verdict on any cell stops *that cell's* descent at the human's
  level — it does not freeze the whole field unless the field itself moves.

**Honest limit.** This is a coordination *shape*, not a scheduling policy (fairness, resource
caps, timeouts). Those are build-phase decisions; the requirement is only that the shape obeys
the center-only law.

---

## P4 — Multi-dimensional addressing: the same field on many surfaces

**The problem.** "Do it in different dimensions" — how the same question runs on multiple
surfaces without the cells merging.

**Proposal.** A dimension is a **declared surface**. The axis `field` is the invariant,
inherited byte-exact; `delta` is the per-surface declared references. A multi-dimensional run
is the same field read on N surfaces, each an independent cell with its own address and its
own `delta` — and the movement check is exactly the engine's:

- fields differ → **MOVING** (stop-and-surface)
- fields equal, surfaces equal → **recast**
- fields equal, surfaces differ → **STASIS** (axis held, content moved — health)

The assembly (P6) reads across surfaces by the shared field. Dimensions are orthogonally
addressed: the address word identifies the cell, the surface identifies the axis's delta
within it.

---

## P5 — Bulk end-of-run attestation: the thousand held gates

**The problem.** O5 requires whole-run attestation, but resolving a thousand held gates in one
human act is unbuilt — and must not become heuristic auto-attestation.

**Proposal.** The assembly composes the held list into one **attestation stack**, ordered by
lineage depth (origin spark at the top). The human reviews the run as a *field*, not gate by
gate. The single human act is a **run-verdict** on the field:

- `STASIS` + `authentic` → all held gates resolve as `attested-via-run-verdict`, each recorded
  individually with that provenance (nothing is silently promoted; the provenance differs from
  a direct attestation).
- `MOVING` or `inauthentic` → the cascade stops; the first drift surfaces (stop-and-surface);
  gates below it stay held.

**Hard rule.** The run-verdict is itself **held** until the human attests it — the machine
never converts a run-verdict into per-gate truth by heuristic. This is the direct operational
consequence of "tentative is temporal, never epistemic."

**Honest limit.** This is the deepest proposal and the least settled by structure. It is
exactly the ∞0′ question of the cycle: *what does attestation actually see?* The felt answer
is human; the machinery above is only the shape that refuses to answer on the human's behalf.

---

## P6 — Field-of-inquiry assembly: the holistic question across 100 sessions

**The problem.** O6 requires reading the shared question across a long run; the centrifuge
projection exists per-descent but the assembly-at-scale is unbuilt.

**Proposal.** Structure-only reading, three steps:

1. **Walk the axis inheritance chain** — follow `axis.field.anchor` back byte-exact to the
   deepest shared ancestor field. The field of openness itself is the axis; the deepest shared
   field is the candidate "holistic question."
2. **Collect leaf ∞0′** — every leaf cell's return question is a candidate reading of the
   field's direction (the questions the run could not have asked at its start).
3. **Propose, never attest** — the machine composes the deepest shared field + the leaf ∞0′
   set into a candidate B″ ("the question this run was living"), and *offers* it. The human
   names the question; the machine records the name as the field's new anchor.

**Hard rule.** The machine never reconstructs content (only references); never attests the
composed question; never lets the composed candidate re-enter the flow as attested data until
the human names it.

---

## What these six proposals leave OPEN

The scheduling *policy* (P3), the exact bulk-attestation UX (P5), and the felt definition of
authenticity (P5/P6) are human territory. The structure refuses the four auto-* positions at
every seam — none of P1–P6 lets a heuristic self-validate. Each proposal is a candidate; the
trail records only what the human attests.
