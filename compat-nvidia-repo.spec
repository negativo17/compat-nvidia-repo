Name:           compat-nvidia-repo
Version:        440.31
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
