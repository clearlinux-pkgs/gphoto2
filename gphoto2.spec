#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : gphoto2
Version  : 2.5.17
Release  : 6
URL      : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.17/gphoto2-2.5.17.tar.gz
Source0  : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.17/gphoto2-2.5.17.tar.gz
Source99 : https://sourceforge.net/projects/gphoto/files/gphoto/2.5.17/gphoto2-2.5.17.tar.gz.asc
Summary  : Command line interface to libgphoto2
Group    : Development/Tools
License  : GPL-2.0
Requires: gphoto2-bin
Requires: gphoto2-doc
Requires: gphoto2-locales
BuildRequires : libgphoto2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : popt-dev
BuildRequires : readline-dev

%description
gphoto2 is a command line client to for the libgphoto2. It allows to
use gPhoto software from a terminal or from a script shell to perform
any camera operation that can be done. This is the main user interface.

%package bin
Summary: bin components for the gphoto2 package.
Group: Binaries

%description bin
bin components for the gphoto2 package.


%package doc
Summary: doc components for the gphoto2 package.
Group: Documentation

%description doc
doc components for the gphoto2 package.


%package locales
Summary: locales components for the gphoto2 package.
Group: Default

%description locales
locales components for the gphoto2 package.


%prep
%setup -q -n gphoto2-2.5.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524062132
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1524062132
rm -rf %{buildroot}
%make_install
%find_lang gphoto2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gphoto2

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gphoto2/*
%doc /usr/share/man/man1/*

%files locales -f gphoto2.lang
%defattr(-,root,root,-)

