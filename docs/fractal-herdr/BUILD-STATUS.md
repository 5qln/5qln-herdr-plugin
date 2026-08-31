# BUILD-STATUS — where the Fractal Herdr build stands

*Canonical state record. Status words are binding: **candidate / decided / attested**. The live box
beats this file for *state*; this file beats the box for *revision* — reconcile before acting.
Nothing is upgraded by being written here: ATTESTED means an execution record written by the non-author
exists; DECIDED means Amihai's word; CANDIDATE is everything else.*

*Last updated: 2026-08-31.*

## The map (start → end)

**Firmware — attested and closed** (each an execution record written by the non-author):

- B0 ledger/record · B1 walker · B2 driver · P4a step-mode · P4b desk-bundles · B3 descent ·
  B4 unattended run · the Grammar (decoder/compiler) · the bridge (live desk adapter + softconfig
  read-path) · R06 orchestration · R07 the seam (`cellctl`, 13 commands) · R08 the bindings
  (the hard↔soft link) + correction-1 (TypeBox 1.x `.description()` constructor fix).

**Soft layer — candidate, cultivated (never authored once):**

- W3 — all five desks wired: `desks/{S,G,Q,P,V}/` each `SYSTEM.md` + `AGENTS.md` + `boot.sh` +
  `.pi/`, all parse `lawful`. The five desks run live on fresh sessions; S = conductor +
  x-articulator, holding `/conduct`.

**Next — W4: the first real `/conduct` (the paid turn). Amihai's order alone.**

## The one open word (the acceptance word)

`/conduct` refuses until the cell spec declares a **scenario** — the acceptance word for what the
first run *does*. The engine answers verbatim:

> `the cell spec declares no scenario (D2 open — the acceptance word is Amihai's to choose)`

That word is **Amihai's to choose**; the machine must not invent it. It is the sole blocker between
the wired cell and the first real run.

## Live truth (re-probe, never assert)

- The five desks are live at `/home/deploy/the-cell/desks/`; S has `/conduct` and calls the engine,
  which answers honestly (above). The plant is untouched (`6989a742…`); the drift check is in sync.
- PRD §0.2 (the build-rounds record) is current through R07; R08 + W3 are recorded here pending the
  next PRD fold.

## Status discipline

- **ATTESTED:** the firmware rounds listed above.
- **DECIDED (Amihai's word):** D1–D7 (PRD §13.1) · D8 answered ("the output is the input", canon
  `REVERSE-ENGINEERING.md`) · the address letter-order inner-first · S = Pi conductor.
- **CANDIDATE:** the five desk constitutions and everything else the cultivation loop is still refining.
