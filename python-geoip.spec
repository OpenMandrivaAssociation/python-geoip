%define oname GeoIP

Summary: Python bindings for the GeoIP library


Name: python-geoip
Version:	1.3.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/f2/7b/a463b7c3df8ef4b9c92906da29ddc9e464d4045f00c475ad31cdb9a97aae/GeoIP-1.3.2.tar.gz
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




