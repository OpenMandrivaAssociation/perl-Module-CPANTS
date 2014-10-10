%define module  Module-CPANTS

Name:		perl-%{module}
Version:	0.20030725
Release:	7
Summary:	CPAN module testing
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
Kwalitee is an automatically-measurable gauge of how good your software is.
That's very different from quality, which a computer really can't measure in a
general sense. (If you can, you've solved a hard problem in computer science.)

In the world of the CPAN, the CPANTS project (CPAN Testing Service; also a
funny acronym on its own) measures Kwalitee with several metrics. If you plan
to release a distribution to the CPAN -- or even within your own organization
-- testing its Kwalitee before creating a release can help you improve your
quality as well.

Test::Kwalitee and a short test file will do this for you automatically.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# currently broken
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Module
%{perl_vendorlib}/auto/Module
%{_mandir}/*/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.20030725-5mdv2010.0
+ Revision: 430506
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.20030725-4mdv2009.0
+ Revision: 257853
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.20030725-3mdv2009.0
+ Revision: 245886
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.20030725-1mdv2008.1
+ Revision: 123036
- kill re-definition of %%buildroot on Pixel's request


* Sat Nov 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20030725-1mdv2007.0
+ Revision: 87239
- Import perl-Module-CPANTS

* Sat Nov 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20030725-1mdv2007.1
- first mdv release

