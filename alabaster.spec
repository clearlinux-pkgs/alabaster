#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : alabaster
Version  : 0.7.12
Release  : 37
URL      : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz
Source1  : https://files.pythonhosted.org/packages/cc/b4/ed8dcb0d67d5cfb7f83c4d5463a7614cb1d078ad7ae890c9143edebbf072/alabaster-0.7.12.tar.gz.asc
Summary  : A configurable sidebar-enabled Sphinx theme
Group    : Development/Tools
License  : BSD-3-Clause
Requires: alabaster-license = %{version}-%{release}
Requires: alabaster-python = %{version}-%{release}
Requires: alabaster-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
What is Alabaster?
==================
Alabaster is a visually (c)lean, responsive, configurable theme for the `Sphinx
<http://sphinx-doc.org>`_ documentation system. It is Python 2+3 compatible.

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
Provides: pypi(alabaster)

%description python3
python3 components for the alabaster package.


%prep
%setup -q -n alabaster-0.7.12
cd %{_builddir}/alabaster-0.7.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585319796
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alabaster
cp %{_builddir}/alabaster-0.7.12/LICENSE %{buildroot}/usr/share/package-licenses/alabaster/04da7d4f55379e4b1055b4b9ee2d14a2706a334c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alabaster/04da7d4f55379e4b1055b4b9ee2d14a2706a334c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
