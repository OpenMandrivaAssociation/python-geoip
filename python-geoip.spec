%define name python-geoip
%define oname GeoIP-Python

Summary: Python bindings for the GeoIP library
Name: %{name}
Version: 1.2.8
Release: 1
Source0: http://geolite.maxmind.com/download/geoip/api/python/GeoIP-Python-%{version}.tar.gz
URL: http://www.maxmind.com/app/python
License: BSD-like
Group: Development/Python
%py_requires -d
BuildRequires: libgeoip-devel

%description
This is the Python API to the GeoIP library that enables the user to
find the country that any IP address or hostname originates from. It
uses a file based database that is accurate as of March 2003. This
database simply contains IP blocks as keys, and countries as
values. This database should be more complete and accurate than using
reverse DNS lookups. Commercial databases and automatic update
services are available from http://www.maxmind.com/

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README
%py_platsitedir/*




%changelog
* Wed Nov 02 2011 Götz Waschk <waschk@mandriva.org> 1.2.4-3mdv2012.0
+ Revision: 711832
- rebuild

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 1.2.4-2mdv2011.0
+ Revision: 591473
- rebuild for new python 2.7

* Thu Jun 25 2009 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2011.0
+ Revision: 388906
- update to new version 1.2.4

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1.2.1-7mdv2009.1
+ Revision: 320169
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-6mdv2009.0
+ Revision: 259614
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2009.0
+ Revision: 247417
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 1.2.1-3mdv2007.0
+ Revision: 88299
- bot rebuild
- Import python-geoip

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.2.1-2mdv2007.1
- update file list

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdk
- New release 1.2.1

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.2.0-2mdk
- Rebuild for new python

* Thu Feb 19 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.0-1mdk
- new version



