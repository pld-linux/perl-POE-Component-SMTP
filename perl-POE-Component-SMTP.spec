#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Component-SMTP
Summary:	POE::Filter::SMTP - SMTP protocol filter
Summary(pl.UTF-8):	POE::Filter::SMTP - filtr dla protokołu SMTP
Name:		perl-POE-Component-SMTP
Version:	1.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26c8d3705ef2bb9ac3d6d980ee5da73d
URL:		http://search.cpan.org/dist/POE-Component-SMTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE
BuildRequires:	perl-POE-Session-MultiDispatch
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Filter::SMTP filters input and output and splits command and
arguments, as well as return codes and return strings. It is a
subclass of POE::Filter::Line.

%description -l pl.UTF-8
POE::Filter::SMTP filtruje wejście i wyjście oraz oddziela polecenia i
argumenty, a także zwracane kody i łańcuchy. Jest to podklasa
POE::Filter::Line.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*/*.pm
%{perl_vendorlib}/%{pdir}/*/*/*.pm
%{_mandir}/man3/*
