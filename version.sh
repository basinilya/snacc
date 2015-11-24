#!/bin/sh
ver=
if { read ver <version.txt; } 2>/dev/null && [ -n "$ver" ]; then
  printf "%s\n" "$ver"
else
  git describe --dirty --always --tags | sed -e 's/^[^0-9]*[-_]//' -e 's/-/_/g'
fi
