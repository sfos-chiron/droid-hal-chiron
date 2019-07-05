# Reference: dhd/droid-hal-device.inc

%define vendor oneplus
%define device cheeseburger

%define vendor_pretty OnePlus
%define device_pretty 5

%define installable_zip 1
%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define makefstab_skip_entries /dev/cpuctl

%define additional_post_scripts \
/bin/chmod +x /usr/bin/droid/android-links.sh || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
