%global pypi_name oslo.context
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?_licensedir:%global license %%doc}

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-oslo-context
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/oslo.context
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python2-%{pypi_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python2-%{pypi_name}}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{pypi_name} = %{upstream_version}
Obsoletes:      python-%{pypi_name} < %{upstream_version}

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel

%description -n python2-%{pypi_name}
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python2-%{pypi_name}-doc
Summary:        Documentation for the OpenStack Oslo context library
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{pypi_name}-doc = %{upstream_version}
Obsoletes:      python-%{pypi_name}-doc < %{upstream_version}

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures

%description -n python2-%{pypi_name}-doc
Documentation for the OpenStack Oslo context library.

# python3
%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr

Requires:       python3-babel

%description -n python3-%{pypi_name}
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python3-%{pypi_name}-doc
Summary:        Documentation for the OpenStack Oslo context library
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-fixtures

%description -n python3-%{pypi_name}-doc
Documentation for the OpenStack Oslo context library.
%endif

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

%if 0%{?with_python3}
%{__python3} setup.py build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_context
%{python3_sitelib}/*.egg-info
%endif

%files -n python2-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html

%if 0%{?with_python3}
%files -n python3-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
