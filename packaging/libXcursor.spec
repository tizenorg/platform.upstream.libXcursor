Name:           libXcursor
Version:        1.1.13
Release:        1
License:        MIT
Summary:        Cursor management library
Url:            http://www.x.org
Group:          System Environment/Libraries
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrender)

%description
This is  a simple library designed to help locate and load cursors.
Cursors can be loaded from files or memory. A library of common cursors
exists which map to the standard X cursor names.Cursors can exist in
several sizes and the library automatically picks the best size.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
libXcursor development package.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/default

%remove_docs


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2
%dir %{_datadir}/icons/default

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
