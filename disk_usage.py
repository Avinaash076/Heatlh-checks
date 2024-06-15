#!/usr/bin/env python3

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True
def check_root_full():
    """Returns true if the root position is full,false otherwise"""
    return check_disk_full(disk="/",min_gb=2,min_percent=10)
# Check for at least 2 GB and 10% free
if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: Not enough disk space")
    return 1

print("Everything is  okay")
return 0
def main():
    
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_root_full():
        print("Root partition full.")
        sys.exit(1)
