# Reference: dhd/droid-hal-device.inc

%define vendor oneplus
%define device cheeseburger

%define vendor_pretty OnePlus
%define device_pretty 5

%define installable_zip 1
%define droid_target_aarch64 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define makefstab_skip_entries /sys/fs/pstore /dev/cpuctl /dev/cpuset

%include rpm/dhd/droid-hal-device.inc
