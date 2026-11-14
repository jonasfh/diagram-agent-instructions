#!/usr/bin/env python3
"""Self-bootstrapping helper that ensures the `d2` CLI binary is available."""

import json
import os
import platform
import shutil
import stat
import tarfile
import tempfile
import urllib.request
from pathlib import Path

CACHE_BIN_DIR = Path.home() / ".cache" / "diagram-agent-tools" / "bin"
D2_RELEASES_API = "https://api.github.com/repos/terrastruct/d2/releases/latest"


def _platform_asset_suffix() -> str:
    sys_name = platform.system().lower()
    machine = platform.machine().lower()

    os_map = {"linux": "linux", "darwin": "macos"}
    arch_map = {
        "x86_64": "amd64",
        "amd64": "amd64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }

    if sys_name not in os_map or machine not in arch_map:
        raise RuntimeError(
            f"Unsupported platform for auto-installing d2: {sys_name}/{machine}. "
            "Please install d2 manually from https://d2lang.com."
        )
    return f"{os_map[sys_name]}-{arch_map[machine]}.tar.gz"


def ensure_d2() -> str:
    """Return path to `d2` binary, downloading into user cache if missing."""
    existing = shutil.which("d2")
    if existing:
        return existing

    cached_bin = CACHE_BIN_DIR / "d2"
    if cached_bin.is_file() and os.access(cached_bin, os.X_OK):
        return str(cached_bin)

    suffix = _platform_asset_suffix()
    req = urllib.request.Request(
        D2_RELEASES_API,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "diagram-agent-instructions"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        release = json.loads(resp.read().decode("utf-8"))

    asset_url = None
    for asset in release.get("assets", []):
        if asset.get("name", "").endswith(suffix):
            asset_url = asset.get("browser_download_url")
            break

    if not asset_url:
        raise RuntimeError(f"Could not find d2 release asset ending with {suffix}.")

    CACHE_BIN_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        archive_path = Path(tmpdir) / "d2.tar.gz"
        urllib.request.urlretrieve(asset_url, archive_path)
        with tarfile.open(archive_path, "r:gz") as tar:
            d2_member = next(
                (m for m in tar.getmembers() if m.isfile() and Path(m.name).name == "d2"),
                None,
            )
            if not d2_member:
                raise RuntimeError("Downloaded d2 archive did not contain a `d2` binary.")
            extracted = tar.extractfile(d2_member)
            if extracted is None:
                raise RuntimeError("Failed to extract `d2` binary from archive.")
            cached_bin.write_bytes(extracted.read())

    cached_bin.chmod(cached_bin.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return str(cached_bin)


if __name__ == "__main__":
    print(ensure_d2())
