Summary:	Visual interface to programs
Summary(pl.UTF-8):	Tekstowy interfejs dla programów
Name:		otak
Version:	1.3.4
Release:	3
License:	GPL v2
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
Group:		Applications/Mail
Source0:	http://otak.k-k.pl/tgz/%{name}-%{version}.tar.gz
# Source0-md5:	1f11039b70a20db4edf0a5c1e6819f48
Patch0:		%{name}-desktop.patch
URL:		http://otak.k-k.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main idea behind otak, is to provide visual interface to programs,
that doesn't have one, but needs to take arguments, that can be
selected from list. For example one can use it as an adress book
program in connection with mutt, or as a phone-book with sms-sending
software, or even as list of hosts to ssh or FTP to.

%description -l pl.UTF-8
Otak został zaprojektowany jako interfejs graficzny dla programów,
które go nie posiadają, ale wymagają argumentu, który może być wybrany
z listy. Przykładowo: Można powiązać otak z muttem i używać jako
książki adresowej, albo powiązać go z sms-em i używać jako książki
"smsowej", można też np. powiązać otaka z komendą ssh (czy FTP) i
nawiązywać połączenia z gromadzonymi hostami.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.png $RPM_BUILD_ROOT%{_pixmapsdir}
install *.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ABOUT{,-pl} BUGS-pl THANKS TODO-pl NEWS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man*/*.*
%lang(pl) %{_mandir}/pl/man*/*.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
