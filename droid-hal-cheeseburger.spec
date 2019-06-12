# ref: dhd/droid-hal-device.inc

%define device cheeseburger
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty OnePlus 5

%define installable_zip 1
%define droid_target_aarch64 1

%define android_config\
  #define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
