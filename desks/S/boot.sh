#!/usr/bin/env bash
# boot the S desk as pi, in its own cwd, constitution loaded
export PI_SKIP_VERSION_CHECK=1
source ~/.nvm/nvm.sh >/dev/null 2>&1
cd /home/deploy/the-cell/desks/S
exec pi --provider deepseek --model deepseek-v4-pro --append-system-prompt "$(cat SYSTEM.md)"
