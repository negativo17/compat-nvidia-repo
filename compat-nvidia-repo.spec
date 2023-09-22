Name:           compat-nvidia-repo
Version:        535.113.01
Epoch:          3
Release:        1%{?dist}
Summary:        Compatibility package required by official CUDA packages
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-toolkit

BuildArch:      noarch

Requires:       nvidia-driver >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-NVML >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-NvFBCOpenGL >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-devel >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-libXNVCtrl >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-libXNVCtrl-devel >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-modprobe >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-persistenced >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-settings >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-xconfig >= %{?epoch:%{epoch}:}%{version}

Provides:       cuda-drivers >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-drivers >= %{?epoch:%{epoch}:}%{version}

%description
Nvidia drivers metapackage required by official CUDA packages. It pulls in all
Nvidia driver components.

%files
# Empty

%changelog
* Fri Sep 22 2023 Simone Caronni <negativo17@gmail.com> - 3:535.113.01-1
- Update to 535.113.01.

* Thu Aug 24 2023 Simone Caronni <negativo17@gmail.com> - 3:535.104.05-1
- Update to 535.104.05.

* Wed Aug 09 2023 Simone Caronni <negativo17@gmail.com> - 3:535.98-1
- Update to 535.98.

* Wed Jul 19 2023 Simone Caronni <negativo17@gmail.com> - 3:535.86.05-1
- Update to 535.86.05.

* Tue Jun 20 2023 Simone Caronni <negativo17@gmail.com> - 3:535.54.03-1
- Update to 535.54.03.

* Fri May 12 2023 Simone Caronni <negativo17@gmail.com> - 3:525.116.04-1
- Update to 525.116.04.

* Mon May 01 2023 Simone Caronni <negativo17@gmail.com> - 3:525.116.03-1
- Update to 525.116.03.

* Fri Feb 10 2023 Simone Caronni <negativo17@gmail.com> - 3:525.89.02-1
- Update to 525.89.02.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 3:525.85.05-1
- Update to 525.85.05.

* Mon Jan 09 2023 Simone Caronni <negativo17@gmail.com> - 3:525.78.01-1
- Update to 525.78.01.

* Tue Nov 29 2022 Simone Caronni <negativo17@gmail.com> - 3:525.60.11-1
- Update to 525.60.11.

* Thu Oct 13 2022 Simone Caronni <negativo17@gmail.com> - 3:520.56.06-1
- Update to 520.56.06.

* Wed Sep 21 2022 Simone Caronni <negativo17@gmail.com> - 3:515.76-1
- Update to 515.76.

* Mon Aug 08 2022 Simone Caronni <negativo17@gmail.com> - 3:515.65.01-1
- Update to 515.65.01.

* Wed Jun 29 2022 Simone Caronni <negativo17@gmail.com> - 3:515.57-1
- Update to 515.57.

* Thu Jun 09 2022 Simone Caronni <negativo17@gmail.com> - 3:515.48.07-1
- Update to 515.48.07.

* Tue May 31 2022 Simone Caronni <negativo17@gmail.com> - 3:510.73.05-1
- Update to 510.73.05.

* Mon May 02 2022 Simone Caronni <negativo17@gmail.com> - 3:510.68.02-1
- Update to 510.68.02.

* Mon Mar 28 2022 Simone Caronni <negativo17@gmail.com> - 3:510.60.02-1
- Update to 510.60.02.

* Mon Feb 14 2022 Simone Caronni <negativo17@gmail.com> - 3:510.54-1
- Update to 510.54.

* Wed Feb 02 2022 Simone Caronni <negativo17@gmail.com> - 3:510.47.03-1
- Update to 510.47.03.

* Tue Dec 14 2021 Simone Caronni <negativo17@gmail.com> - 3:495.46-1
- Update to 495.46.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 3:495.44-1
- Update to 495.44.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 3:470.82.00-1
- Update to 470.82.00.

* Tue Sep 21 2021 Simone Caronni <negativo17@gmail.com> - 3:470.74-1
- Update to 470.74.

* Wed Aug 11 2021 Simone Caronni <negativo17@gmail.com> - 3:470.63.01-1
- Update to 470.63.01.

* Tue Jul 20 2021 Simone Caronni <negativo17@gmail.com> - 3:470.57.02-1
- Update to 470.57.02.

* Mon Jun 07 2021 Simone Caronni <negativo17@gmail.com> - 3:460.84-1
- Update to 460.84.

* Wed May 12 2021 Simone Caronni <negativo17@gmail.com> - 3:460.80-1
- Update to 460.80.

* Sun Apr 18 2021 Simone Caronni <negativo17@gmail.com> - 3:460.73.01-1
- Update to 460.73.01.

* Fri Mar 19 2021 Simone Caronni <negativo17@gmail.com> - 3:460.67-1
- Update to 460.67.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 3:460.56-1
- Update to 460.56.

* Wed Jan 27 2021 Simone Caronni <negativo17@gmail.com> - 3:460.39-1
- Update to 460.39.

* Thu Jan  7 2021 Simone Caronni <negativo17@gmail.com> - 3:460.32.03-1
- Update to 460.32.03.

* Sun Dec 20 2020 Simone Caronni <negativo17@gmail.com> - 3:460.27.04-1
- Update to 460.27.04.

* Tue Oct 06 2020 Simone Caronni <negativo17@gmail.com> - 3:450.80.02-1
- Update to 450.80.02.

* Thu Aug 20 2020 Simone Caronni <negativo17@gmail.com> - 3:450.66-1
- Update to 450.66.

* Fri Jul 10 2020 Simone Caronni <negativo17@gmail.com> - 3:450.57-1
- Update to 450.57.

* Thu Jun 25 2020 Simone Caronni <negativo17@gmail.com> - 3:440.100-1
- Update to 440.100.

* Thu Apr 09 2020 Simone Caronni <negativo17@gmail.com> - 3:440.82-1
- Update to 440.82.

* Fri Feb 28 2020 Simone Caronni <negativo17@gmail.com> - 3:440.64-1
- Update to 440.64.

* Tue Feb 04 2020 Simone Caronni <negativo17@gmail.com> - 3:440.59-1
- Update to 440.59.

* Sat Dec 14 2019 Simone Caronni <negativo17@gmail.com> - 3:440.44-1
- Update to 440.44.

* Sat Nov 30 2019 Simone Caronni <negativo17@gmail.com> - 3:440.36-1
- Update to 440.36.

* Sat Nov 09 2019 Simone Caronni <negativo17@gmail.com> - 3:440.31-1
- Update to 440.31.

* Thu Oct 17 2019 Simone Caronni <negativo17@gmail.com> - 3:440.26-1
- Update to 440.26.

* Tue Sep 03 2019 Simone Caronni <negativo17@gmail.com> - 3:435.21-1
- Update to 435.21.

* Thu Aug 22 2019 Simone Caronni <negativo17@gmail.com> - 3:435.17-1
- Update to 435.17.

* Wed Jul 31 2019 Simone Caronni <negativo17@gmail.com> - 3:430.40-1
- Update to 430.40.

* Fri Jul 12 2019 Simone Caronni <negativo17@gmail.com> - 3:430.34-1
- Update to 430.34.

* Wed Jun 12 2019 Simone Caronni <negativo17@gmail.com> - 3:430.26-1
- Update to 430.26.

* Sat May 18 2019 Simone Caronni <negativo17@gmail.com> - 3:430.14-1
- Update to 430.14.

* Thu May 09 2019 Simone Caronni <negativo17@gmail.com> - 3:418.74-1
- Update to 418.74.

* Sun Mar 24 2019 Simone Caronni <negativo17@gmail.com> - 3:418.56-1
- Update to 418.56.

* Fri Feb 22 2019 Simone Caronni <negativo17@gmail.com> - 3:418.43-1
- Update to 418.43.

* Sun Feb  3 2019 Simone Caronni <negativo17@gmail.com> - 3:415.27-1
- First build.
