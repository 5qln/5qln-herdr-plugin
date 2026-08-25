# 5qln-herdr-plugin — The Cell as a Herdr instrument

The 4+1 cell as a [Herdr](https://herdr.dev) plugin: a sealed podium holding the human's
question, four free desks **G · Q · P · V**, and the gestures that raise, plant, attest and
descend.

> One rule: the cell, 4 + 1. Four corners — Language · Circle · Machine · Persons — around the
> attested centre. The centre is attested, never claimed; it has no name, and nothing in this
> plugin stands on it.

The machine holds the form; the humans attest the meaning.

## What the cell is

A cell is **1 centre + 4 corners**, invariant at every depth and every height — never 3+1,
never 6+1 ([ADDRESS.md](ADDRESS.md), D.1). In this plugin:

- **The podium** — a plugin-owned, shell-less pane that renders only `question.md`. The
  centre. The question is planted by the human alone, by hand, in the pane.
- **The four desks** — G (the irreducible essence), Q (the lock), P (the unforced gradient),
  V (what crystallized). Bare panes; agents boot only at an attested walk.
- **Zoom** — a desk is not a smaller box, it is the same cell one level in (`XY := X within
  Y`). Every node is a directory; the descent is an address, not a copy.

## Requirements

- herdr **0.8.2** (protocol 20) — the manifest pins `min_herdr_version = "0.8.2"`
- Linux
- `watch`, a POSIX shell, python3 (stdlib only — no dependencies)

## Layout

```
5qln-herdr-plugin/
├── herdr-plugin.toml      the manifest (v4 — node-local centre)
├── ADDRESS.md             the node language (locked vocabulary, §A)
├── cell.layout.json       the score, machine form (what `cell-begin` applies)
├── cell.yaml              the same score, human-readable
├── bin/
│   ├── _cell_api.py       the cell's own minimal herdr socket client (stdlib)
│   ├── cell-begin         raise the cell in its own workspace (free)
│   ├── cell-plant         open a node's question.md for the human (TTY-guarded)
│   ├── cell-attest        record the human's attestation at a gate (TTY-guarded)
│   ├── cell-zoom          report the descent into the focused desk (pure read)
│   └── cell-on-desk-state event hook: record desk agent transitions (recorder only)
└── nodes/
    └── _/                 the ε node (the origin of this reading)
        └── cell.node.json the node's declared identity (template)
```

## Install

The plugin's actions are invoked by herdr as absolute commands inside the plugin directory.
The canonical deployment root is `/home/deploy/the-cell`; if you install elsewhere, adjust
the absolute paths in `herdr-plugin.toml` and `cell.layout.json` (the podiums are
node-local and need no path edits — only the action commands and the workspace cwd do).

```sh
# 1. place the tree (deploy root shown; any root works with the path edits above)
mkdir -p /home/deploy/the-cell && cp -r . /home/deploy/the-cell/plugin

# 2. link the plugin (directory form; --disabled first is the safe order)
herdr plugin link /home/deploy/the-cell/plugin --disabled
herdr plugin list --json          # verify: panes ["podium"], warnings []

# 3. enable it
herdr plugin enable cell.fiveqln

# 4. raise the cell
herdr plugin pane open --plugin cell.fiveqln --entrypoint podium \
  --placement split --target-pane <a desk pane id> --cwd /home/deploy/the-cell/nodes/_ \
  --no-focus
```

Then plant the first question — the human's act, in the pane, with a keyboard:

```sh
EDITOR=vi /home/deploy/the-cell/plugin/bin/cell-plant      # ε node
EDITOR=vi /home/deploy/the-cell/plugin/bin/cell-plant SGQ  # any declared node
```

## The four actions

| action | context | guard | what it does |
|---|---|---|---|
| `begin` | global | refuses a standing cell; never `focus:true`; never touches `w1` | raises the cell: podium + desks, boots no agents |
| `plant` | global | **refuses without a human TTY** (exit 4, no override) | opens the node's `question.md` in `${EDITOR}` |
| `attest` | global, pane | **refuses without a human TTY**; structural centre detection | appends one gate line to `state/gates.jsonl`, bound to the question's sha256 |
| `zoom` | pane | refuses the centre; pure read | reports the descent target; creates nothing |

The centre is detected **structurally** — the pane that is not one of the four desks — never
by matching a label string. The plugin podium's label is derived from the manifest pane's
`title` (`THE QUESTION`); a name-based lookup would break the first time that title changes.

## The node model (ADDRESS.md §4)

- A node is a directory `nodes/<word>/` (`_` stands for ε), holding `cell.node.json`
  (the declared word; `reading` required iff the word is empty) and `question.md`
  (the node's own centre, human-planted only).
- **No default node. No fallback in code.** A missing or malformed declaration is
  `AddressUnknown` — refuse, never assume ε.
- The podium command is **relative** (`watch -n 2 cat ./question.md`); the node is selected
  by the pane's `cwd`. One manifest serves every node at every depth.
- The workspace label mirrors the node word for the human's eyes (ε mirrors as its
  `reading`). The mirror is a display, never a source; a disagreement refuses.

Words are stored; **addresses are derived** (`+^k · (−x₁)…(−x_m)`, all `+` first). The
grammar, the decision rule and the One Law are in [ADDRESS.md](ADDRESS.md), with the canon
spans quoted verbatim.

## The law, encoded

- **The seal.** The podium is a plugin-owned non-shell pane — no interactive shell lives
  there, so typed text cannot become commands. An agent that is not already inside the
  socket's uid has no write path to the centre.
- **Fail closed.** `plant` and `attest` refuse to run unless a human is at the keyboard.
  An attestation typed by a machine is not an attestation; there is no flag, no env var,
  no override path — by construction, not by policy.
- **Nothing autonomous.** No `[[startup]]`, no `[[build]]`, no `[[link_handlers]]`. The
  events hook is a pure recorder — it writes `state/desk-state.jsonl` for the cell's desks
  only, drops every other workspace's events unread, never mutates, and always exits 0.
  A hook is not a gate.
- **One cell, many scales.** `zoom` reports the descent; a real descent creates a
  word-named node directory and opens the same podium there with `--cwd nodes/<word>/`.

## What this repository deliberately does not contain

- `state/` — runtime records (gates, desk state) are never committed.
- `question.md` — centres are human-planted; the repo ships no question and no placeholder.
- The workshop — operator guides, tuning knobs, bridge logs, API schema dumps and the
  conversation history of the cell's construction stay private. This repo is the
  instrument, not the workshop.
- The memory-side kernel (`cell_context.py` and its tests) — that is the orchestrator's
  renderer and lives with the orchestrator, not with this plugin. `ADDRESS.md` is the
  shared vocabulary both sides hash against.

## Version & provenance

- Manifest **v4** (node-local centre, R4) — byte-identical to the artifact verified and
  linked on the live host (sha256 `11b9b53c…a791`). Its header carries the full lineage:
  v1 rejected by the parser (`missing field id`), v2 corrected + events withheld, v3 events
  restored with the verified dotted name, v4 centre made node-local.
- `ADDRESS.md` — locked candidate, sha256 `2724c99b…644`; the span-checked vocabulary both
  agents hash against (8/8 canon spans matched).

The byte-identical artifacts (manifest, `ADDRESS.md`, `bin/*`) keep their original
provenance headers, which cite the construction workshop's internal reports (`inbox/…`)
and its sibling agent. Those references are provenance — pointers into the workshop's
history, not files shipped here — and are preserved so the verified bytes stay the
verified bytes. If you change nothing else, change nothing there.
- `cell.layout.json` / `cell.yaml` — **R4-aligned revision**: the podium command is
  relative and every pane lives in the ε node's directory. The live host's on-disk score
  is the older absolute-path form (sha256 `d9b4512f…`); the delta is the R4 demotion
  itself — the centre path is a node coordinate, not a privileged root.
- `bin/cell-plant` / `bin/cell-attest` — the v2 node-local revisions (sha256
  `6b8b8909…` / `fa6bd292…`), identical to what the host runs after the §D swap.
- `bin/_cell_api.py` — the repo revision: state directory derived from the file's own
  location, no host paths, no references to any other agent's files.

## License

MIT — see [LICENSE](LICENSE). The instrument is free; the meaning is attested.
