%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-ROC perl module
Summary(pl):	Modu³ perla Statistics-ROC
Name:		perl-Statistics-ROC
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-ROC-%{version}.tar.gz
Patch:		perl-Statistics-ROC-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Statistics-ROC perl module. 

%description -l pl
Modu³ perla Statistics-ROC.

%prep
%setup -q -n Statistics-ROC-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/ROC
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Statistics/ROC.pm
%{perl_sitelib}/Statistics/roc_ui.pl
%{perl_sitearch}/auto/Statistics/ROC

%{_mandir}/man3/*
