Summary:	A Japanese character input system library (with dictionary)
Summary(pl.UTF-8):	System wprowadzania znaków japońskich (ze słownikiem)
Name:		anthy
Version:	9100h
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.jp/anthy/37536/%{name}-%{version}.tar.gz
# Source0-md5:	1f558ff7ed296787b55bb1c6cf131108
URL:		http://anthy.sourceforge.jp/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Japanese character input system library (with dictionary).

%description -l pl.UTF-8
System wprowadzania znaków japońskich (ze słownikiem).

%package devel
Summary:	Header files for anthy libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek anthy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anthy libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek anthy.

%package static
Summary:	Static anthy libraries
Summary(pl.UTF-8):	Statyczne biblioteki anthy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static anthy libraries.

%description static -l pl.UTF-8
Statyczne biblioteki anthy.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DIARY NEWS README doc/[!M]* doc/MISC
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/anthy-conf
%{_datadir}/anthy

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/anthy
%{_pkgconfigdir}/anthy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
