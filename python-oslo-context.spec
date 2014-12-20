# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.context

Name:           python-oslo-context
Version:        XXX
Release:        XXX{?dist}
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel

%description
The OpenStack Oslo Context library.
* Documentation: http://docs.openstack.org/developer/oslo.context
* Source: http://git.openstack.org/cgit/openstack/oslo.context
* Bugs: http://bugs.launchpad.net/oslo


%package doc
Summary:    Documentation for the Oslo database handling library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the Oslo database handling library.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE

%changelog
* Sat Dec 20 2014 Dan Prince <dprince@redhat.com> XXX
- Initial package.
