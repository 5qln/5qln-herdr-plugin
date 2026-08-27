#!/usr/bin/env python3
"""What Amihai's own command runs — read-only, on his own cell.

Shows three things and writes nothing:
  1. his ledger's fingerprint before and after (must be identical)
  2. the driver's boot() against HIS live cell: it must REFUSE, because no desk on this
     box is constituted per §7 (no Pi extension is installed) — B2's fail-closed default
  3. that his five desks still resolve by label through the same adapter (a read)
No prompt is sent. No record is appended. Nothing under ~/.pi is touched.
"""
import hashlib
import json
import os
import sys

AUTHORED = "/home/deploy/the-cell/rounds/R03-B2/authored"
LEDGER = "/home/deploy/the-cell/state/gates.jsonl"
SOCK = "/home/deploy/.config/herdr/herdr.sock"

sys.path[:0] = [AUTHORED, "/home/deploy/the-cell/ledger"]
os.environ["FRACTAL_LEDGER_DIR"] = "/home/deploy/the-cell/ledger"

before = hashlib.sha256(open(LEDGER, "rb").read()).hexdigest()
pi_before = hashlib.sha256(open("/home/deploy/.pi/agent/settings.json", "rb").read()).hexdigest()

import instrument as I     # noqa: E402
import lens as L           # noqa: E402
import driver as D         # noqa: E402

print("1. your ledger, before      :", before[:16] + "…", "(%d bytes)" % os.path.getsize(LEDGER))
print()

print("2. the driver boots against YOUR cell:")
drv = D.Driver(socket_path=SOCK, ledger_path=LEDGER)   # the shipped arrangement, as authored
try:
    out = drv.boot()
    print("   IT STARTED — due:", out.get("due"), "  <-- this is NOT expected today")
except Exception as exc:
    print("   REFUSED  :", type(exc).__name__)
    print("   because  :", str(exc)[:150])
    print("   stage    :", getattr(exc, "stage", "-"), "/ verdict:", getattr(exc, "verdict", "-"))
    print("   meaning  : no desk on this box is constituted per §7 (no Pi extension is")
    print("              installed), so the driver refuses before sending anything.")
print()

print("3. your desks still read by label, through the same adapter (a read):")
try:
    print("  ", json.dumps(drv.instrument.desks(), ensure_ascii=False))
except Exception as exc:
    print("   read failed:", type(exc).__name__, str(exc)[:100])
finally:
    drv.close()
print()

after = hashlib.sha256(open(LEDGER, "rb").read()).hexdigest()
pi_after = hashlib.sha256(open("/home/deploy/.pi/agent/settings.json", "rb").read()).hexdigest()
print("4. your ledger, after       :", after[:16] + "…")
print("   your ~/.pi settings      :", "unchanged" if pi_after == pi_before else "CHANGED")
print()
print("VERDICT:", "nothing was written — your ledger is byte-identical"
      if after == before else "SOMETHING CHANGED — stop and tell Hermes")
