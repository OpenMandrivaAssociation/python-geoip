%define name python-geoip
%define version 1.2.1
%define release %mkrel 7
%define oname GeoIP-Python

Summary: Python bindings for the GeoIP library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.maxmind.com/download/geoip/api/python/%{oname}-%{version}.tar.bz2
URL: http://www.maxmind.com/app/python
License: BSD-like
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
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
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%py_platsitedir/*


