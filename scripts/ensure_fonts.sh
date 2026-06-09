#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FONT_DIR="${MANUSCRIPTS_FONT_DIR:-$ROOT/assets/fonts}"
KAMI_FONT_DIR="${KAMI_FONT_DIR:-$HOME/.agents/skills/kami/assets/fonts}"

mkdir -p "$FONT_DIR"

MIN_TSANGER=10000000
MIN_JETBRAINS=30000

check_size() {
  local file="$1"
  local min_size="$2"
  [[ -f "$file" ]] || return 1
  local size
  size=$(wc -c < "$file" | tr -d ' ')
  [[ "$size" -ge "$min_size" ]]
}

copy_if_valid() {
  local source="$1"
  local target="$2"
  local min_size="$3"
  if check_size "$source" "$min_size"; then
    cp "$source" "$target"
    echo "OK: copied $(basename "$target")"
    return 0
  fi
  return 1
}

download_if_valid() {
  local url="$1"
  local target="$2"
  local min_size="$3"
  echo "  Trying: $url"
  if curl --retry 2 --connect-timeout 15 --max-time 300 -fSL "$url" -o "$target.tmp" 2>/dev/null; then
    if check_size "$target.tmp" "$min_size"; then
      mv "$target.tmp" "$target"
      echo "OK: downloaded $(basename "$target")"
      return 0
    fi
  fi
  rm -f "$target.tmp"
  return 1
}

ensure_file() {
  local name="$1"
  local min_size="$2"
  shift 2
  local target="$FONT_DIR/$name"

  if check_size "$target" "$min_size"; then
    echo "OK: $name already present"
    return 0
  fi

  if copy_if_valid "$KAMI_FONT_DIR/$name" "$target" "$min_size"; then
    return 0
  fi

  local url
  for url in "$@"; do
    if download_if_valid "$url" "$target" "$min_size"; then
      return 0
    fi
  done

  echo "ERROR: could not prepare $name" >&2
  return 1
}

ensure_file \
  "TsangerJinKai02-W04.ttf" \
  "$MIN_TSANGER" \
  "https://tsanger.cn/download/%E4%BB%93%E8%80%B3%E4%BB%8A%E6%A5%B702-W04.ttf" \
  "https://cdn.jsdmirror.com/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W04.ttf" \
  "https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W04.ttf"

ensure_file \
  "TsangerJinKai02-W05.ttf" \
  "$MIN_TSANGER" \
  "https://tsanger.cn/download/%E4%BB%93%E8%80%B3%E4%BB%8A%E6%A5%B702-W05.ttf" \
  "https://cdn.jsdmirror.com/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W05.ttf" \
  "https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W05.ttf"

ensure_file \
  "JetBrainsMono.woff2" \
  "$MIN_JETBRAINS" \
  "https://cdn.jsdmirror.com/gh/tw93/Kami@main/assets/fonts/JetBrainsMono.woff2" \
  "https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/JetBrainsMono.woff2"

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$FONT_DIR" >/dev/null 2>&1 || true
fi

echo "OK: shared fonts ready in $FONT_DIR"
