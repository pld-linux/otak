Summary:	text-based adress book
Summary(pl):	ksi±¿ka adresowa z interfejsem textowym
Name:		otak
Version:	0.0.4
Release:	1
License:	GPL
Vendor:		Grzegorz Moskal <eldevarth@hoga.pl>
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	conflib-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a text-based address book program. Fields describing a person
are fully configurable, initially they are: nick, First and Surname,
home page and phone fields, but you can add eye colour or whetever if
you like to.

%description -l pl
Jest to ksi±¿ka adresowa z interfejsem tekstowym. Pola opisuj±ce osobê
s± w pe³ni konfigurowalne, pocz±tkowo zawieraj± one: ksyfkê, imiê i
nazwisko, stronê domowa (www) oraz telefon, ale mo¿esz dodaæ kolor
oczu czy cokolwiek, je¶li chcesz.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/*
%{_mandir}/man*/*.*
%lang(pl) %{_mandir}/pl/man*/*.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*
