#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : alabaster
Version  : 0.7.10
Release  : 16
URL      : http://pypi.debian.net/alabaster/alabaster-0.7.10.tar.gz
Source0  : http://pypi.debian.net/alabaster/alabaster-0.7.10.tar.gz
Source99 : http://pypi.debian.net/alabaster/alabaster-0.7.10.tar.gz.asc
Summary  : A configurable sidebar-enabled Sphinx theme
Group    : Development/Tools
License  : BSD-3-Clause
Requires: alabaster-python3
Requires: alabaster-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
==================
        
        Alabaster is a visually (c)lean, responsive, configurable theme for the `Sphinx

%package legacypython
Summary: legacypython components for the alabaster package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the alabaster package.


%package python
Summary: python components for the alabaster package.
Group: Default
Requires: alabaster-python3

%description python
python components for the alabaster package.


%package python3
Summary: python3 components for the alabaster package.
Group: Default
Requires: python3-core

%description python3
python3 components for the alabaster package.


%prep
%setup -q -n alabaster-0.7.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519395943
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519395943
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
