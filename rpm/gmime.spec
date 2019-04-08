Name:       gmime

%define keepstatic 1

Summary:    Library for creating and parsing MIME messages
Version:    2.6.20
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://spruce.sourceforge.net/gmime/
Source0:    http://download.gnome.org/sources/gmime/2.6/gmime-%{version}.tar.xz
Source1:    gpgme.m4
Patch0:     gmime-2.5.8-gpg-error.patch
Patch1:     disable-gtkdoc.patch
Patch2:     Add-automake-1.16.1-support.patch
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains header files
to develop applications that use libgmime.

%prep
%setup -q -n %{name}-%{version}/%{name}

# gmime-2.5.8-gpg-error.patch
%patch0 -p1
# disable-gtkdoc.patch
%patch1 -p1
# Add-automake-1.16.1-support.patch
%patch2 -p1
%__cp $RPM_SOURCE_DIR/gpgme.m4 m4/

%build
AUTOGEN_SUBDIR_MODE=1 %autogen || true

%configure  \
    --disable-gtk-doc \
    --enable-cryptography=no \
    --program-prefix=%{name}

make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gmime-*.pc
%{_includedir}/gmime-*
#%{_datadir}/gtk-doc/html/gmime-*
