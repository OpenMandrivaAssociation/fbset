%define name fbset
%define version 2.1
%define release %mkrel 24

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1-23mdv2011.0
+ Revision: 664298
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-22mdv2011.0
+ Revision: 605120
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-21mdv2010.1
+ Revision: 522626
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1-20mdv2010.0
+ Revision: 424429
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.1-19mdv2009.1
+ Revision: 350985
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1-18mdv2009.0
+ Revision: 220785
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.1-17mdv2008.1
+ Revision: 149717
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 2.1-16mdv2008.0
+ Revision: 18881
- clean spec, bzip manpages, rebuild for new era


* Sun May 14 2006 Stefan van der Eijk <stefan@eijk.nu> 2.1-15mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.1-14mdk
- Rebuild

* Tue Oct 05 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.1-13mdk
- fix deps for build

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.1-12mdk
- rebuild
- macroize

