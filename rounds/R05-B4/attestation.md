# ATTESTATION — R05 · B4 · the unattended run

*Amihai's act. One sentence in his own words, and the sha256 of what he attested. The machine wrote the
material below the line so he knows exactly what he is putting his word to; it never types his word for him.*

---

## What he ran, by his own hand

```
bash /home/deploy/the-cell/rounds/R05-B4/verify-live.sh
```

Its output, from his own box (python 3.12.3; the machine ran the identical script first — this is what it showed):

```
Python 3.12.3
Ran 34 tests in 26.438s
OK
6989a742f57ec60a54d44062bad3fe9c6d2df28e66e92de96c1336be3a6539c3  /home/deploy/the-cell/state/gates.jsonl
```

## What is being attested

That **B4 — the unattended run — does what it was commissioned to do**, on the evidence of an execution
record written by the non-author (`evidence.md`, **18/18 PASS — C1–C7, K1–K5, six lenses — 6.93 s, zero
corrections**), and an audit pack **accepted 42/42 against the real interface before it judged anything**
(the conforming run passes; a twin with five surgical defects — C1 hold-state, C2 seed-tentative,
C5 audit, K1 third-party import, K5 podium write — fails exactly those axes and is named).

- holds accumulate instead of stopping the run — a held gate is recorded, never auto-resolved, and other cells keep moving (C1);
- TENTATIVE seeding of the next S — `tentative: true`, corruption L2, never promoted, never reaching the podium (C2);
- restart re-arm from the ledger alone — a fresh process re-arms to byte-identical ledger + trail, no duplicate/skipped gate (C3);
- budget hold — a spend ceiling surfaces as a held gate, never a silent kill, never an overspend (C4);
- no tentative node consumed by a downstream gate — the dependency audit (C5);
- ≥ 20 cycles with zero human keystrokes — the plant is the only attested record (C6);
- **the observability deliverable** — a readable, hash-chained, replayable trail *while it runs*, decoding-not-transcript, two trails never merged (C7);
- the five desk function-specs are the **codex §2 decoding operations in attention mode**, quoted byte-faithful — no new L1 symbol, no new decoding operation (K2/K3);
- stdlib-only, no LLM in the run mechanics (K1); no authenticity verdict (K4); no write path to the podium (K5);
- the six lenses, including cold-restart (a fresh process rebuilds from disk alone) and absence-never-valid.

**What is NOT being attested:** that a real desk has ever booted or answered a prompt — no desk is
constituted on the box, so the run is fixture-driven (deterministic stand-in desks, hold H-B4-1); the
live per-Pi memory-cost measurement awaits a constituted desk (H-B4-2); B″ composition is B6, not B4
(H-B4-5); and nothing about B5–B6.

## The drafted sentence — his to change, delete, or replace

> *"I attest the unattended run — holds accumulate instead of stopping, tentative seeding never reaches
> the podium, restart re-arms from the ledger alone, the budget holds as a held gate, twenty cycles with
> zero keystrokes, and a readable trail while it runs. Verified PASS 18/18, zero corrections."*

**He may say it differently, or say only "attest it". The machine never types his word for him.**

## His word — recorded exactly as he gave it

> **"attest the unattended run — holds accumulate instead of stopping, tentative seeding never reaches
> the podium, restart re-arms from the ledger alone, the budget holds as a held gate, twenty cycles with
> zero keystrokes, and a readable trail while it runs. Verified PASS 18/18, zero corrections."**
> — Amihai Loven, 2026-08-29.

*(His fuller word, sent after the close; the earlier terse "attest it" endorsed this same sentence as
drafted. Nothing else changed — the round stays closed and attested.)*

---

- `evidence.md` sha256: `8fde8c5b91e882de334111b24988e978619f654f7fc27a6d0f1ad54329096938`
- `commission.md` sha256: `fe61d69b974be4aec84fef164c5be818040beaee9473483963857a00a0473a22`
- authored files (sha256): `run.py 5a798bbd…` · `trail.py fd3f557c…` · `cost.py f9ddb7a0…` · `surface_contract.py aa0ea654…` · `selftest.py 36db2f99…` · `phase-card.md 885ee2c9…`
- his box at the moment of attesting: `state/gates.jsonl` — 1 record, his plant (`6989a742…`; B4 is a run on fixtures, not a gate)
- date: **2026-08-29**
