%global             full_name zen-browser-twilight
%global             application_name zen
%global             debug_package %{nil}

Name:               zen-browser-twilight
Version:            1.7t.20250109235539
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
* Fri Jan 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250109235539
- Update to upstream release 1.7t.20250109235539

* Tue Jan 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250107115539
- Update to upstream release 1.6t.20250107115539

* Tue Jan 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250107092211
- Update to upstream release 1.6t.20250107092211

* Mon Jan 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250105235243
- Update to upstream release 1.6t.20250105235243

* Mon Jan 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250105221814
- Update to upstream release 1.6t.20250105221814

* Sun Jan 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250105145836
- Update to upstream release 1.6t.20250105145836

* Sun Jan 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250104230446
- Update to upstream release 1.6t.20250104230446

* Sun Jan 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250104200652
- Update to upstream release 1.6t.20250104200652

* Sat Jan 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250104013706
- Update to upstream release 1.6t.20250104013706

* Fri Jan 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.20250103161901
- Update to upstream release 1.6t.20250103161901

* Fri Jan 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250103010552
- Update to upstream release 1.2.t.6.20250103010552

* Thu Jan 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250102160952
- Update to upstream release 1.2.t.6.20250102160952

* Thu Jan 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250102130100
- Update to upstream release 1.2.t.6.20250102130100

* Thu Jan 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250102000944
- Update to upstream release 1.2.t.6.20250102000944

* Wed Jan 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250101104335
- Update to upstream release 1.2.t.6.20250101104335

* Wed Jan 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20250101021217
- Update to upstream release 1.2.t.6.20250101021217

* Tue Dec 31 2024 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20241231045420
- Update to upstream release 1.2.t.6.20241231045420

* Mon Dec 30 2024 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20241230160906
- Update to upstream release 1.2.t.6.20241230160906

* Mon Dec 30 2024 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20241230001029
- Update to upstream release 1.2.t.6.20241230001029

* Sun Dec 29 2024 ArchitektApx <architektapx@gehinors.ch> - 1.2.t.6.20241229001218
- Update to upstream release 1.2.t.6.20241229001218

* Sat Dec 28 2024 ArchitektApx <architektapx@gehinors.ch> - 1.2t.6.20241228000949
- Update to upstream release 1.2t.6.20241228000949

* Wed Dec 25 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.6.20241225190501
- Update to upstream release 1.0.2.t.6.20241225190501

* Wed Dec 25 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.6.20241225123427
- Update to upstream release 1.0.2.t.6.20241225123427

* Wed Dec 25 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.6.20241225000939
- Update to upstream release 1.0.2.t.6.20241225000939

* Tue Dec 24 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.6.20241224113255
- Update to upstream release 1.0.2.t.6.20241224113255

* Tue Dec 24 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.5.20241223202635
- Update to upstream release 1.0.2.t.5.20241223202635

* Mon Dec 23 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.5.20241222231426
- Update to upstream release 1.0.2.t.5.20241222231426

* Sat Dec 21 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.4.20241221002510
- Update to upstream release 1.0.2.t.4.20241221002510

* Fri Dec 20 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.4.20241219195209
- Update to upstream release 1.0.2.t.4.20241219195209

* Thu Dec 19 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.4.20241219073300
- Update to upstream release 1.0.2.t.4.20241219073300

* Wed Dec 18 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.3.20241218001025
- Update to upstream release 1.0.2.t.3.20241218001025

* Wed Dec 18 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.3.20241217211556
- Update to upstream release 1.0.2.t.3.20241217211556

* Tue Dec 17 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.3.20241217001024
- Update to upstream release 1.0.2.t.3.20241217001024

* Sun Dec 15 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.3.20241215001128
- Update to upstream release 1.0.2.t.3.20241215001128

* Sun Dec 15 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.3.20241214213441
- Update to upstream release 1.0.2.t.3.20241214213441

* Fri Dec 13 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.2.20241213004942
- Update to upstream release 1.0.2.t.2.20241213004942

* Thu Dec 12 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.2.20241212001043
- Update to upstream release 1.0.2.t.2.20241212001043

* Wed Dec 11 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.2.20241211164440
- Update to upstream release 1.0.2.t.2.20241211164440

* Wed Dec 11 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.t.2.20241211001330
- Update to upstream release 1.0.2.t.2.20241211001330

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
