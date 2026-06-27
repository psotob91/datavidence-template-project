#!/usr/bin/env python3
"""Probe machine capacity to size parallelization (cores / RAM / OS).

Standard-library only (no deps), cross-platform. Used by
`.claude/policies/analysis/computational-efficiency.md` to choose worker counts
and a parallel backend before running expensive R code.

Usage:
    python scripts/sysinfo.py            # human-readable summary
    python scripts/sysinfo.py --json     # machine-readable JSON
"""
from __future__ import annotations

import json
import os
import platform
import sys


def total_ram_bytes() -> int | None:
    """Total physical RAM in bytes, or None if it cannot be determined."""
    # Linux / macOS: POSIX sysconf
    try:
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
    except (ValueError, AttributeError, OSError):
        pass
    # Windows: GlobalMemoryStatusEx via ctypes
    try:
        import ctypes

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))  # type: ignore[attr-defined]
        return int(stat.ullTotalPhys)
    except Exception:
        return None


def main() -> int:
    cores = os.cpu_count() or 1
    ram = total_ram_bytes()
    ram_gb = round(ram / 1024 ** 3, 1) if ram else None
    # Conservative default: leave one core for the OS.
    suggested_workers = max(1, cores - 1)
    info = {
        "os": f"{platform.system()} {platform.release()}",
        "machine": platform.machine(),
        "logical_cores": cores,
        "total_ram_gb": ram_gb,
        "suggested_parallel_workers": suggested_workers,
        "half_ram_gb": round(ram_gb / 2, 1) if ram_gb else None,
    }

    if "--json" in sys.argv[1:]:
        print(json.dumps(info, indent=2))
        return 0

    print("Machine capacity (for parallelization sizing)")
    print(f"  OS / arch          : {info['os']} ({info['machine']})")
    print(f"  Logical cores      : {cores}")
    print(f"  Total RAM (GB)     : {ram_gb if ram_gb is not None else 'unknown'}")
    print(f"  ~1/2 RAM (GB)      : {info['half_ram_gb'] if info['half_ram_gb'] else 'unknown'}"
          "   <- DuckDB-vs-data.table rule of thumb")
    print(f"  Suggested workers  : {suggested_workers}   (cores - 1; always use reproducible seeds)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
