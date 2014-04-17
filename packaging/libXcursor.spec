%bcond_with x

Name:           libXcursor
Version:        1.1.14
Release:        1
License:        MIT
Summary:        Cursor management library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXcursor.manifest

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrender)

%if !%{with x}
ExclusiveArch:
%endif

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
cp %{SOURCE1001} .

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/default

%remove_docs


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXcursor.so.1
%{_libdir}/libXcursor.so.1.0.2
%dir %{_datadir}/icons/default

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
