Summary: e-smith tools for building RPMs
%define name e-smith-devtools
Name: %{name}
%define version 1.13.1
%define release 07
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-devtools-1.13.1-03.mitel_patch
Patch1: e-smith-devtools-1.13.1-04.mitel_patch
Patch2: e-smith-devtools-1.13.1-05.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: perl, perl(Test::Inline) >= 0.12, perl(XML::Parser)
AutoReqProv: no

%changelog
* Tue Jan 24 2006 Charlie Brady <charlieb@e-smith.com> 1.13.1-07
- Remove /root/.vimrc [SME: 562]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.1-06
- Bump release number only

* Mon Jun 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-05]
- Fix file permissions (properly) inside /etc/cron.d. [SF: 1226700]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-04]
- Fix file permissions inside /etc/cron.d. [SF: 1226700]

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-03]
- Add safe_touch() and templates2events() functions to support use
  of the generic_template_expand action. [MN00064130]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-02]
- Updated requires with new perl dependencies. [msoulier MN00040240]

* Thu Feb  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.1-01]
- Rolling as-source. [msoulier]

* Thu Feb  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-03]
- Added esmith::Build::CreateLinks to this package. [msoulier 10992]

* Mon Dec 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-02]
- Updating .vimrc settings. [msoulier 5740]

* Mon Dec 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-01]
- rolling to dev - 1.13.0

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-02]
- Updated file list to handle /etc/rc.d/init.d/supervise and it's files.
  [msoulier 10648]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Changing version to stable stream number - 1.12.0

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-12]
- Enhance genfilelist to take command line options to extend its internal
  databases. Add /usr/lib/perl5/site_perl (and its components) to list
  of ignored directories. Reformat ignoredirs list to make it easier to extend.
  Strip trailing spaces from spec for dirs and files, and add it to the output
  print statements (so that we don't need a trailing space for every extra spec.
  [charlieb 7719]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-11]
- Add missing cd .. after processing a .po directory [gordonr 8828]

* Thu Apr 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-10]
- Updated the files list to pick up the .vimrc file. [msoulier 8044]

* Thu Apr 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Added a standard .vimrc file for the root user. [msoulier 8044]

* Wed Apr  2 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-08]
- Added support for /sbin/e-smith/console-screens. [msoulier 7968]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-07]
- Added support for /home/e-smith/files/samba/netlogon [gordonr 5241]

* Tue Mar 25 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-06]
- small fix to update-po usage() function [tonyc 7794]

* Tue Mar 25 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-05]
- Add update-po to install/files sections [tonyc 7794]

* Tue Mar 25 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-04]
- Add update-po script [tonyc 7794]

* Thu Mar  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-03]
- And add generate-lexicons to %install and %files [gordonr 7578]

* Thu Mar  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-02]
- Added initial generate-lexicons [gordonr 7578]

* Wed Nov  6 2002 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- need new dev version to 1.11.0

* Wed Nov  6 2002 Michael Soulier <msoulier@e-smith.com>
- [1.10.1-02]
- Added /usr/lib/perl5/site_perl/esmith/FormMagick/Panel/ to the fileperms
  hash to set the panel libs to 0644 permissions. [msoulier 5516]

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.1-01]
- Roll new version to fix tagging problem

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Roll to maintained version number to 1.10.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Roll to maintained version number to 1.10.0

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to maintained stream number to 1.9.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to maintained stream number to 1.8.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.6-01]
- RPM rebuild forced by cvsroot2rpm

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.5-01]
- Sigh. Hash-bang line brokenness. [gordonr 3155]

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.4-01]
- Forced attributes on scripts so we don't rely on the repository 
  [gordonr 3155]

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.3-01]
- Actually copy validate-lexicon to the correct place [gordonr 3155]

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.2-01]
- Added validate-lexicon which exits non-zero if the lexicon
  doesn't parse properly [gordonr 3155]

* Sat Apr 05 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-01]
- New development stream. Added /sbin/e-smith/quicktest [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.10-01]
- /var/run/named -> /home/dns/var/run/named for chroot() [gordonr #3019]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.9-01]
- Added /var/run/named [gordonr #3019]

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [1.6.8-01]
- Botched the spec file. :(

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [1.6.7-01]
- Adding smoketest's permissions from e-smith-test.

* Fri Feb 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.6-01]
- Fix permissions on /var/spool/fax/faxrunqd directory (sticky, not setgid).

* Fri Feb 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.5-01]
- Add specifications for directories and run scripts for mgetty's faxrunqd.

* Thu Feb 21 2002 Kirrily Robert <skud@e-smith.com>
- [1.6.4-01]
- Added buildtests to filelist so it actually installs.  Bah.

* Thu Feb 21 2002 Kirrily Robert <skud@e-smith.com>
- [1.6.3-01]
- Added buildtests script for building a package's test suite

* Mon Feb 18 2002 Kirrily Robert <skud@e-smith.com>
- [1.6.2-01]
- Imported to CVS; testing that it worked.

* Mon Feb 18 2002 Kirrily Robert <skud@e-smith.com>
- [1.6.1-01]
- rollRPM: Rolled version number to 1.6.1-01. Includes patches up to 1.6.0-02.

* Wed Jan 02 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-02]
- Add execute permissions to files under /etc/cron.daily and /etc/cron.weekly.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-07.

* Thu Dec 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-07]
- Add missing trailing / to /etc/diald/scripts, to make scripts there
  executable.

* Tue Dec 04 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-06]
- Add specs for /var/lock/fetchmail and /etc/diald/scripts/*.
- Add execute permission for /etc/cron.d/* fragments
- Add spec for /home/e-smith/files/netlogon/netlogon.bat, for when we
  need it.

* Fri Nov 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-05]
- Made /home/e-smith/files/samba/profiles 02750,admin,shared to allow
  users to search that directory when accessing their profile subdirectory

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-04]
- Make /etc/e-smith/events/actions/create-machine-account 06554,root,root
  to allow "admin" to create machine accounts through Samba

* Mon Nov 19 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-03]
- Explicitly list printer driver and profiles directories
- Returned /home/e-smith/files/samba to default ownership by root

* Mon Nov 19 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-02]
- Made /home/e-smith/files/samba 02755,admin,admin to allow admin write
  access to the printer drivers share

* Mon Nov 19 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-02.

* Mon Sep  3 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Include /var/named, plus lots of other directories which are from the
  filesystem RPM.

* Thu Aug 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-02.

* Thu Aug 16 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Configure a list of directories to omit from RPMs - e.g., RedHat supplied
  directories.A
- Fix permissions/ownership of ~admin and ~admin/home
- Add space between %attr() and directory name

* Thu Aug 16 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-05.

* Fri Jul 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-05]
- Fix up misplaced defattr, so that files are root owned, unless stated
  otherwise (rather than by the developer building the package). 

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-04]
- Changed license to GPL

* Sat May 05 2001 Paul Nesbit <pkn@e-smith.com>
- [1.2.0-03]
- Corrected permission in genfilelist.

* Mon Jan 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Mark netlogon.bat as a noreplace config file.
- Add some horde config files rules, and rule for /root/.ssh
  directory
- Add e-smith Maildir rules
- Give admin ownership of admin home directory

* Fri Jan 26 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-3.

* Sat Jan 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-3]
- Remove "other" execute permission for console and action scripts
- Add execute permission rule for /sbin/e-smith/dynamic-dns/*.
- Add permission rules for /etc/cron.d/* and /etc/profile.d/* files

* Mon Dec 18 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-2]
- Include ownership and permission for netlogon share

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-1]
- Rolled version and tarball including patches to 0.1-11

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- Added settings for /home/dns/var/run and /home/dns/var/named

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- Added default permissions setting for directories

* Tue Sep 12 2000 Adrian Chung <mac@e-smith.com>
- Changed /sbin/e-smith/web to /etc/e-smith/web.

* Mon Sep 11 2000 Adrian Chung <mac@e-smith.com>
- Changed permissions on functions dir to 4750. 

* Thu Aug 31 2000 Adrian Chung <mac@e-smith.com>
- Added executable permissions to index.cgi.

* Thu Aug 31 2000 Adrian Chung <mac@e-smith.com>
- Modified all panel directories to root,admin. 

* Wed Aug 30 2000 Adrian Chung <mac@e-smith.com>
- Modified web directories to (root,admin) permissions.

* Wed Aug 30 2000 Adrian Chung <mac@e-smith.com>
- Moved %defattr below to under files section.
- Changed genfilelist for new web permissions.
- Changed genfilelist for new permissions on some other
  files.

* Tue Aug 29 2000 Charlie Brady <charlieb@e-smith.net>
- Fix another stupid ordering problem - can't get ordered searching of 
  hash. We only need to key by file and containing directory anyway.

* Fri Aug 25 2000 Charlie Brady <charlieb@e-smith.net>
- Fix ordering problem with using hash before defined.

* Thu Aug 24 2000 Charlie Brady <charlieb@e-smith.net>
- initial release

%description
Tools for use in building RPMs for the e-smith serverand gateway.

Use "genfilelist" to create a filelist file with correct ownerships and
permissions.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin/e-smith
mkdir -p $RPM_BUILD_ROOT/root
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/esmith/Build
cp genfilelist $RPM_BUILD_ROOT/sbin/e-smith
cp buildtests  $RPM_BUILD_ROOT/sbin/e-smith
cp validate-lexicon  $RPM_BUILD_ROOT/sbin/e-smith
cp generate-lexicons $RPM_BUILD_ROOT/sbin/e-smith
cp update-po $RPM_BUILD_ROOT/sbin/e-smith
cp CreateLinks.pm $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/esmith/Build

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files
%defattr(-,root,root)
%attr(0755,root,root) /sbin/e-smith/genfilelist
%attr(0755,root,root) /sbin/e-smith/buildtests
%attr(0755,root,root) /sbin/e-smith/validate-lexicon
%attr(0755,root,root) /sbin/e-smith/generate-lexicons
%attr(0755,root,root) /sbin/e-smith/update-po
%attr(-,root,root) %dir /sbin
%attr(-,root,root) %dir /sbin/e-smith
%attr(0644,root,root) /usr/lib/perl5/site_perl/esmith/Build/CreateLinks.pm
%doc COPYING
