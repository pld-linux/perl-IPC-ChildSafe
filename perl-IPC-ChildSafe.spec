#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	ChildSafe
Summary:	IPC::ChildSafe perl module
Summary(pl.UTF-8):	Moduł perla IPC::ChildSafe
Name:		perl-IPC-ChildSafe
Version:	3.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68f9ae8be45c7399272a26bbe86d12ba
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ChildSafe - control a child process without blocking.

%description -l pl.UTF-8
IPC::ChildSafe umożliwia kontrolowanie procesu potomnego bez
blokowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IPC/*.pm
%dir %{perl_vendorarch}/auto/IPC/ChildSafe
%{perl_vendorarch}/auto/IPC/ChildSafe/ChildSafe.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IPC/ChildSafe/ChildSafe.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
