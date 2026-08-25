# CHANGELOG — 5qln-herdr-plugin

The manifest's own header carries the full lineage and the lessons each version taught;
this file is the short form.

## 2026-08-24 — manifest lineage (all authored against herdr 0.8.2 / protocol 20)

- **v1** — never linked. The live server rejected it: `plugin_manifest_parse_failed →
  missing field \`id\``. The TOML input model's identity key is `id`; `plugin_id` is the
  name the API hands back. A schema of the API's view is not a schema of the file.
- **v2** — identity key corrected; `[[events]]` withheld rather than guessed.
- **v3** — `[[events]]` restored with the verified DOTTED name
  `pane.agent_status_changed` (the underscored `EventKind` spelling is the push-stream
  namespace and would be an unknown name in a manifest hook).
- **v4** — node-local centre (R4). The podium command becomes relative
  (`watch -n 2 cat ./question.md`); the node is selected by the pane's `cwd`
  (proven: `--cwd` is honoured outside `plugin_root`). One manifest serves every node at
  every depth.

## 2026-08-25 — repo v1 (public revision)

- `bin/_cell_api.py` shipped in its portable form: state directory derived from the file's
  own location, no host paths, no references to any other agent's files.
- `bin/cell-plant` / `bin/cell-attest` are the v2 node-local revisions (what the live host
  runs after the descent swap).
- `cell.layout.json` / `cell.yaml` aligned to R4: podium command relative, every pane
  living in the ε node's directory.
- `ADDRESS.md`, `README.md`, `LICENSE`, `.gitignore`, `nodes/_/cell.node.json` added.
