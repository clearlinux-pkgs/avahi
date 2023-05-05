#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : avahi
Version  : 0.8
Release  : 14
URL      : http://avahi.org/download/avahi-0.8.tar.gz
Source0  : http://avahi.org/download/avahi-0.8.tar.gz
Source1  : avahi.tmpfiles
Summary  : Avahi Multicast DNS Responder (GLib GObject Support)
Group    : Development/Tools
License  : LGPL-2.1
Requires: avahi-bin = %{version}-%{release}
Requires: avahi-config = %{version}-%{release}
Requires: avahi-data = %{version}-%{release}
Requires: avahi-lib = %{version}-%{release}
Requires: avahi-license = %{version}-%{release}
Requires: avahi-locales = %{version}-%{release}
Requires: avahi-man = %{version}-%{release}
Requires: avahi-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : gdbm-dev
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : libcap-dev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libdaemon)
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Allow-fallback-to-a-system-wide-default-avahi-daemon.patch
Patch2: 0002-fix-requires-in-pc-file.patch

%description
AVAHI SERVICE DISCOVERY SUITE
Avahi is a free, LGPL implementation of DNS Service Discovery (DNS-SD RFC 6763) over Multicast DNS (mDNS RFC 6762),
commonly known as and compatible with Apple Bonjour primarily targetting Linux.

%package bin
Summary: bin components for the avahi package.
Group: Binaries
Requires: avahi-data = %{version}-%{release}
Requires: avahi-config = %{version}-%{release}
Requires: avahi-license = %{version}-%{release}
Requires: avahi-services = %{version}-%{release}

%description bin
bin components for the avahi package.


%package config
Summary: config components for the avahi package.
Group: Default

%description config
config components for the avahi package.


%package data
Summary: data components for the avahi package.
Group: Data

%description data
data components for the avahi package.


%package dev
Summary: dev components for the avahi package.
Group: Development
Requires: avahi-lib = %{version}-%{release}
Requires: avahi-bin = %{version}-%{release}
Requires: avahi-data = %{version}-%{release}
Provides: avahi-devel = %{version}-%{release}
Requires: avahi = %{version}-%{release}

%description dev
dev components for the avahi package.


%package extras
Summary: extras components for the avahi package.
Group: Default

%description extras
extras components for the avahi package.


%package lib
Summary: lib components for the avahi package.
Group: Libraries
Requires: avahi-data = %{version}-%{release}
Requires: avahi-license = %{version}-%{release}

%description lib
lib components for the avahi package.


%package license
Summary: license components for the avahi package.
Group: Default

%description license
license components for the avahi package.


%package locales
Summary: locales components for the avahi package.
Group: Default

%description locales
locales components for the avahi package.


%package man
Summary: man components for the avahi package.
Group: Default

%description man
man components for the avahi package.


%package services
Summary: services components for the avahi package.
Group: Systemd services
Requires: systemd

%description services
services components for the avahi package.


%prep
%setup -q -n avahi-0.8
cd %{_builddir}/avahi-0.8
%patch1 -p1
%patch2 -p1
pushd ..
cp -a avahi-0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683313452
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-distro=none \
--disable-qt3 \
--disable-qt4 \
--disable-gtk \
--disable-gtk3 \
--disable-mono \
--disable-python \
--disable-pygobject \
--disable-python-dbus \
--sysconfdir=/usr/share/defaults/etc \
--enable-compat-libdns_sd
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-distro=none \
--disable-qt3 \
--disable-qt4 \
--disable-gtk \
--disable-gtk3 \
--disable-mono \
--disable-python \
--disable-pygobject \
--disable-python-dbus \
--sysconfdir=/usr/share/defaults/etc \
--enable-compat-libdns_sd
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1683313452
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/avahi
cp %{_builddir}/avahi-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/avahi/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang avahi
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/avahi.conf
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/avahi
install avahi-daemon.conf %{buildroot}/usr/share/defaults/etc/avahi/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/avahi-autoipd
/V3/usr/bin/avahi-browse
/V3/usr/bin/avahi-browse-domains
/V3/usr/bin/avahi-dnsconfd
/V3/usr/bin/avahi-publish
/V3/usr/bin/avahi-publish-address
/V3/usr/bin/avahi-publish-service
/V3/usr/bin/avahi-resolve
/V3/usr/bin/avahi-resolve-address
/V3/usr/bin/avahi-resolve-host-name
/V3/usr/bin/avahi-set-host-name
/usr/bin/avahi-autoipd
/usr/bin/avahi-browse
/usr/bin/avahi-browse-domains
/usr/bin/avahi-dnsconfd
/usr/bin/avahi-publish
/usr/bin/avahi-publish-address
/usr/bin/avahi-publish-service
/usr/bin/avahi-resolve
/usr/bin/avahi-resolve-address
/usr/bin/avahi-resolve-host-name
/usr/bin/avahi-set-host-name

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/avahi.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Avahi-0.6.typelib
/usr/lib64/girepository-1.0/AvahiCore-0.6.typelib
/usr/share/avahi/avahi-service.dtd
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.AddressResolver.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.DomainBrowser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.EntryGroup.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.HostNameResolver.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.RecordBrowser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.Server.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceBrowser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceResolver.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceTypeBrowser.xml
/usr/share/defaults/etc/avahi/avahi-autoipd.action
/usr/share/defaults/etc/avahi/avahi-dnsconfd.action
/usr/share/defaults/etc/avahi/hosts
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libavahi-client.so
/V3/usr/lib64/libavahi-common.so
/V3/usr/lib64/libavahi-core.so
/V3/usr/lib64/libavahi-glib.so
/V3/usr/lib64/libavahi-gobject.so
/V3/usr/lib64/libavahi-libevent.so
/V3/usr/lib64/libavahi-qt5.so
/V3/usr/lib64/libdns_sd.so
/usr/include/avahi-client/client.h
/usr/include/avahi-client/lookup.h
/usr/include/avahi-client/publish.h
/usr/include/avahi-common/address.h
/usr/include/avahi-common/alternative.h
/usr/include/avahi-common/cdecl.h
/usr/include/avahi-common/defs.h
/usr/include/avahi-common/domain.h
/usr/include/avahi-common/error.h
/usr/include/avahi-common/gccmacro.h
/usr/include/avahi-common/llist.h
/usr/include/avahi-common/malloc.h
/usr/include/avahi-common/rlist.h
/usr/include/avahi-common/simple-watch.h
/usr/include/avahi-common/strlst.h
/usr/include/avahi-common/thread-watch.h
/usr/include/avahi-common/timeval.h
/usr/include/avahi-common/watch.h
/usr/include/avahi-compat-libdns_sd/dns_sd.h
/usr/include/avahi-core/core.h
/usr/include/avahi-core/log.h
/usr/include/avahi-core/lookup.h
/usr/include/avahi-core/publish.h
/usr/include/avahi-core/rr.h
/usr/include/avahi-glib/glib-malloc.h
/usr/include/avahi-glib/glib-watch.h
/usr/include/avahi-gobject/ga-client.h
/usr/include/avahi-gobject/ga-entry-group.h
/usr/include/avahi-gobject/ga-enums.h
/usr/include/avahi-gobject/ga-error.h
/usr/include/avahi-gobject/ga-record-browser.h
/usr/include/avahi-gobject/ga-service-browser.h
/usr/include/avahi-gobject/ga-service-resolver.h
/usr/include/avahi-libevent/libevent-watch.h
/usr/include/avahi-qt5/qt-watch.h
/usr/lib64/libavahi-client.so
/usr/lib64/libavahi-common.so
/usr/lib64/libavahi-core.so
/usr/lib64/libavahi-glib.so
/usr/lib64/libavahi-gobject.so
/usr/lib64/libavahi-libevent.so
/usr/lib64/libavahi-qt5.so
/usr/lib64/libdns_sd.so
/usr/lib64/pkgconfig/avahi-client.pc
/usr/lib64/pkgconfig/avahi-compat-libdns_sd.pc
/usr/lib64/pkgconfig/avahi-core.pc
/usr/lib64/pkgconfig/avahi-glib.pc
/usr/lib64/pkgconfig/avahi-gobject.pc
/usr/lib64/pkgconfig/avahi-libevent.pc
/usr/lib64/pkgconfig/avahi-qt5.pc

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/avahi-daemon
/V3/usr/lib64/libavahi-qt5.so.1
/V3/usr/lib64/libavahi-qt5.so.1.0.2
/usr/bin/avahi-daemon
/usr/lib/systemd/system/avahi-daemon.service
/usr/lib/systemd/system/avahi-daemon.socket
/usr/lib64/libavahi-qt5.so.1
/usr/lib64/libavahi-qt5.so.1.0.2
/usr/share/dbus-1/system-services/org.freedesktop.Avahi.service
/usr/share/defaults/etc/avahi/avahi-daemon.conf
/usr/share/defaults/etc/avahi/services/sftp-ssh.service
/usr/share/defaults/etc/avahi/services/ssh.service
/usr/share/defaults/etc/dbus-1/system.d/avahi-dbus.conf
/usr/share/man/man5/avahi-daemon.conf.5
/usr/share/man/man8/avahi-daemon.8

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libavahi-client.so.3
/V3/usr/lib64/libavahi-client.so.3.2.9
/V3/usr/lib64/libavahi-common.so.3
/V3/usr/lib64/libavahi-common.so.3.5.4
/V3/usr/lib64/libavahi-core.so.7
/V3/usr/lib64/libavahi-core.so.7.1.0
/V3/usr/lib64/libavahi-glib.so.1
/V3/usr/lib64/libavahi-glib.so.1.0.2
/V3/usr/lib64/libavahi-gobject.so.0
/V3/usr/lib64/libavahi-gobject.so.0.0.5
/V3/usr/lib64/libavahi-libevent.so.1
/V3/usr/lib64/libavahi-libevent.so.1.0.0
/V3/usr/lib64/libdns_sd.so.1
/V3/usr/lib64/libdns_sd.so.1.0.0
/usr/lib64/libavahi-client.so.3
/usr/lib64/libavahi-client.so.3.2.9
/usr/lib64/libavahi-common.so.3
/usr/lib64/libavahi-common.so.3.5.4
/usr/lib64/libavahi-core.so.7
/usr/lib64/libavahi-core.so.7.1.0
/usr/lib64/libavahi-glib.so.1
/usr/lib64/libavahi-glib.so.1.0.2
/usr/lib64/libavahi-gobject.so.0
/usr/lib64/libavahi-gobject.so.0.0.5
/usr/lib64/libavahi-libevent.so.1
/usr/lib64/libavahi-libevent.so.1.0.0
/usr/lib64/libdns_sd.so.1
/usr/lib64/libdns_sd.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/avahi/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/avahi-browse-domains.1
/usr/share/man/man1/avahi-browse.1
/usr/share/man/man1/avahi-publish-address.1
/usr/share/man/man1/avahi-publish-service.1
/usr/share/man/man1/avahi-publish.1
/usr/share/man/man1/avahi-resolve-address.1
/usr/share/man/man1/avahi-resolve-host-name.1
/usr/share/man/man1/avahi-resolve.1
/usr/share/man/man1/avahi-set-host-name.1
/usr/share/man/man5/avahi.hosts.5
/usr/share/man/man5/avahi.service.5
/usr/share/man/man8/avahi-autoipd.8
/usr/share/man/man8/avahi-autoipd.action.8
/usr/share/man/man8/avahi-dnsconfd.8
/usr/share/man/man8/avahi-dnsconfd.action.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/avahi-dnsconfd.service

%files locales -f avahi.lang
%defattr(-,root,root,-)

