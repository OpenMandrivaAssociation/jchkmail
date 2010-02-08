%define name jchkmail
%define version 2.2.1
%define release %mkrel 1

%define Werror_cflags %nil

Summary: A mail filtering software
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tgz
License: GPL
Group: System/Servers
Url: http://www.j-chkmail.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
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
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_sysconfdir/init.d

%makeinstall_std

%pre
%_pre_user_add %name %_var/lib/%name /bin/false

%postun
%_postun_user_del %name

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/mail/%name
%_bindir/*
%_sbindir/*
%_sysconfdir/init.d/*
%attr(-,jchkmail,jchkmail) %config(noreplace) %_var/lib/%name
%_mandir/*/*
