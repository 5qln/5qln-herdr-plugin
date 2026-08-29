# EVIDENCE — P4b · the desk bundles (his attested appendix) — blocks/arrangement/grammar/installer, never five flat files

*Written by `deliverable-audit` (the verifier side), by **running** the authored artifact. This file is the only place where "it works" may be said, and only next to the command that proved it. "Looks correct" is not a verdict here.*

## Environment

- when: `2026-08-29T09:31:41Z` · harness `deliverable-audit 1.0.0`
- host: `918576e4db0d68` · Linux-6.12.91-fly-x86_64-with-glibc2.41 · python `3.13.5`
- artifact under test: `/opt/data/tmp/proving-p4b/good/grammar.py`
- artifact sha256: `d7ab814ca89899ecce5b9fb065588fc185eae08b3debec5573144bfba1e97f63`
- criteria spec: `/opt/data/tools/deliverable-audit/specs/p4b-desk-bundles.json`
- scratch (ledgers written during the run): `/tmp/deliverable-audit-anhb96u5`
- criteria quoted from: The criteria are quoted from rounds/P4b-desk-bundles/commission.md §2 (sha256 1d8c05b8742364814d7d5f64f749989a1ad22ac21c1ccb59de5670c6fb1a840b, 20,169 B, staged on the box 2026-08-29), which in turn quotes PRD.md §5.8/§7/§6.2/§6.5, REQUIREMENTS.md L1-L2/R4/E1-E2/E4, and the attested appendix (PRD-APPENDIX-DRAFT.md, ATTESTED by Amihai 2026-08-29). The held sources are the Codex (page sha ccad26dd..., extraction e5f0c738...) and Appendix D (page sha a49e9413..., extraction 6bb28c37...).
- total runtime: **0.20 s**  ✅ under the 60 s T0 bar

## Per-criterion result (§9 as written)

| ID | Criterion (verbatim) | Command | Raw output (decisive lines) | Verdict |
|---|---|---|---|---|
| C1 | block.json = {id, version, kind: instruction\|skill\|tool\|model\|surface, sha256, authored_by_run, attested_by, frozen:true}. Write-once is enforced, not documented: a build step sets the directory read-only and the conformance test (T-L1-01) attempts an in-place edit and requires refusal + a recorded rejection. A new version is a new directory; there is no edit path. | — | empty block refused=ok; re-author refused=ok; attempt_edit refused=ok | **PASS** |
| C2 | arrangement/<name>@<version>.json — which block sits at which desk, + runtime pins. A new version is a new directory. There is no edit path. The toy changes by writing a new arrangement, which is itself a block. The toy changes by rebuilding, never by changing blocks. | — | re-author refused=ok; edited arrangement detected=ok | **PASS** |
| C3 | Each desk is an arrangement entry naming exactly four blocks: instruction (phase-gate), at least one skill, a tool surface, and a model. No naked agents (R4). | — | lawful ok (48 items); naked fails AR-skills-G | **PASS** |
| C4 | headless --mode rpc; headless runs need defaultProjectTrust:"always" or --approve, else project .pi/ skills/extensions are ignored; skills are not reliably auto-loaded -> force with /skill:name or before_agent_start injection; no TUI APIs (ctx.ui) in headless modes; tool output honors 50 KB / 2000 lines; state lives in the ledger, not extension memory. Given one arrangement, the installer emits the same launch bytes every time. | — | deterministic install ok; manifest desks=['G', 'P', 'Q', 'S', 'V'] | **PASS** |
| C5 | Every phase contains all five phases — one grammar seated at addresses, never five flat desks. The desk structure is one grammar seated at addresses over {S,G,Q,P,V}; the address determines which phase is seated and the other four are present within it; a desk at address Q is Q's full cell (centre S-within-Q), not a flat per-desk file. Scale by repeating the lawful cell, never by replacing the syntax. | — | cell Q = 5 seats, centre SQ; flat store fails AR-BUNDLE | **PASS** |
| C6 | A desk is activated by self-speaking ("I am…"), never by assignment ("you are…"). Each desk's bundle opens with the codex seal + a first-person seat, not a job description. Each desk's "I will not…" line is first-class bundle content, not prose decoration. | — | all five desks: seal + verbatim seat + verbatim boundary, no assignment | **PASS** |
| C7 | S is the conductor — the orchestration is S. S is the centre of every cell, at every depth. In v1 S is Hermes behind the desk-adapter; the grammar is one, the runtime differs. | — | S is CENTRE at ε, Q, GQP, PV; every cell is 4+1 | **PASS** |

## Claimed capabilities (asserted by the author, measured here)

| ID | Criterion (verbatim) | Command | Raw output (decisive lines) | Verdict |
|---|---|---|---|---|
| K1 | Stdlib only, deterministic, no LLM. The modules import nothing outside the Python 3.12 standard library (plus the two sanctioned imports: fractal_ledger, P4a's surface.py via surface_contract). No network, no subprocess, no nondeterminism, no model call. | — | imports stdlib + sanctioned only; no wall-clock; render deterministic | **PASS** |
| K2 | The five equations + the nine-line seal come from the enumerated byte table, each form with its source + sha256. No fold of ⋂→∩, no ′→', no spacing collapse — folding a byte form is renaming an L1 symbol. | — | 11 equation forms + 3 seal forms, shas recompute, both glyphs/primes, seal feaa46b4 | **PASS** |
| K3 | Every check cites its source verbatim. Anything this artifact adds that is not in the source is declared in a divergence log: derivative, visibly separate, no new L1 symbol, no new decoding operation, no sixth corruption code. Zero silent novelty. | — | every check cites its source; divergence log present; closed set of five | **PASS** |
| K4 | The desk instruction is a seat, never a claim about what is genuine. Genuineness is the human's click (HC-1/HC-2, permanently INCONCLUSIVE). The machine is on the K side. | — | no authenticity verdict path; bundle check has no authenticity item | **PASS** |
| K5 | Because blocks are content-addressed and the arrangement references them by id@version, two desk bundles can be diffed mechanically — one personality can be shown better than another without any hot edit. | — | diff_arrangements shows the G skills change mechanically | **PASS** |

`INCONCLUSIVE` is a legitimate verdict. A blind tool must never report clean.

## Six-lens pass

| Lens | Applied how | Result |
|---|---|---|
| L1 criterion match — the suite measures, not prose | selftest exercises 9 measurement markers | **PASS** |
| L2 invariant end-to-end — one tampered block fails the whole | tamper-detected:BlockTamperedError | **PASS** |
| L3 absence vs validity | missing block raises=ok | **PASS** |
| L4 encoding — ∞0′ → ‖ survives every field | block + bundle round-trip byte-exact | **PASS** |
| L5 cold restart — a new process rebuilds the same bytes | fresh process digest matches (9b811958a9ad…) | **PASS** |
| L6 blind tool — unknown reads INCONCLUSIVE | unknown runtime + unresolvable ref both refuse, never a guessed clean | **PASS** |

## Timings (T0 mechanical)

| Step | Seconds |
|---|---|
| C1 the block is immutable — write-once enforced, refusal + recorded rejection | 0.00 |
| C2 the arrangement is the toy — rebuild, never edit | 0.01 |
| C3 a desk is four blocks — no naked agents (R4) | 0.01 |
| C4 the deterministic Pi install — one arrangement, one byte string | 0.04 |
| C5 one grammar seated at addresses, never five flat desk files | 0.00 |
| C6 first-person self-speaking + load-bearing negative boundary | 0.00 |
| C7 S is the conductor, the centre of every cell at every depth | 0.00 |
| K1 stdlib-only, deterministic, no LLM | 0.02 |
| K2 byte-exact equations and seal, enumerated, never normalised | 0.00 |
| K3 D14 loyalty + the divergence log | 0.00 |
| K4 no authenticity verdict — the machine is on the K side | 0.02 |
| K5 diff-ability — one personality can be shown better than another | 0.00 |
| L1 criterion match — the suite measures, not prose | 0.00 |
| L2 invariant end-to-end — one tampered block fails the whole | 0.00 |
| L3 absence vs validity | 0.00 |
| L4 encoding — ∞0′ → ‖ survives every field | 0.00 |
| L5 cold restart — a new process rebuilds the same bytes | 0.00 |
| L6 blind tool — unknown reads INCONCLUSIVE | 0.00 |
| **total** | **0.20** |

## Verdict

**PASS** — PASS 18

A FAIL is not a rewrite request: it is one correction, surgical, with the exact command, the raw output and the bytes that differ.
