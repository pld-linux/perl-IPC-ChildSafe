Summary:	IPC-ChildSafe perl module
Summary(pl):	Modu³ perla IPC-ChildSafe
Name:		perl-IPC-ChildSafe
Version:	2.29
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/IPC-ChildSafe-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
IPC-ChildSafe - control a child process without blocking.

%description -l pl
IPC-ChildSafe umo¿liwia kontrolowanie procesu potomnego bez blokowania.

%prep
%setup -q -n IPC-ChildSafe-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/IPC/ChildSafe/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IPC/ChildSafe
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitearch}/IPC/*.pm

%dir %{perl_sitearch}/auto/IPC/ChildSafe
%{perl_sitearch}/auto/IPC/ChildSafe/.packlist
%{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ChildSafe/ChildSafe.so

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
