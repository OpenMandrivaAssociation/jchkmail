%define Werror_cflags %nil

Summary: A mail filtering software
Name:    jchkmail
Version: 2.2.1
Release: 4
Source0: %{name}-%{version}.tgz
License: GPL
Group: System/Servers
Url: http://www.j-chkmail.org/
BuildRequires: libxml2-devel
BuildRequires: libmilter-devel 
BuildRequires: sendmail

%description
j-chkmail is a mail filtering software using sendmail milter API. j-chkmail is
compatible with UNIX based mailservers running sendmail or postfix.

The goal of j-chkmail is to be able to filter as much messages as possible, as
fast as possible and as well as possible. Originally, it's intended to be use
in large and heterogeneous communities such as university campus, but not only. 

%prep
%setup -q
# don't try action needing to be root
perl -pi -e 's:@(chown|chgrp):/bin/true:' \
    Makefile.am etc/Makefile.am \
    Makefile.in etc/Makefile.in

%build
aclocal
automake
autoreconf
%configure \
  --with-work-dir=%_var/lib/%name \
  --with-jgreyd-dir=%_var/lib/%name/jgreyd \
  --with-user=%name \
  --with-group=%name

%make

%install
mkdir -p %buildroot%_sysconfdir/init.d

%makeinstall_std

%files
%config(noreplace) %_sysconfdir/mail/%name
%_bindir/*
%_sbindir/*
%_sysconfdir/init.d/*
%attr(-,jchkmail,jchkmail) %config(noreplace) %_var/lib/%name
%_mandir/*/*
%doc README*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-3mdv2011.0
+ Revision: 612440
- the mass rebuild of 2010.1 packages

* Mon Feb 08 2010 Olivier Thauvin <nanardon@mandriva.org> 2.2.1-2mdv2010.1
+ Revision: 502501
- add docs files
- 2.2.1

* Mon Nov 23 2009 Olivier Thauvin <nanardon@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 469198
- import jchkmail


