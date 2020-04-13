# Reference: dhd/droid-hal-device.inc

%define vendor xiaomi
%define device chiron

%define vendor_pretty Xiaomi
%define device_pretty Mi Mix 2

%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
  /bt_firmware\
  /bugreports\
  /d\
  /dsp\
  /firmware\
  /persist\
  /product\
  /sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc
