#!/bin/bash
MONGODB_DIR="/home/chinmayi/mongodb"

echo "[+] Starting MongoDB daemon..."
"$MONGODB_DIR/bin/mongod" \
  --dbpath "$MONGODB_DIR/data" \
  --logpath "$MONGODB_DIR/logs/mongod.log" \
  --port 27017 \
  --fork \
  --bind_ip 127.0.0.1

echo "[+] Checking if mongod process is running..."
sleep 2
ps aux | grep mongod | grep -v grep
