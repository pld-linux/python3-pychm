%define		module	pychm
Summary:	PyCHM is a Python library to manipulate CHM files (Microsoft HTML Help)
Name:		python3-%{module}
Version:	0.8.6
Release:	2
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pychm/%{module}-%{version}.tar.gz
# Source0-md5:	c83c0f292131fc80df662d372fc96ee3
URL:		https://github.com/dottedmag/pychm
BuildRequires:	chmlib-devel
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyCHM is a Python library to manipulate CHM files (Microsoft HTML
Help).

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%dir %{py3_sitedir}/chm
%{py3_sitedir}/chm/__pycache__
%{py3_sitedir}/chm/*.py
%attr(755,root,root) %{py3_sitedir}/chm/*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
