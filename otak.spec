Summary:	text-based addressbook
Summary(pl):	ksi±¿ka adresowa z interfejsem tekstowym
Name:		otak
Version:	1.0.7
Vendor:		Grzegorz Moskal <eldevarth@hoga.pl>
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	conflib-devel
BuildRequires:	ncurses-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/
%define         _mandir         %{_prefix}/man

%description
Otak is a text-based addressbook program. Main feature of this program
is that you can use it as a visual interface for programs which don`t
have one. For instance you can use otak only as a cell-phone book.(and
send sms by it:), or as a host-list (and making ftp ot ssh connection
by it). Default it contain: Name, E-mail, Cell-phone, WWW and Comment
fields. You can add new fields or remove those if you want.

%description -l pl
Otak [teoretycznie] jest ksi±¿k± adresow±, z interfejsem opartym na
tekstowym systemie okienkowym. Jednak g³ówn± cech± tego programu jest
jego du¿a konfigurowalno¶æ. To czyni z niego intefejs graficzny do
jakiejkolwiek komendy, w ktorej by³by przydatny, ale (obecnie) go brak.
Np mo¿esz u¿yæ tego programu jako ksi±¿ki nr. telefonów komórkowych lub
jako listy hostów, na które czêsto robisz ftp. Standardowo dostêpne s±
nastêpuj±ce pola: Imie i Nazwisko, E-mail, Tel. Komorkowy (sms), Tel.
domowy, WWW, i komentarz. Ale zawsze mozesz dodaæ swoje lub usun±æ te.
%prep
%setup -q

%build

gettextize --copy --force
aclocal
autoconf
automake -a -c
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
