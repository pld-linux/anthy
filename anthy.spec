Summary:	A Japanese character input system library (with dictionary)
Summary(pl):	System wprowadzania znaków japoñskich (ze s³ownikiem)
Name:		anthy
Version:	5122
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.jp/anthy/8819/%{name}-%{version}.tar.gz
# Source0-md5:	f855b2e7a3de33c819ee9eefa652b231
URL:		http://anthy.sourceforge.jp/
# URL: http://cannadic.oucrc.org
# Source1: cannadic-0.93.tar.gz
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Japanese character input system library (with dictionary).

%description -l pl
System wprowadzania znaków japoñskich (ze s³ownikiem).

%package devel
Summary:	Header files for anthy libraries
Summary(pl):	Pliki nag³ówkowe bibliotek anthy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anthy libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek anthy.

%package static
Summary:	Static anthy libraries
Summary(pl):	Statyczne biblioteki anthy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static anthy libraries.

%description static -l pl
Statyczne biblioteki anthy.

%prep
%setup -q
#tar zxf %{_sourcedir}/cannadic-0.93.tar.gz
#ln -s ../cannadic-0.93/gcanna.t mkanthydic
#ln -s ../cannadic-0.93/gcannaf.t mkanthydic

%build
cp -f /usr/share/automake/config.* .
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/anthy-conf
%{_datadir}/anthy

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/anthy

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

#%{_datadir}/emacs/site-lisp/*
