%global             full_name zen-browser-twilight
%global             application_name zen
%global             debug_package %{nil}

Name:               zen-browser-twilight
Version:            1.0.2.t.0.20241210010952
Release:            1%{?dist}
Summary:            Zen Browser Twilight Build

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/twilight/zen.linux-aarch64.tar.bz2
Source1:            %{full_name}.desktop
Source2:            policies.json
Source3:            %{full_name}

ExclusiveArch:      aarch64

Recommends:         (plasma-browser-integration if plasma-workspace)
Recommends:         (gnome-browser-connector if gnome-shell)

%description
This is a package of the twilight (pre-release) build of Zen web browser for aarch64. 
Zen Browser is a fork of Firefox that aims to improve the browsing experience by focusing on a simple,
performant, private and beautifully designed browser.

Bugs related to Zen should be reported directly to the Zen Browser GitHub repo: 
<https://github.com/zen-browser/desktop/issues>

Bugs related to this package should be reported at this Git project:
<https://github.com/ArchitektApx/zen-browser-copr>

%prep
%setup -q -n %{application_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{full_name},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

%__cp -r * %{buildroot}/opt/%{full_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{full_name}/distribution

%__install -D -m 0755 %{SOURCE3} -t %{buildroot}%{_bindir}

%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png

if [ -d /usr/share/hunspell ]; then ln -Tsf /usr/share/hunspell %{buildroot}/opt/%{full_name}/dictionaries; fi
if [ -d /usr/share/hyphen ]; then ln -Tsf /usr/share/hyphen %{buildroot}/opt/%{full_name}/hyphenation; fi

%files
%{_datadir}/applications/%{full_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{full_name}
/opt/%{full_name}

%changelog
* Tue Dec 10 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.0.20241210010952
- Update to upstream release 1.0.2.t.0.20241210010952

* Mon Dec 09 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.0.20241209001057
- Update to upstream release 1.0.2.t.0.20241209001057

* Mon Dec 09 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.0.20241208194125
- Update to upstream release 1.0.2.t.0.20241208194125

* Sun Dec 08 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241208095719
- Update to upstream release 1.0.1.t.22.20241208095719

* Sat Dec 07 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241207172449
- Update to upstream release 1.0.1.t.22.20241207172449

* Sat Dec 07 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241207113605
- Update to upstream release 1.0.1.t.22.20241207113605

* Fri Dec 06 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241206101632
- Update to upstream release 1.0.1.t.22.20241206101632

* Fri Dec 06 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241206012838
- Update to upstream release 1.0.1.t.22.20241206012838

* Thu Dec 05 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241205164042
- Update to upstream release 1.0.1.t.22.20241205164042

* Thu Dec 05 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241205001055
- Update to upstream release 1.0.1.t.22.20241205001055

* Wed Dec 04 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241204001040
- Update to upstream release 1.0.1.t.22.20241204001040

* Tue Dec 03 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241203001149
- Update to upstream release 1.0.1.t.22.20241203001149

* Mon Dec 02 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241202001049
- Update to upstream release 1.0.1.t.22.20241202001049

* Sun Dec 01 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241201001215
- Properly separate the twilight build from the main build

* Sun Dec 01 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241201001215
- Update to upstream release 1.0.1.t.22.20241201001215

* Sat Nov 30 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241130001045
- Update to upstream release 1.0.1.t.22.20241130001045

* Fri Nov 29 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241129001029
- Update to upstream release 1.0.1.t.22.20241129001029

* Thu Nov 28 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.22.20241128122701
- Update to upstream release 1.0.1.t.22.20241128122701

* Tue Nov 26 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.20.20241126001012
- Update to upstream release 1.0.1.t.20.20241126001012

* Mon Nov 25 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.t.20
- Update to twilight 1.0.1-t.20

* Mon Nov 25 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.19
- Initial Release of spec file to package twiligt builds
