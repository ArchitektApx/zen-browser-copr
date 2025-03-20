%global             full_name zen-browser-twilight
%global             application_name zen
%global             debug_package %{nil}

Name:               zen-browser-twilight
Version:            1.10.1t.20250320190610
Release:            1%{?dist}
Summary:            Zen Browser Twilight Build

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/twilight/zen.linux-aarch64.tar.xz
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
* Thu Mar 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10.1t.20250320190610
- Update to upstream release 1.10.1t.20250320190610

* Thu Mar 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250320123712
- Update to upstream release 1.10t.20250320123712

* Thu Mar 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250319230342
- Update to upstream release 1.10t.20250319230342

* Wed Mar 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250318230319
- Update to upstream release 1.10t.20250318230319

* Tue Mar 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250318144736
- Update to upstream release 1.10t.20250318144736

* Tue Mar 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250317232409
- Update to upstream release 1.10t.20250317232409

* Mon Mar 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250317134126
- Update to upstream release 1.10t.20250317134126

* Mon Mar 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250316230317
- Update to upstream release 1.10t.20250316230317

* Sun Mar 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250316151037
- Update to upstream release 1.10t.20250316151037

* Sat Mar 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250315183701
- Update to upstream release 1.10t.20250315183701

* Sat Mar 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250315154628
- Update to upstream release 1.10t.20250315154628

* Sat Mar 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250315124121
- Update to upstream release 1.10t.20250315124121

* Sat Mar 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250315093810
- Update to upstream release 1.10t.20250315093810

* Sat Mar 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250314230327
- Update to upstream release 1.10t.20250314230327

* Fri Mar 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250314173011
- Update to upstream release 1.10t.20250314173011

* Fri Mar 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.10t.20250314122150
- Update to upstream release 1.10t.20250314122150

* Wed Mar 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250311230326
- Update to upstream release 1.9.1t.20250311230326

* Tue Mar 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250311181423
- Update to upstream release 1.9.1t.20250311181423

* Tue Mar 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250310230330
- Update to upstream release 1.9.1t.20250310230330

* Mon Mar 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250310154355
- Update to upstream release 1.9.1t.20250310154355

* Mon Mar 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250310122904
- Update to upstream release 1.9.1t.20250310122904

* Mon Mar 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250309232454
- Update to upstream release 1.9.1t.20250309232454

* Sun Mar 09 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9.1t.20250309143521
- Update to upstream release 1.9.1t.20250309143521

* Sun Mar 09 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250308230318
- Update to upstream release 1.9t.20250308230318

* Sun Mar 09 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250308184630
- Update to upstream release 1.9t.20250308184630

* Sat Mar 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250307230332
- Update to upstream release 1.9t.20250307230332

* Fri Mar 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250307164229
- Update to upstream release 1.9t.20250307164229

* Fri Mar 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250306230335
- Update to upstream release 1.9t.20250306230335

* Thu Mar 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250306194108
- Update to upstream release 1.9t.20250306194108

* Thu Mar 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250306151154
- Update to upstream release 1.9t.20250306151154

* Thu Mar 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250306115655
- Update to upstream release 1.9t.20250306115655

* Thu Mar 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250305230355
- Update to upstream release 1.9t.20250305230355

* Wed Mar 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.9t.20250305191849
- Update to upstream release 1.9t.20250305191849

* Wed Mar 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250305120634
- Update to upstream release 1.8.2t.20250305120634

* Wed Mar 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250304230325
- Update to upstream release 1.8.2t.20250304230325

* Wed Mar 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250304194758
- Update to upstream release 1.8.2t.20250304194758

* Tue Mar 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250304142207
- Update to upstream release 1.8.2t.20250304142207

* Tue Mar 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250303232338
- Update to upstream release 1.8.2t.20250303232338

* Mon Mar 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250303095711
- Update to upstream release 1.8.2t.20250303095711

* Mon Mar 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250303001912
- Update to upstream release 1.8.2t.20250303001912

* Mon Mar 03 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250302203742
- Update to upstream release 1.8.2t.20250302203742

* Sun Mar 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250302172218
- Update to upstream release 1.8.2t.20250302172218

* Sun Mar 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250302160456
- Update to upstream release 1.8.2t.20250302160456

* Sun Mar 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250302130349
- Update to upstream release 1.8.2t.20250302130349

* Sun Mar 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250302103306
- Update to upstream release 1.8.2t.20250302103306

* Sun Mar 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250301220242
- Update to upstream release 1.8.2t.20250301220242

* Sat Mar 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250301182015
- Update to upstream release 1.8.2t.20250301182015

* Sat Mar 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250301132505
- Update to upstream release 1.8.2t.20250301132505

* Sat Mar 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250228230325
- Update to upstream release 1.8.2t.20250228230325

* Sat Mar 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250228215916
- Update to upstream release 1.8.2t.20250228215916

* Fri Feb 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250228073817
- Update to upstream release 1.8.2t.20250228073817

* Fri Feb 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250227233111
- Update to upstream release 1.8.2t.20250227233111

* Wed Feb 26 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250225231144
- Update to upstream release 1.8.2t.20250225231144

* Tue Feb 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.2t.20250225174834
- Update to upstream release 1.8.2t.20250225174834

* Tue Feb 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1t.20250225142538
- Update to upstream release 1.8.1t.20250225142538

* Tue Feb 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1t.20250224190845
- Update to upstream release 1.8.1t.20250224190845

* Mon Feb 24 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1t.20250224095552
- Update to upstream release 1.8.1t.20250224095552

* Mon Feb 24 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8.1t.20250224072318
- Update to upstream release 1.8.1t.20250224072318

* Mon Feb 24 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250223230317
- Update to upstream release 1.8t.20250223230317

* Sun Feb 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250223124955
- Update to upstream release 1.8t.20250223124955

* Sun Feb 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250223081220
- Update to upstream release 1.8t.20250223081220

* Sun Feb 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222234806
- Update to upstream release 1.8t.20250222234806

* Sun Feb 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222200117
- Update to upstream release 1.8t.20250222200117

* Sat Feb 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222172113
- Update to upstream release 1.8t.20250222172113

* Sat Feb 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222151236
- Update to upstream release 1.8t.20250222151236

* Sat Feb 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222113642
- Update to upstream release 1.8t.20250222113642

* Sat Feb 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222090019
- Update to upstream release 1.8t.20250222090019

* Sat Feb 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250222000127
- Update to upstream release 1.8t.20250222000127

* Fri Feb 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250221174001
- Update to upstream release 1.8t.20250221174001

* Fri Feb 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250221155131
- Update to upstream release 1.8t.20250221155131

* Fri Feb 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250221114206
- Update to upstream release 1.8t.20250221114206

* Fri Feb 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250221002648
- Update to upstream release 1.8t.20250221002648

* Fri Feb 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250220221849
- Update to upstream release 1.8t.20250220221849

* Thu Feb 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250219232639
- Update to upstream release 1.8t.20250219232639

* Wed Feb 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250219121309
- Update to upstream release 1.8t.20250219121309

* Wed Feb 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250218233255
- Update to upstream release 1.8t.20250218233255

* Wed Feb 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250218200659
- Update to upstream release 1.8t.20250218200659

* Tue Feb 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250217232520
- Update to upstream release 1.8t.20250217232520

* Mon Feb 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250217183150
- Update to upstream release 1.8t.20250217183150

* Mon Feb 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.8t.20250217112809
- Update to upstream release 1.8t.20250217112809

* Mon Feb 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250217090937
- Update to upstream release 1.7.7t.20250217090937

* Mon Feb 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250217001029
- Update to upstream release 1.7.7t.20250217001029

* Sun Feb 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250216160719
- Update to upstream release 1.7.7t.20250216160719

* Sun Feb 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250216065150
- Update to upstream release 1.7.7t.20250216065150

* Sun Feb 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250215234905
- Update to upstream release 1.7.7t.20250215234905

* Sat Feb 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250214191403
- Update to upstream release 1.7.7t.20250214191403

* Fri Feb 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250214160230
- Update to upstream release 1.7.7t.20250214160230

* Fri Feb 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250214103908
- Update to upstream release 1.7.7t.20250214103908

* Fri Feb 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250213234606
- Update to upstream release 1.7.7t.20250213234606

* Thu Feb 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250213181827
- Update to upstream release 1.7.7t.20250213181827

* Thu Feb 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250213101722
- Update to upstream release 1.7.7t.20250213101722

* Thu Feb 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250212204016
- Update to upstream release 1.7.7t.20250212204016

* Thu Feb 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250212192933
- Update to upstream release 1.7.7t.20250212192933

* Wed Feb 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250212114035
- Update to upstream release 1.7.7t.20250212114035

* Wed Feb 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250212100006
- Update to upstream release 1.7.7t.20250212100006

* Tue Feb 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250211124632
- Update to upstream release 1.7.7t.20250211124632

* Tue Feb 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250210230330
- Update to upstream release 1.7.7t.20250210230330

* Mon Feb 10 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250209230326
- Update to upstream release 1.7.7t.20250209230326

* Sun Feb 09 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250208230335
- Update to upstream release 1.7.7t.20250208230335

* Sat Feb 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250208140201
- Update to upstream release 1.7.7t.20250208140201

* Sat Feb 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250208091014
- Update to upstream release 1.7.7t.20250208091014

* Sat Feb 08 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.7t.20250207230320
- Update to upstream release 1.7.7t.20250207230320

* Fri Feb 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250207133946
- Update to upstream release 1.7.6t.20250207133946

* Fri Feb 07 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250207004702
- Update to upstream release 1.7.6t.20250207004702

* Thu Feb 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250206175143
- Update to upstream release 1.7.6t.20250206175143

* Thu Feb 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250205230330
- Update to upstream release 1.7.6t.20250205230330

* Thu Feb 06 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250205202324
- Update to upstream release 1.7.6t.20250205202324

* Wed Feb 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250205142109
- Update to upstream release 1.7.6t.20250205142109

* Wed Feb 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250205064122
- Update to upstream release 1.7.6t.20250205064122

* Wed Feb 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.6t.20250204233807
- Update to upstream release 1.7.6t.20250204233807

* Wed Feb 05 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.5t.20250204190528
- Update to upstream release 1.7.5t.20250204190528

* Tue Feb 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.5t.20250204101736
- Update to upstream release 1.7.5t.20250204101736

* Tue Feb 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250203230333
- Fix upstream release url to use xz instead of bz2 archives
- Update to upstream release 1.7.2t.20250203230333

* Tue Feb 04 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250203203956
- Update to upstream release 1.7.2t.20250203203956

* Sun Feb 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4t.20250202165854
- Update to upstream release 1.7.4t.20250202165854

* Sun Feb 02 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4t.20250201231222
- Update to upstream release 1.7.4t.20250201231222

* Sat Feb 01 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4t.20250201093405
- Update to upstream release 1.7.4t.20250201093405

* Fri Jan 31 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4t.20250130230343
- Update to upstream release 1.7.4t.20250130230343

* Fri Jan 31 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.4t.20250130220508
- Update to upstream release 1.7.4t.20250130220508

* Thu Jan 30 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250130131215
- Update to upstream release 1.7.2t.20250130131215

* Thu Jan 30 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250130061301
- Update to upstream release 1.7.2t.20250130061301

* Thu Jan 30 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250129234032
- Update to upstream release 1.7.2t.20250129234032

* Tue Jan 28 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250127233450
- Update to upstream release 1.7.2t.20250127233450

* Mon Jan 27 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250127002411
- Update to upstream release 1.7.2t.20250127002411

* Mon Jan 27 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250126204128
- Update to upstream release 1.7.2t.20250126204128

* Sun Jan 26 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250125230324
- Update to upstream release 1.7.2t.20250125230324

* Sat Jan 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250125010251
- Update to upstream release 1.7.2t.20250125010251

* Sat Jan 25 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250124202521
- Update to upstream release 1.7.2t.20250124202521

* Fri Jan 24 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250123230336
- Update to upstream release 1.7.2t.20250123230336

* Thu Jan 23 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250123131101
- Update to upstream release 1.7.2t.20250123131101

* Wed Jan 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250122103820
- Update to upstream release 1.7.2t.20250122103820

* Wed Jan 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250122054504
- Update to upstream release 1.7.2t.20250122054504

* Wed Jan 22 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250121221815
- Update to upstream release 1.7.2t.20250121221815

* Tue Jan 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250121174601
- Update to upstream release 1.7.2t.20250121174601

* Tue Jan 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7.2t.20250120230320
- Update to upstream release 1.7.2t.20250120230320

* Tue Jan 21 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250120214830
- Update to upstream release 1.7t.20250120214830

* Mon Jan 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250120154732
- Update to upstream release 1.7t.20250120154732

* Mon Jan 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250120072322
- Update to upstream release 1.7t.20250120072322

* Mon Jan 20 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250119193233
- Update to upstream release 1.7t.20250119193233

* Sun Jan 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250119163012
- Update to upstream release 1.7t.20250119163012

* Sun Jan 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250119120133
- Update to upstream release 1.7t.20250119120133

* Sun Jan 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250118230325
- Update to upstream release 1.7t.20250118230325

* Sun Jan 19 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250118213911
- Update to upstream release 1.7t.20250118213911

* Sat Jan 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250118100112
- Update to upstream release 1.7t.20250118100112

* Sat Jan 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250118003745
- Update to upstream release 1.7t.20250118003745

* Sat Jan 18 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250117192928
- Update to upstream release 1.7t.20250117192928

* Fri Jan 17 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250116230355
- Update to upstream release 1.7t.20250116230355

* Thu Jan 16 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250115230348
- Update to upstream release 1.7t.20250115230348

* Wed Jan 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250115160907
- Update to upstream release 1.7t.20250115160907

* Wed Jan 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250114230320
- Update to upstream release 1.7t.20250114230320

* Wed Jan 15 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250114194505
- Update to upstream release 1.7t.20250114194505

* Tue Jan 14 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250113230612
- Update to upstream release 1.7t.20250113230612

* Mon Jan 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.1.20250113155623
- Update to upstream release 1.6t.1.20250113155623

* Mon Jan 13 2025 ArchitektApx <architektapx@gehinors.ch> - 1.6t.1.20250112234610
- Update to upstream release 1.6t.1.20250112234610

* Sun Jan 12 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250112000721
- Update to upstream release 1.7t.20250112000721

* Sat Jan 11 2025 ArchitektApx <architektapx@gehinors.ch> - 1.7t.20250110230347
- Update to upstream release 1.7t.20250110230347

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
