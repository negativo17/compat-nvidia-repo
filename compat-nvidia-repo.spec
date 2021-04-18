Name:           compat-nvidia-repo
Version:        465.24.02
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
* Sun Apr 18 2021 Simone Caronni <negativo17@gmail.com> - 3:465.24.02-1
- Update to 465.24.02.

* Fri Apr 09 2021 Simone Caronni <negativo17@gmail.com> - 3:465.19.01-1
- Update to 465.19.01.

* Fri Mar 19 2021 Simone Caronni <negativo17@gmail.com> - 3:460.67-1
- Update to 460.67.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 3:460.56-1
- Update to 460.56.

* Wed Jan 27 2021 Simone Caronni <negativo17@gmail.com> - 3:460.39-1
- Update to 460.39.

* Thu Jan  7 2021 Simone Caronni <negativo17@gmail.com> - 3:460.32.03-1
- Update to 460.32.03.

* Sun Dec 20 14:39:19 CET 2020 Simone Caronni <negativo17@gmail.com> - 3:460.27.04-1
- Update to 460.27.04.

* Wed Nov 18 2020 Simone Caronni <negativo17@gmail.com> - 3:455.45.01-1
- Update to 455.45.01.

* Mon Nov 02 2020 Simone Caronni <negativo17@gmail.com> - 3:455.38-1
- Update to 455.38.

* Mon Oct 12 2020 Simone Caronni <negativo17@gmail.com> - 3:455.28-1
- Update to 455.28.

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
