#!/usr/bin/env bash
# Export redacted cloud agent transcripts to diagnostics/cursor-chat-archive/cloud/
# Run from a machine with Cursor Cloud MCP or copy JSON from agent dashboard exports.
# Output files are gitignored — store copies on Google Drive for ticket #375660.

set -euo pipefail
OUT_DIR="$(cd "$(dirname "$0")/cloud" && pwd)"
mkdir -p "$OUT_DIR"

BC_IDS=(
  bc-badd5954-984d-412a-8c1c-80a985692480
  bc-87234e27-1251-4700-9db0-c37e19a60626
  bc-16f364f0-f650-4deb-a735-e07176aba537
)

echo "Manual step: open each agent URL while logged in and save a PDF or use Cloud Agent transcript export."
echo "URLs:"
for id in "${BC_IDS[@]}"; do
  echo "  https://cursor.com/agents/${id}"
done
echo ""
echo "If you have transcript.json files, place them here and run:"
echo "  python3 $(dirname "$0")/redact-transcript.py INPUT.json > OUTPUT.redacted.json"
