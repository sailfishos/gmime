Name:       gmime
Summary:    Library for creating and parsing MIME messages
Version:    3.2.8
Release:    1
License:    LGPLv2
URL:        https://gitlab.gnome.org/GNOME/gmime
Source0:    gmime-%{version}.tar.xz
Patch1:     0001-disabled-gtk-doc.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.12.0
BuildRequires:  pkgconfig(zlib) >= 1.2.1.1
BuildRequires:  libgpg-error-devel
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package devel
Summary:    Header files to develop libgmime applications
Requires:   %{name} = %{version}-%{release}

%description devel
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains header files
to develop applications that use libgmime.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}


%build
./autogen.sh
%configure  \
    --disable-gtk-doc \
    --enable-crypto=no \
    --disable-introspection \
    --program-prefix=%{name}
%make_build

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gmime-*.pc
%{_includedir}/gmime-*
