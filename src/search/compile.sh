#!/bin/bash
gcc  $(pkg-config --cflags python3) ped.c -o ped
