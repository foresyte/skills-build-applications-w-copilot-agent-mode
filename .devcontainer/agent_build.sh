#!/usr/bin/env bash
set -euo pipefail

echo "[agent_build] Disabling common telemetry environment variables for this run"
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export AZURE_CORE_COLLECT_TELEMETRY=0
export HOMEBREW_NO_ANALYTICS=1
export NPM_CONFIG_DISABLE_TELEMETRY=1

WORKDIR="$PWD"
echo "[agent_build] workspace: $WORKDIR"

mkdir -p octofit-tracker/backend

if [ ! -d "octofit-tracker/backend/venv" ]; then
  echo "[agent_build] Creating Python virtual environment..."
  python3 -m venv octofit-tracker/backend/venv
  echo "[agent_build] venv created at octofit-tracker/backend/venv"
else
  echo "[agent_build] venv already exists; skipping creation"
fi

if [ -f "octofit-tracker/backend/requirements.txt" ]; then
  echo "[agent_build] Installing Python requirements (telemetry disabled for this session)"
  # shellcheck disable=SC1091
  source octofit-tracker/backend/venv/bin/activate
  pip install -r octofit-tracker/backend/requirements.txt
  deactivate
else
  echo "[agent_build] No requirements.txt found; skipping pip install"
fi

echo "[agent_build] Agent-mode build script finished."
