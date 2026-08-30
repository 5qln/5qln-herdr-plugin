# CO-DEVELOPMENT — how we built the Fractal Herdr (and how to do it again)

*Written 2026-08-30, at the close of the bridge round — the last firmware round. This document is the
companion to `REVERSE-ENGINEERING.md`: that one reverse-engineers **what** we built; this one records
**how** we built it, so the next co-development can be as efficient as this one and lose nothing to the
ocean.*

*Wherever it quotes Amihai, it is his word. Wherever it names a command, path, hash or identity, those
were executed, not remembered. The machine wrote it; it is his to correct, rename, or extend.*

---

## 0. Why this document exists

Amihai's question, asked at the close: *"Can you truly say the repo holds everything? documented
perfectly?"* The honest answer is **no**. The repo holds the *product* — every commission, evidence file,
attestation, the code, the held sources. It does **not** hold the *process* — how the profile was set up,
how the plan was made, how the sessions ran. That lived scattered across `STATE.md`, `FACTS.md`,
`RESUME-NOW.md`, and the Hindsight bank `herdr`, nowhere in one place.

This document is that missing place. It is the **co-development playbook**: the repeatable part, written
down so the next build (or any co-development) starts from experience instead of from scratch.

---

## 1. The setup — one dedicated profile, isolated from everything else

The first decision was structural: **the build got its own Hermes profile**, `herdr`, separate from
`default` (the VPS sysadmin profile). This was not cosmetic — it meant the build's constitution, skills,
memory and identity could not collide with the machine's other work.

| Thing | Value |
|---|---|
| Profile home | `/opt/data/profiles/herdr` |
| Wrapper | `/opt/data/.local/bin/herdr` → `hermes -p herdr …` |
| Workspace (cwd) | `/opt/data/profiles/herdr/workspace` — `AGENTS.md` here is the constitution |
| Model / delegation | `deepseek-v4-pro` · delegation `gpt-5.6-luna` |
| Memory budget | 6000 chars personal / 2000 user (vs ~2200 on `default`) — the build needs a long memory |
| Keys | DeepSeek · GitHub · Obsidian sync · LiteLLM · VPS · Kimi (cloned `.env`) |
| Telegram | own bot token + `gateway-herdr` (s6) — a dedicated DM, separate from `default` |
| Skills | ~38 kept, focused (5qln-*, herdr-*, dsh, hindsight, github, verification, iPad ops) |
| Verifier harness | `/opt/data/tools/deliverable-audit/` — the non-author's execution engine |

**The two-profile split is load-bearing.** `default` = the VPS, the runtime, everything operational.
`herdr` = only this build. When a request does not serve the build, `herdr` hands it back to `default`.
One goal, one profile, no bleed.

**Pitfalls paid for, so you don't:**
- `HERMES_PROFILE=herdr hermes config set …` silently writes the **default** profile's config. Always use
  the wrapper (`herdr config set …`) and verify which file the confirmation names.
- This profile's own skills are **not curator-managed**; autonomous patches are refused — they need
  `hermes curator adopt <name>`.

---

## 2. The plan phase — a machine proposal *before* any code

The single most unusual thing about this build was that **there was a plan phase before there was any
build round** — and the plan was written by a third party.

- **Qwen** (an external model, routed by Amihai) authored the plan:
  `wiki/projects/fractal-herder/BUILD-FLOW-HERMES-DSH-2026-08-27.md`.
- It was **mirrored** into the workspace as `PLAN.md` with its canon sha recorded in the header.
- It was labelled, from the first line, a **machine proposal (K)** — *not doctrine*. It carried **five
  open questions** that only Amihai could answer.

The key insight is that status word — **K**. The plan was a *candidate*, never mistaken for truth. It
proposed a sequence (Phase 0 sync → Phase 1 audit harness → B0 → B1 → … B6), a set of roles, a cost
discipline, and a drift discipline — and every one of those was treated as *correctable by Amihai* until
he answered the open questions.

**Why this matters for the next build:** a machine-proposed plan, explicitly marked non-authoritative and
held open until the human answers its questions, is what let the build stay honest for ten rounds. The
plan said "here's what I think and here's what I don't know" — and the build followed the first while
respecting the second.

---

## 3. The round — the unit of work

Everything was built one **round** at a time. A round is a directory:

```
rounds/<name>/
├── commission.md     1. Hermes  — what to build + verified facts + criteria verbatim + holds + prohibitions
├── authored/         2. dsh     — code, selftests, phase card (predictions only, never results)
├── evidence.md       3. Hermes  — executed output, per-criterion PASS/FAIL + six lenses ← the only "it works"
├── correction-<k>.md 4. Hermes  — surgical: exact command, traceback, bytes, hashes (≤2)
└── attestation.md    5. Amihai  — one sentence + the sha256 of what he attested
                      6. Hermes  — deposit to canon, mirror, Hindsight, drift check green → closed
```

**The one rule the whole flow exists for:** *an author's own green checkmarks are a hypothesis. Only an
execution record written by the non-author counts as "it works."*

- **dsh** (the author, `deepseek-v4-pro`, one generation per round) writes the code and its own selftests
  and a "phase card" — but the card's every verdict is a **prediction**, and it is forbidden from saying
  anything ran.
- **Hermes** (the verifier, a separate profile, a separate context) runs the artifact fresh, writes
  `evidence.md` with a PASS/FAIL per criterion, and *recomputes every verdict with its own
  implementation.* A divergence in either direction is a FAIL.
- **Amihai** plants, attests, corrects, names — nothing else.

The audit harness encodes three verdicts only — PASS / FAIL / INCONCLUSIVE — and it is impossible for an
operator to soften a FAIL into a PASS. A probe that cannot run is INCONCLUSIVE, never rounded up.

---

## 4. The roles — fixed, and never crossed

| Actor | Owns | May never |
|---|---|---|
| **dsh** (v4-pro, on the box) | authoring: specs, contracts, code, gate semantics, phase cards | state that something ran · touch git · claim a path it did not read |
| **Hermes (`herdr`)** | execution, conformance, host truth, canon + publishing, correction evidence, guiding Amihai | author doctrine · attest · be the conductor's lifecycle authority |
| **Amihai** | **plant · attest · correct · name** | be asked for anything else |

The roles are the discipline. The author never verifies. The verifier never authors. The human never
debugs — he confirms; if he balks, the machine takes it over agent-side.

---

## 5. The disciplines — the rules that kept it honest

1. **Builder ≠ verifier.** The author's green checks are a hypothesis; only the non-author's execution
   record is "it works."
2. **One generation per round.** One dsh authoring run + one verification session + **≤ 2 corrections**.
   Exceeding it is a HOLD surfaced to Amihai, never a silent continue.
3. **Never claim what did not run.** Nothing is described as running unless a verified run wrote state;
   nothing is "attested / decided / verified" that the commission did not already mark so.
4. **Never upgrade a status by writing it.** Candidate → decided → attested only by whose word and on what
   date. TENTATIVE is temporal, never epistemic.
5. **The TTY seal.** `cell-plant` / `cell-attest` refuse a non-TTY (RC=4). Attestation is Amihai's act at
   the terminal — the machine never types his word, and a machine-posed question never reaches the podium.
6. **Drift discipline.** One canon (the repo), one authoring scratch (the box), one read mirror (the
   wiki). Four copies would be four truths, so every mirror records its `canon_sha256` and a zero-token
   drift check runs before a round opens and after it closes.
7. **Never pay twice for a fact.** Verified facts live in `FACTS.md` and in the round's commission. A fact
   re-probed is money spent twice.
8. **The six lenses** — every verification re-checks: criterion match · invariant end-to-end · absence vs
   validity (`e3b0c44298fc…` is the sha of empty) · encoding (`∞0′ → ‖` through every string field) ·
   cold restart (a second process rebuilds from disk alone) · blind tool (unavailable reads INCONCLUSIVE,
   never clean).

---

## 6. Session-to-session — how the build survived restarts

The build ran across many sessions over five days. The machinery that made that survivable:

- **`RESUME-NOW.md`** — a one-page pointer read *first*, telling any fresh session the exact resume
  position.
- **`STATE.md`** — where the build actually stands, opening with THE MAP (✅ done · ▶ here · ☐ not
  started), and never re-probing facts already recorded.
- **`FACTS.md`** — the verified-facts block (executed, not read). "Do not re-probe what is here; a fact
  re-probed is money spent twice."
- **First actions of any session:** drift check (zero tokens) → read RESUME-NOW → STATE → FACTS → load the
  skills the step needs → continue at the first unfinished step.
- **Durable state.** The box and the container differ: `/opt/data` survives restarts, everything else is
  ephemeral. Pointers live in memory; substance lives in the repo, the box, and Hindsight.

The one fear worth naming (Amihai's, recorded): *a mid-build context break stranding the work.* The answer
is the same every time: the durable state is on disk, not in a session — `RESUME-NOW.md` + `STATE.md` +
the repo + Hindsight re-arm a fresh session to the exact position.

---

## 7. The build, round by round — what it actually produced

| Round | What | Canon |
|---|---|---|
| Phase 0 | sync — repo/box/wiki agree, REQUIREMENTS published | `e50eb25` |
| Phase 1 | the audit harness (the verifier's engine) | — |
| R01 · B0 | the ledger + the record (plant/attest, the chain) | `e17e475` |
| R02 · B1 | the read-only walker | `74be2b6` |
| R03 · B2 | the driver (one cell, sequential) | `b316167` |
| P4a | the step mode (the codex's own checklist made mechanical) | `898593b` |
| P4b | the desk bundles (one grammar seated at addresses) | `2a2053a` |
| R04 · B3 | the descent (zoom — `XY := X within Y`) | `be30010` |
| R05 · B4 | the unattended run (the core claim + the observability trail) | `87085ed` |
| the Grammar | the meta implementation (codex Parts II+III executable) | `3d51ecd` |
| **the bridge** | the live desk adapter + the runtime config-read (last firmware) | `105b6ad` |

The whole thing reads as a chip (Amihai's framing): **ASIC = the codex** (sealed, held) · **firmware =
everything we built** (B0 → bridge) · **soft layer = the Pi/Hermes customization** that *activates* the
firmware, never modifies it.

---

## 8. The cost discipline — money is part of the work

- **One dsh generation + one verification + ≤2 corrections per round.** Exceeding it is a HOLD, never a
  silent continue.
- **Heavy generations batched into the cheap overnight window** (before ~10:00 his time), a Telegram alert
  when he is needed.
- **Weekend grant** (his word): dsh runs with no limit on the cost window.
- **Never pay twice for a fact.** Open-ended probing is the expensive mode; the round is surgical —
  artifact + criteria in, evidence out.

---

## 9. What's next — soft mode (no more dsh)

With the bridge closed, **the firmware is finished**. Everything that follows is **soft mode** — soft
files, written by Amihai or by Hermes from his intent, never a code change:

1. **The constitution — S first.** Real desks wired into the five seats, cultivated with him, never
   authored once. The two-way Start is load-bearing: he brings raw interest, S helps crystallize it into
   the question.
2. **The settings surface.** The conductor reads the soft layer at runtime (budget/hold/poll, each desk's
   §2-emphasis/voice/model) — the bridge already built the read path.
3. **The two surfaces over the soft layer.** Developer mode (he writes) vs usability mode (Hermes writes
   from his spoken intent).
4. **The swarm** — endgame, deferred: one firmware, repeated by the lawful cell, driven by many soft-layer
   configs.

D8, answered: **"the output is the input."** The cycle is a spiral of inquiry into manifestation — output
= **B** (the artifact) + **∞0′** (the return question more alive than the start).

---

## 10. What to repeat, and what to change (honest lessons)

**Repeat:**
- A dedicated profile per build (no bleed).
- A machine-proposed plan, marked K, with open questions held for the human.
- The round: commission → author → verify → attest → deposit → drift.
- Builder ≠ verifier; one generation; ≤2 corrections; never claim what didn't run.
- The TTY seal for attestation; never type the human's word.
- RESUME-NOW / STATE / FACTS as the restart machinery.

**Change / watch:**
- **The Hindsight tag collision.** Round deposits were tagged `canon` (meaning "canon commit sha"), which
  reads like "the canon bank." Use `canon-commit` going forward. (The canon *bank* itself was never
  written during the build — verified.)
- **The circular-audit trap** (paid for in P4a): an audit pack accepted against a twin the *pack itself*
  invented reads "accepted" and then fails the real artifact. Rebuild twins from the *real* artifact, never
  a parallel hand-written reference.
- **Path-string byte-identity:** trail lines carry the ledger path as observability, so byte-pinned
  fixtures only reproduce under the canonical work path. Compare under one path, or compare projections.
- **Bank hygiene:** build rounds → `herdr`; produced fruit + research → `living`; source → `canon`
  (read-only, untouched). Check `fact_count` and `last_document_at` before assuming a bank is clean.

---

*This document is the machine's record of the process. Where it quotes Amihai, it is his word; where it
names a command or hash, it was executed. It is his to correct, rename, or extend — and it is meant to be
used, not filed.*
