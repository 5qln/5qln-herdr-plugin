# nodes — one directory per cell-node

A node is a directory `nodes/<word>/` — with `_` standing for ε — holding:

- `cell.node.json` — the node's declared identity: `{"word": "…", "reading": "…"}`.
  `reading` is required iff `word` is `""` (ε is legal only declared, and only as
  origin-of-a-reading — never a global root).
- `question.md` — the node's own centre, planted by the human alone. Never committed.

**No default node. No fallback in code.** A missing or malformed declaration is
`AddressUnknown` and refuses to render.

Convention: ADDRESS.md §4. The workspace label mirrors the node word (ε mirrors as its
`reading`); the mirror is a display, never a source.
