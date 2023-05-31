#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : gphoto2
Version  : 2.5.28
Release  : 24
URL      : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.28/gphoto2-2.5.28.tar.xz
Source0  : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.28/gphoto2-2.5.28.tar.xz
Source1  : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.28/gphoto2-2.5.28.tar.xz.asc
Summary  : Command line interface to libgphoto2
Group    : Development/Tools
License  : GPL-2.0
Requires: gphoto2-bin = %{version}-%{release}
Requires: gphoto2-license = %{version}-%{release}
Requires: gphoto2-locales = %{version}-%{release}
Requires: gphoto2-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : pkgconfig(popt)
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
gphoto2 is a command line client to for the libgphoto2. It allows to
use gPhoto software from a terminal or from a script shell to perform
any camera operation that can be done. This is the main user interface.

%package bin
Summary: bin components for the gphoto2 package.
Group: Binaries
Requires: gphoto2-license = %{version}-%{release}

%description bin
bin components for the gphoto2 package.


%package doc
Summary: doc components for the gphoto2 package.
Group: Documentation
Requires: gphoto2-man = %{version}-%{release}

%description doc
doc components for the gphoto2 package.


%package license
Summary: license components for the gphoto2 package.
Group: Default

%description license
license components for the gphoto2 package.


%package locales
Summary: locales components for the gphoto2 package.
Group: Default

%description locales
locales components for the gphoto2 package.


%package man
Summary: man components for the gphoto2 package.
Group: Default

%description man
man components for the gphoto2 package.


%prep
%setup -q -n gphoto2-2.5.28
cd %{_builddir}/gphoto2-2.5.28
pushd ..
cp -a gphoto2-2.5.28 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685542908
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1685542908
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gphoto2
cp %{_builddir}/gphoto2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gphoto2/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang gphoto2
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gphoto2
/usr/bin/gphoto2

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gphoto2/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gphoto2/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gphoto2.1

%files locales -f gphoto2.lang
%defattr(-,root,root,-)

