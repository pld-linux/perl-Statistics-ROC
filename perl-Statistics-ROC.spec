#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	ROC
Summary:	Receiver-operator-characteristic (ROC) curves with nonparametric confidence bounds
Name:		perl-Statistics-ROC
Version:	0.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-GIFgraph
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-FileDialog
BuildRequires:	perl-Tk-WaitBox
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program determines the ROC curve and its nonparametric confidence
bounds for data categorized into two groups.  A ROC curve shows the
relationship of B<probability of false alarm> (x-axis) to B<probability of
detection> (y-axis) for a certain test.  Expressed in medical terms: the
B<probability of a positive test, given no disease> to the B<probability
of a positive test, given disease>.  The ROC curve may be used to
determine an I<optimal> cutoff point for the test.

%prep
%setup -q -c -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Statistics/ROC.pm
%{perl_sitelib}/Statistics/roc_ui.pl
%{_mandir}/man3/*
