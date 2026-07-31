Name:		python-treq
Version:	26.7.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/treq/treq-%{version}.tar.gz
Summary:	High-level Twisted HTTP Client API
URL:		https://pypi.org/project/treq/
License:	MIT/X
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(incremental)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
High-level Twisted HTTP Client API

%prep
%autosetup -p1 -n treq-26.7.0

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/treq
%{py_sitedir}/treq-%{version}.dist-info
