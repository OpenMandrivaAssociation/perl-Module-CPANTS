%define module  Module-CPANTS
%define name    perl-%{module}
%define version 0.20030725
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        CPAN module testing
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# currently broken
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Module
%{perl_vendorlib}/auto/Module
%{_mandir}/*/*


