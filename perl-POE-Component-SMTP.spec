#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-SMTP
Summary:	POE::Filter::SMTP - SMTP protocol filter
Summary(pl):	POE::Filter::SMTP - filtr dla protoko³u SMTP
Name:		perl-POE-Component-SMTP
Version:	1.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75999b462eb9a3726c521f2547b96b53
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?with_tests}
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

%description -l pl
POE::Filter::SMTP filtruje wej¶cie i wyj¶cie oraz oddziela polecenia
i argumenty, a tak¿e zwracane kody i ³añcuchy. Jest to podklasa
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
