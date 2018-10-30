%define debug_package %{nil}

Summary:	Framebuffer utilities for changing video modes
Name:		fbset
Version:	2.1
Release:	34
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://users.telenet.be/geertu/Linux/fbdev/
Source0:	http://users.telenet.be/geertu/Linux/fbdev/%{name}-%{version}.tar.gz
Patch0:		fbset-2.0-pre-19981028.patch
Patch2:		fbset-2.1-mdkconf.patch
BuildRequires:	bison
BuildRequires:	bzip2
BuildRequires:	flex

%description
fbset is a utility for querying and changing video modes of fbcon consoles.

%prep
%setup -q
%apply_patches

sed -i -e 's|geometry 10224 768 10224 768 8|geometry 1024 768 1024 768 8|' etc/fb.modes.ATI
sed -i -e 's|geometry 1024 1024 1024 1024 8|geometry 1280 1024 1280 1024 8|' etc/fb.modes.ATI

%build
%make

%install
install %{name} -D %{buildroot}%{_sbindir}/%{name}
install %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8
install fb.modes.5 -D %{buildroot}%{_mandir}/man5/fb.modes.5

install etc/fb.modes.ATI -D %{buildroot}%{_sysconfdir}/fb.modes

%files
%config(noreplace) %{_sysconfdir}/fb.modes
%{_sbindir}/%{name}
%{_mandir}/man[58]/*

