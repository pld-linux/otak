Summary:	Visual interface to programs
Summary(pl):	Tekstowy interfejs dla programów
Name:		otak
Version:	1.2.0
Vendor:		Grzegorz Moskal <eldevarth@hoga.pl>
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	conflib-devel
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main idea behind otak, is to provide visual interface to programs,
that doesn't have one, but needs to take arguments, that can be selected
from list.  For example one can use it as an adress book program in 
connection with mutt, or as a phone-book with sms-sending software,
or even as list of hosts to ssh or ftp to.

%description -l pl
Otak zosta³ zaprojektowany jako interfejs graficzny dla programów,
które go nie posiadaj±, ale wymagaj± argumentu, który mo¿e byæ wybrany
z listy. Przyk³adowo : Mo¿na powi±zaæ otak z mutt`em i u¿ywaæ jako
ksi±¿ki adresowej, albo powi±zaæ go z sms`em i u¿ywaæ jako 
ksi±¿ki "smsowej", mo¿na te¿ np. powi±zaæ otaka z komend± ssh (czy ftp)
i nawi±zywaæ po³±czenia z gromadzonymi hostami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install *.png $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail/
install *.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*

%{_applnkdir}/Network/Mail/*
%{_pixmapsdir}/*

%{_mandir}/man*/*.*
%lang(pl) %{_mandir}/pl/man*/*.*

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*
