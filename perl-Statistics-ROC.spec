%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	ROC
Summary:	Statistics::ROC perl module
Summary(pl):	Modu� perla Statistics::ROC
Name:		perl-Statistics-ROC
Version:	0.02
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GIFgraph
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-FileDialog
BuildRequires:	perl-Tk-WaitBox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::ROC perl module.

%description -l pl
Modu� perla Statistics::ROC.

%prep
%setup -q -c -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

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
