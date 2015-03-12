# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.context

Name:           python-oslo-context
Version:        XXX
Release:        XXX%{?dist}
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/oslo.context
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-setuptools
Requires:       python-babel
Requires:       pytz

%description
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package doc
Summary:        Documentation for the OpenStack Oslo context library

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the OpenStack Oslo context library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.rst README.rst PKG-INFO ChangeLog
%{python2_sitelib}/oslo_context
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files doc
%doc doc/build/html

%changelog
* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-3
- Fixes typo in spec file

* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-2
- Added docs

* Thu Mar 12 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-1
- Updated the spec file for oslo-context 0.2.0 release

* Sat Dec 20 2014 Dan Prince <dprince@redhat.com> -XXX
- Initial package.
