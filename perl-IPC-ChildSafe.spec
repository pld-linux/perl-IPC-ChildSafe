%include	/usr/lib/rpm/macros.perl
Summary:	IPC-ChildSafe perl module
Summary(pl):	Modu³ perla IPC-ChildSafe
Name:		perl-IPC-ChildSafe
Version:	3.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/IPC-ChildSafe-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-IPC-ChildSafe
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC-ChildSafe - control a child process without blocking.

%description -l pl
IPC-ChildSafe umo¿liwia kontrolowanie procesu potomnego bez
blokowania.

%prep
%setup -q -n IPC-ChildSafe-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitearch}/IPC/*.pm

%dir %{perl_sitearch}/auto/IPC/ChildSafe
%{perl_sitearch}/auto/IPC/ChildSafe/.packlist
%{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.so

%{_mandir}/man3/*

%{_examplesdir}/%{name}
