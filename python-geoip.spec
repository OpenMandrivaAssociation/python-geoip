%define oname GeoIP

Summary: Python bindings for the GeoIP library


Name: python-geoip
Version: 1.3.1
Release: 2
Source0: http://www.maxmind.com/download/geoip/api/python/GeoIP-%{version}.tar.gz
URL: http://www.maxmind.com/app/python
License: BSD-like
Group: Development/Python
BuildRequires:  python-devel
BuildRequires: pkgconfig(geoip)

%description
This is the Python API to the GeoIP library that enables the user to
find the country that any IP address or hostname originates from. It
uses a file based database that is accurate as of March 2003. This
database simply contains IP blocks as keys, and countries as
values. This database should be more complete and accurate than using
reverse DNS lookups. Commercial databases and automatic update
services are available from http://www.maxmind.com/

%prep
%setup -q -n %oname-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_platsitedir}/*




