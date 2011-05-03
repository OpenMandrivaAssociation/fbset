%define name fbset
%define version 2.1
%define release %mkrel 23

Summary: Framebuffer utilities for changing video modes
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Kernel and hardware
Source: fbset-%{version}.tar.bz2
Patch: fbset-2.0-pre-19981028.patch
Patch2: fbset-2.1-mdkconf.patch
BuildRequires: bison flex bzip2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
fbset is a utility for querying and changing video modes of fbcon consoles.

%prep
%setup -q
%patch -p1
%patch2 -p1 -b .mdkconf

perl -pi -e 's|geometry 10224 768 10224 768 8|geometry 1024 768 1024 768 8|' etc/fb.modes.ATI
perl -pi -e 's|geometry 1024 1024 1024 1024 8|geometry 1280 1024 1280 1024 8|' etc/fb.modes.ATI

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
#make install PREFIX=$RPM_BUILD_ROOT
install %{name} -D $RPM_BUILD_ROOT%{_sbindir}/%{name}
bzip2 %{name}.8 fb.modes.5
install %{name}.8.bz2 -D $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8.bz2
install fb.modes.5.bz2 -D $RPM_BUILD_ROOT%{_mandir}/man5/fb.modes.bz2

## It's a useable default not perfect but ..
#%ifarch sparc sparc64
install etc/fb.modes.ATI -D $RPM_BUILD_ROOT%{_sysconfdir}/fb.modes
#%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#/dev/*
%{_sbindir}/%{name}
%{_mandir}/man[58]/*
#%ifarch sparc sparc64
%config(noreplace) %{_sysconfdir}/fb.modes
#%endif

