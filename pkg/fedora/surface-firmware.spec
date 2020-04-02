Name:       surface-firmware
Version:    20200402
Release:    1%{?dist}
Summary:    Firmware for Microsoft Surface devices

License:    proprietary
BuildArch:  noarch
URL:        https://github.com/linux-surface/linux-surface

%description
This package provides firmware files required Microsoft Surface devices.

%prep

%install
cd surface-firmware
find firmware -type f -name "*.bin" -exec install -D -m644 "{}" "%{buildroot}/usr/lib/{}" \;

%files
/usr/lib/firmware/intel/ipts

%changelog
* Thu Apr 02 2020 Dorian Stoll <dorian.stoll@tmsp.io> 20200402-1
- Bump package version to align across distributions

* Tue Mar 31 2020 Dorian Stoll <dorian.stoll@tmsp.io> 20191004-2
- Bump pkgrel

* Wed Oct 02 2019 Dorian Stoll <dorian.stoll@tmsp.io>
- Actually fix the HID descriptor on Surface Laptop instead of replacing it

* Wed Oct 02 2019 Dorian Stoll <dorian.stoll@tmsp.io>
- Update firmware to fix touch input for Surface Laptop

* Fri Sep 27 2019 Dorian Stoll <dorian.stoll@tmsp.io>
- Initial version
