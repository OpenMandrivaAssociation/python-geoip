%define oname GeoIP-Python

Summary: Python bindings for the GeoIP library
Name:    python-geoip
Version: 1.2.8
Release: 1
Source0: http://geolite.maxmind.com/download/geoip/api/python/GeoIP-Python-%{version}.tar.gz
URL: http://www.maxmind.com/app/python
License: BSD-like
Group: Development/Python

BuildRequires: pkgconfig(geoip)
BuildRequires: python-devel

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
%{py_platsitedir}/*

