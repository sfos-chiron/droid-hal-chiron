# Reference: dhd/droid-hal-device.inc

%define vendor oneplus
%define device cheeseburger

%define vendor_pretty OnePlus
%define device_pretty OnePlus 5

%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
  /bt_firmware \
  /dsp \
  /firmware \
  /persist \
%{nil}

%define makefstab_skip_entries /sys/fs/pstore /dev/mtp

%include rpm/dhd/droid-hal-device.inc
