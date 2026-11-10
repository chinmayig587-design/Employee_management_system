#!/bin/bash
set -e

MONGODB_DIR="/home/chinmayi/mongodb"
DOWNLOAD_URL="https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2404-8.0.4.tgz"
TGZ_FILE="mongodb.tgz"

echo "[+] Creating MongoDB directories..."
mkdir -p "$MONGODB_DIR"
mkdir -p "$MONGODB_DIR/data"
mkdir -p "$MONGODB_DIR/logs"

cd "$MONGODB_DIR"

if [ ! -f "bin/mongod" ]; then
    echo "[+] Downloading MongoDB 8.0.4..."
    curl -L "$DOWNLOAD_URL" -o "$TGZ_FILE"

    echo "[+] Extracting archive..."
    tar -zxvf "$TGZ_FILE" --strip-components=1

    echo "[+] Cleaning up archive..."
    rm "$TGZ_FILE"
    echo "[+] MongoDB binary setup completed!"
else
    echo "[+] MongoDB is already downloaded and extracted."
fi
