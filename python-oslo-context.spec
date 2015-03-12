# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.context

Name:           python-oslo-context
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/oslo.context
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel

%description
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package doc
Summary:        Documentation for the OpenStack Oslo context library
Group:          Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures

%description doc
Documentation for the OpenStack Oslo context library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
rm -f requirements.txt

%build
%{__python2} setup.py build
# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx

# Remove the sphinx-build leftovers
rm -fr doc/build/html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html

%changelog
