%define	module	PAR
%define	name	perl-%{module}
%define	version	0.959
%define	release	%mkrel 1

Summary:	Perl Archive Toolkit
Version:	%{version}
Name:		%{name}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
URL:		http://par.perl.org/
Source0:	%{module}-%{version}.tar.bz2
Patch0:		perl-PAR-fix-interp.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%description
PAR is a toolkit to use perl scripts and modules stored inside compressed
.par files.

For bundling prerequisite modules of scripts into a PAR file (ala
PerlApp, Perl2exe, or 'perlcc that works'), see "perldoc pp".
For running ".par" files directly, see "perldoc parl".
To generate/execute self-contained perl scripts, see "perldoc par.pl".

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%__make

%check
# don't run signature test since this package was patched
rm -f SIGNATURE
yes | (%__make test)

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog contrib/ README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*



