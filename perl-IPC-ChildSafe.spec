%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	ChildSafe
Summary:	IPC::ChildSafe perl module
Summary(pl):	Modu³ perla IPC::ChildSafe
Name:		perl-IPC-ChildSafe
Version:	3.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ChildSafe - control a child process without blocking.

%description -l pl
IPC::ChildSafe umo¿liwia kontrolowanie procesu potomnego bez
blokowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/IPC/*.pm
%dir %{perl_sitearch}/auto/IPC/ChildSafe
%{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
