#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	ROC
Summary:	Receiver-operator-characteristic (ROC) curves with nonparametric confidence bounds
Summary(pl):	Krzywe ROC z nieparametrycznymi przedzia�ami ufno�ci
Name:		perl-Statistics-ROC
Version:	0.02
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-GIFgraph
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-FileDialog
BuildRequires:	perl-Tk-WaitBox
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program determines the ROC curve and its nonparametric confidence
bounds for data categorized into two groups.  A ROC curve shows the
relationship of probability of false alarm (x-axis) to probability of
detection (y-axis) for a certain test.  Expressed in medical terms:
the probability of a positive test, given no disease to the
probability of a positive test, given disease.  The ROC curve may be
used to determine an optimal cutoff point for the test.

%description -l pl
Ten program okre�la krzyw� ROC i jej nieparametryczne przedzia�y
ufno�ci dla danych podzielonych na dwie grupy. Krzywa ROC pokazuje
zale�no�� prawdopodobie�stwa fa�szywego alarmu (o� x) od
prawdopodobie�stwa wykrycia (o� y) dla konkretnego testu (w
terminologii medycznej: prawdopodobie�stwo pozytywnego testu przy
braku choroby od prawdopodobie�stwa pozytywnego testu przy chorobie).
Krzywa ROC mo�e by� u�ywana do okre�lenia optymalnego punktu
granicznego dla testu.

%prep
%setup -q -c -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Statistics/ROC.pm
%{perl_vendorlib}/Statistics/roc_ui.pl
%{_mandir}/man3/*
