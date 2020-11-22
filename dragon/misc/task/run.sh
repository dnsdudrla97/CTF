#!/bin/sh

# 867361737988403547205962240695953369140625L \
qemu-system-x86_64  -kernel vmlinuz-lts  -initrd initramfs.release.img.lz4  -nographic -monitor /dev/null    -append "console=ttyS0 quiet"
