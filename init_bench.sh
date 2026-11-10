#!/bin/bash
export PATH="$PATH:/home/chinmayi/.local/bin"
echo "[+] PATH is configured to: $PATH"
echo "[+] Checking bench and uv locations:"
which bench
which uv

echo "[+] Removing existing partial bench..."
rm -rf /home/chinmayi/employee-bench

echo "[+] Starting bench init..."
cd /home/chinmayi
bench init employee-bench --frappe-branch version-15 --verbose
