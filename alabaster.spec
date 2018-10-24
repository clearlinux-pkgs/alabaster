#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : alabaster
Version  : 0.7.12
Release  : 25
URL      : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz
Source99 : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz.asc
Summary  : A configurable sidebar-enabled Sphinx theme
Group    : Development/Tools
License  : BSD-3-Clause
Requires: alabaster-license = %{version}-%{release}
Requires: alabaster-python = %{version}-%{release}
Requires: alabaster-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : python-core
BuildRequires : setuptools-legacypython

%description
==================
        
        Alabaster is a visually (c)lean, responsive, configurable theme for the `Sphinx

%package legacypython
Summary: legacypython components for the alabaster package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the alabaster package.


%package license
Summary: license components for the alabaster package.
Group: Default

%description license
license components for the alabaster package.


%package python
Summary: python components for the alabaster package.
Group: Default
Requires: alabaster-python3 = %{version}-%{release}

%description python
python components for the alabaster package.


%package python3
Summary: python3 components for the alabaster package.
Group: Default
Requires: python3-core

%description python3
python3 components for the alabaster package.


%prep
%setup -q -n alabaster-0.7.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538597102
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1538597102
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alabaster
cp LICENSE %{buildroot}/usr/share/package-licenses/alabaster/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alabaster/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
