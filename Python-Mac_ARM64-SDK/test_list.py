#!/usr/bin/env python3
import sys
from pathlib import Path

# Add the local "src" directory so we can import the SDK directly
HERE = Path(__file__).resolve().parent
SRC_DIR = HERE / "src"
sys.path.insert(0, str(SRC_DIR))

from StreamDock.DeviceManager import DeviceManager


def main() -> None:
    manager = DeviceManager()
    devices = manager.enumerate()

    print(f"Found {len(devices)} StreamDock device(s)")
    for dev in devices:
        print(
            f"- {dev.__class__.__name__} "
            f"VID=0x{dev.vendor_id:04X} "
            f"PID=0x{dev.product_id:04X} "
            f"Path={dev.path}"
        )


if __name__ == "__main__":
    main()
