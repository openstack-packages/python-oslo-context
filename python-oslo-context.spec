# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.context

Name:           python-oslo-context
Version:        0.2.0
Release:        1%{?dist}
Summary:        OpenStack Oslo Context library

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/oslo.context
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-setuptools
Requires:       python-babel
Requires:       python-pytz


%description
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc %{license}
%{python2_sitelib}/
%{python2_sitelib}/oslo_context
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Thu Mar 12 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-1
- Updated the spec file for oslo-context 0.2.0 release

* Sat Dec 20 2014 Dan Prince <dprince@redhat.com> -XXX
- Initial package.
