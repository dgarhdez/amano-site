#!/bin/sh
set -eu
cd "$(dirname "$0")/.."

paper=$(sed -n 's/.*--paper: \(#[0-9A-Fa-f]\{6\}\).*/\1/p' build.py | head -1)
expected=$(magick -size 1x1 "xc:$paper" -format '%[pixel:p{0,0}]' info:)
samples="$expected|$expected|$expected|$expected|$expected|$expected"
count=0

for file in assets/phones/*/*.webp; do
    [ -f "$file" ] || continue
    count=$((count + 1))
    size=$(magick "$file" -format '%wx%h' info:)
    pixels=$(magick "$file" -format '%[pixel:p{0,0}]|%[pixel:p{600,0}]|%[pixel:p{0,800}]|%[pixel:p{1199,800}]|%[pixel:p{0,1599}]|%[pixel:p{1199,1599}]' info:)
    if [ "$size" != '1200x1600' ] || [ "$pixels" != "$samples" ]; then
        printf 'background mismatch: %s (%s, %s)\n' "$file" "$size" "$pixels" >&2
        exit 1
    fi
done

[ "$count" -eq 42 ] || { printf 'expected 42 phone images, found %s\n' "$count" >&2; exit 1; }
printf 'All %s phone images match %s at their edges.\n' "$count" "$paper"
