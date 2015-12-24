#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	ChildSafe
Summary:	IPC::ChildSafe - control a child process without blocking
Summary(pl.UTF-8):	IPC::ChildSafe - sterowanie procesem potomnym bez blokowania
Name:		perl-IPC-ChildSafe
Version:	3.16
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68f9ae8be45c7399272a26bbe86d12ba
URL:		http://search.cpan.org/dist/IPC-ChildSafe/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ChildSafe Perl module allows to control a child process without
blocking. It addresses the "blocking problem" inherent in most
coprocessing designs such as IPC::Open3.

%description -l pl.UTF-8
Moduł Perla IPC::ChildSafe umożliwia sterowanie procesem potomnym bez
blokowania. Rozwiązuje "problem blokowania" dziedziczony przez
większość rozwiązań wieloprocesowych, takich jak IPC::Open3.

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
%attr(755,root,root) %{perl_vendorarch}/auto/IPC/ChildSafe/ChildSafe.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
