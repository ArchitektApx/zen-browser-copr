%global             full_name zen-browser
%global             application_name zen
%global             debug_package %{nil}

Name:               zen-browser
Version:            1.15.2b
Release:            1%{?dist}
Summary:            Zen Browser

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/1.15.2b/zen.linux-aarch64.tar.xz
Source1:            %{full_name}.desktop
Source2:            policies.json
Source3:            %{full_name}

ExclusiveArch:      aarch64

Recommends:         (plasma-browser-integration if plasma-workspace)
Recommends:         (gnome-browser-connector if gnome-shell)

Requires(post):     gtk-update-icon-cache

%description
This is a package of the Zen web browser for aarch64. 
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

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

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
* Fri Aug 29 2025 ArchitektApx <architektapx@gehinors.ch> - 1.15.2b
- Update to upstream release 1.15.2b

* Fri Aug 29 2025 ArchitektApx <architektapx@gehinors.ch> - 1.15.1b
- Update to upstream release 1.15.1b

* Wed Aug 27 2025 ArchitektApx <architektapx@gehinors.ch> - 1.15b
- Update to upstream release 1.15b

* Wed Aug 27 2025 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Mon Aug 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.11b
- Update to upstream release 1.14.11b

* Thu Aug 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.10b
- Update to upstream release 1.14.10b

* Mon Jul 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.9b
- Update to upstream release 1.14.9b

* Sun Jul 27 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.8b
- Update to upstream release 1.14.8b

* Sat Jul 26 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.7b
- Update to upstream release 1.14.7b

* Fri Jul 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.6b
- Update to upstream release 1.14.6b

* Mon Jul 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.5b
- Update to upstream release 1.14.5b

* Sat Jul 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.4b
- Update to upstream release 1.14.4b

* Thu Jul 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.3b
- Update to upstream release 1.14.3b

* Sat Jul 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.2b
- Update to upstream release 1.14.2b

* Fri Jul 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.1b
- Update to upstream release 1.14.1b

* Fri Jul 04 2025 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Wed Jul 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14.1b
- Update to upstream release 1.14.1b

* Wed Jul 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14b
- Update to upstream release 1.14b

* Tue Jul 01 2025 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Mon Jun 30 2025 ArchitektApx <architektapx@gehinors.ch> - 1.14b
- Update to upstream release 1.14b

* Fri Jun 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.13.2b
- Update to upstream release 1.13.2b

* Thu Jun 19 2025 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Tue Jun 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.13.2b
- Update to upstream release 1.13.2b

* Sun Jun 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.13.1b
- Update to upstream release 1.13.1b

* Sat Jun 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.13b
- Update to upstream release 1.13b

* Mon Jun 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.10b
- Update to upstream release 1.12.10b

* Sat May 31 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.9b
- Update to upstream release 1.12.9b

* Fri May 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.8b
- Update to upstream release 1.12.8b

* Thu May 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.7b
- Update to upstream release 1.12.7b

* Wed May 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.6b
- Update to upstream release 1.12.6b

* Thu May 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.5b
- Update to upstream release 1.12.5b

* Wed May 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.4b
- Update to upstream release 1.12.4b

* Fri May 09 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.3b
- Update to upstream release 1.12.3b

* Thu May 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.2b
- Update to upstream release 1.12.2b

* Thu May 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.1b
- Update to upstream release 1.12.1b

* Wed May 07 2025 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Mon May 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12.1b
- Update to upstream release 1.12.1b

* Sat May 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.12b
- Update to upstream release 1.12b

* Sun Apr 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.5b
- Update to upstream release 1.11.5b

* Fri Apr 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.4b
- Update to upstream release 1.11.4b

* Wed Apr 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.2b
- Update to upstream release 1.11.2b

* Tue Apr 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.3b
- Update to upstream release 1.11.3b

* Sat Apr 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.2b
- Update to upstream release 1.11.2b

* Sat Apr 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11.1b
- Update to upstream release 1.11.1b

* Fri Apr 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.11b
- Update to upstream release 1.11b

* Fri Mar 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10.3b
- Update to upstream release 1.10.3b

* Wed Mar 26 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10.2b
- Update to upstream release 1.10.2b

* Sat Mar 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10.1b
- Update to upstream release 1.10.1b

* Wed Mar 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10b
- Update to upstream release 1.10b

* Thu Mar 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1b
- Update to upstream release 1.9.1b

* Sat Mar 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9b
- Update to upstream release 1.9b

* Wed Feb 26 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2b
- Update to upstream release 1.8.2b

* Tue Feb 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1b
- Update to upstream release 1.8.1b

* Mon Feb 24 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8b
- Update to upstream release 1.8b

* Sat Feb 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6b
- Fix upstream release url to use xz instead of bz2 archives
- Update to upstream release 1.7.6b

* Sat Feb 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.5b
- Update to upstream release 1.7.5b

* Fri Jan 31 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4b
- Update to upstream release 1.7.4b

* Fri Jan 31 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.3b
- Update to upstream release 1.7.3b

* Thu Jan 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2b
- Update to upstream release 1.7.2b

* Mon Jan 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.1b
- Update to upstream release 1.7.1b

* Thu Jan 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7b
- Update to upstream release 1.7b

* Fri Jan 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6b
- Update to upstream release 1.6b

* Tue Dec 24 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.5
- Update to upstream release 1.0.2-b.5

* Tue Dec 24 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.4
- Update to upstream release 1.0.2-b.4

* Fri Dec 20 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.3
- Update to upstream release 1.0.2-b.3

* Sun Dec 15 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.2
- Update to upstream release 1.0.2-b.2

* Thu Dec 12 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.1
- Update to upstream release 1.0.2-b.1

* Tue Dec 10 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.2.b.0
- Update to upstream release 1.0.2-b.0

* Thu Nov 28 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.22
- Manual Update to upstream release 1.0.1-a.22 due to bugs in 1.0.1-a.20 and 1.0.1-a.21
- Upstream aarch64 builds were removed

* Thu Nov 28 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.21
- Update to upstream release 1.0.1-a.21

* Wed Nov 27 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.20
- Update to upstream release 1.0.1-a.20

* Tue Nov 19 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.19
- Upstream: Fix: adjust vertical tab background opacity for improved visibility

* Sat Nov 16 2024 ArchitektApx <architektapx@gehinors.ch> - 1.0.1.a.18
- Upstream: (style) Modify button active state to exclude workspace button
- Inital arm64 build release
