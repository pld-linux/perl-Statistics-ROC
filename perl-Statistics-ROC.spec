#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Statistics
%define		pnam	ROC
Summary:	Statistics::ROC - receiver-operator-characteristic (ROC) curves with nonparametric confidence bounds
Summary(pl.UTF-8):	Statistics::ROC - krzywe ROC z nieparametrycznymi przedziałami ufności
Name:		perl-Statistics-ROC
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92f9036e1dec5c41a9ccd008e484b1fc
URL:		http://search.cpan.org/dist/Statistics-ROC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GIFgraph
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-FileDialog
BuildRequires:	perl-Tk-WaitBox
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program determines the ROC curve and its nonparametric confidence
bounds for data categorized into two groups. A ROC curve shows the
relationship of probability of false alarm (x-axis) to probability of
detection (y-axis) for a certain test. Expressed in medical terms: the
probability of a positive test, given no disease to the probability of
a positive test, given disease. The ROC curve may be used to determine
an optimal cutoff point for the test.

%description -l pl.UTF-8
Ten program określa krzywą ROC i jej nieparametryczne przedziały
ufności dla danych podzielonych na dwie grupy. Krzywa ROC pokazuje
zależność prawdopodobieństwa fałszywego alarmu (oś x) od
prawdopodobieństwa wykrycia (oś y) dla konkretnego testu (w
terminologii medycznej: prawdopodobieństwo pozytywnego testu przy
braku choroby od prawdopodobieństwa pozytywnego testu przy chorobie).
Krzywa ROC może być używana do określenia optymalnego punktu
granicznego dla testu.

%prep
%setup -q -n %{pdir}-%{pnam}-0.01

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
%doc Changes README
%{perl_vendorlib}/Statistics/ROC.pm
%{perl_vendorlib}/Statistics/roc_ui.pl
%{_mandir}/man3/*
