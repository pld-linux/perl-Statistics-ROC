%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	ROC
Summary:	Statistics::ROC Perl module
Summary(cs):	Modul Statistics::ROC pro Perl
Summary(da):	Perlmodul Statistics::ROC
Summary(de):	Statistics::ROC Perl Modul
Summary(es):	M�dulo de Perl Statistics::ROC
Summary(fr):	Module Perl Statistics::ROC
Summary(it):	Modulo di Perl Statistics::ROC
Summary(ja):	Statistics::ROC Perl �⥸�塼��
Summary(ko):	Statistics::ROC �� ����
Summary(no):	Perlmodul Statistics::ROC
Summary(pl):	Modu� perla Statistics::ROC
Summary(pt_BR):	M�dulo Perl Statistics::ROC
Summary(pt):	M�dulo de Perl Statistics::ROC
Summary(ru):	������ ��� Perl Statistics::ROC
Summary(sv):	Statistics::ROC Perlmodul
Summary(uk):	������ ��� Perl Statistics::ROC
Summary(zh_CN):	Statistics::ROC Perl ģ��
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

%description -l cs
Modul Statistics::ROC pro Perl.

%description -l da
Perlmodul Statistics::ROC.

%description -l de
Statistics::ROC Perl Modul.

%description -l es
M�dulo de Perl Statistics::ROC.

%description -l fr
Module Perl Statistics::ROC.

%description -l it
Modulo di Perl Statistics::ROC.

%description -l ja
Statistics::ROC Perl �⥸�塼��

%description -l ko
Statistics::ROC �� ����.

%description -l no
Perlmodul Statistics::ROC.

%description -l pl
Modu� perla Statistics::ROC.

%description -l pt
M�dulo de Perl Statistics::ROC.

%description -l pt_BR
M�dulo Perl Statistics::ROC.

%description -l ru
������ ��� Perl Statistics::ROC.

%description -l sv
Statistics::ROC Perlmodul.

%description -l uk
������ ��� Perl Statistics::ROC.

%description -l zh_CN
Statistics::ROC Perl ģ��

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
