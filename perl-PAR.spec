%define	module	PAR
%define	name	perl-%{module}
%define	version	0.979
%define	release	%mkrel 1

Summary:	Perl Archive Toolkit
Version:	%{version}
Name:		%{name}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
URL:		http://par.perl.org/
Source0:	http://www.cpan.org/modules/by-module/PAR/%{module}-%{version}.tar.gz
BuildRequires:  perl(AutoLoader) >= 5.63
BuildRequires:	perl(Archive::Zip) >= 1
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::ScanDeps) >= 0.69
BuildRequires:	perl(PAR::Dist) >= 0.21
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Signature
BuildRequires:	perl(Archive::Zip) >= 1
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::ScanDeps) >= 0.45
BuildRequires:	perl(PAR::Dist) >= 0.13
BuildRequires:  perl(Getopt::ArgvFile)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PAR is a toolkit to use perl scripts and modules stored inside compressed
.par files.

For bundling prerequisite modules of scripts into a PAR file (ala
PerlApp, Perl2exe, or 'perlcc that works'), see "perldoc pp".
For running ".par" files directly, see "perldoc parl".
To generate/execute self-contained perl scripts, see "perldoc par.pl".

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%__make

%check
# don't run signature test since this package was patched
rm -f SIGNATURE
%__make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{perl_vendorlib}/PAR
%{perl_vendorlib}/PAR.pm
%{_mandir}/*/*



