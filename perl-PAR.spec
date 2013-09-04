%define	upstream_name	 PAR
%define upstream_version 1.007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl Archive Toolkit
License:	Artistic
Group:		Development/Perl
URL:		http://par.perl.org/
Source0:	http://www.cpan.org/modules/by-module/PAR/PAR-%{upstream_version}.tar.gz

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

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PAR is a toolkit to use perl scripts and modules stored inside compressed
.par files.

For bundling prerequisite modules of scripts into a PAR file (ala
PerlApp, Perl2exe, or 'perlcc that works'), see "perldoc pp".
For running ".par" files directly, see "perldoc parl".
To generate/execute self-contained perl scripts, see "perldoc par.pl".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
# don't run signature test since this package was patched
rm -f SIGNATURE
%make test

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


%changelog
* Wed Jan 18 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1mdv2012.0
+ Revision: 762144
- 1.005 (fixes CVE-2011-4114, CVE-2011-5060)

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 561933
- update to 1.002

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 536209
- update to 1.000

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.994.0-1mdv2010.0
+ Revision: 399265
- update to 0.994
- using %%perl_convert_version

* Thu May 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.992-2mdv2010.0
+ Revision: 372849
- force rebuild, now that io-compress madness is gone
- update to new version 0.992

* Wed Mar 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.991-1mdv2009.1
+ Revision: 353872
- update to new version 0.991

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.983-1mdv2009.1
+ Revision: 292339
- update to new version 0.983

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.982-1mdv2009.0
+ Revision: 272286
- update to new version 0.982

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.980-2mdv2009.0
+ Revision: 268651
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.980-1mdv2009.0
+ Revision: 210828
- update to new version 0.980

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.979-1mdv2009.0
+ Revision: 208359
- update to new version 0.979

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.977-1mdv2008.1
+ Revision: 153993
- update to new version 0.977

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.976-1mdv2008.1
+ Revision: 110873
- new version
- new version


* Sun Mar 04 2007 Olivier Thauvin <nanardon@mandriva.org> 0.959-1mdv2007.0
+ Revision: 132087
- 0.959

* Thu Mar 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.942-3mdv2007.1
+ Revision: 130523
- fix #24641

  + Nicolas Lécureuil <neoclust@mandriva.org>
    -  Add BuildRequires

* Tue Aug 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.942-1mdv2007.0
+ Revision: 53978
- 0.942; remove obsolete URLs
- Import perl-PAR

* Sat Jun 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.94-1mdv2007.0
- 0.94

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.92-1mdk
- 0.92

* Wed Feb 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.91-1mdk
- 0.91

* Sun Nov 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.90-1mdk
- 0.90

* Tue Jun 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.89-1mdk
- 0.89
- Patch 0 : fix interpreter paths

* Wed Jun 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.88-1mdk
- 0.88
- Drop patches, committed upstream

* Fri May 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.87-2mdk
- Rebuild for new perl
- New URL
- Patch 0 : don't skip tests
- Patch 1 : compile with gcc 4

* Mon Jan 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.87-1mdk
- 0.87

* Mon Dec 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.86-1mdk
- New version

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.85-3mdk
- Rebuild for new perl

* Thu Jul 08 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.85-2mdk
- Rebuild for new perl

* Sat Jul 03 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.85-1mdk
- 0.85 ; fix Requires

* Sat Jun 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.83-1mdk
- 0.83

* Tue May 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.81-1mdk
- New version

* Sat May 22 2004 Florin <florin@mandrakesoft.com> 0.80-1mdk
- first Mandrake release


