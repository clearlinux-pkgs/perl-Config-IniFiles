#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-IniFiles
Version  : 3.000003
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Config-IniFiles-3.000003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Config-IniFiles-3.000003.tar.gz
Summary  : 'A module for reading .ini-style configuration files.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Config-IniFiles-license = %{version}-%{release}
Requires: perl-Config-IniFiles-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Scalar)
BuildRequires : perl(Module::Build)

%description
Config::IniFiles - A module for reading .ini-style configuration files.
DESCRIPTION

%package dev
Summary: dev components for the perl-Config-IniFiles package.
Group: Development
Provides: perl-Config-IniFiles-devel = %{version}-%{release}
Requires: perl-Config-IniFiles = %{version}-%{release}

%description dev
dev components for the perl-Config-IniFiles package.


%package license
Summary: license components for the perl-Config-IniFiles package.
Group: Default

%description license
license components for the perl-Config-IniFiles package.


%package perl
Summary: perl components for the perl-Config-IniFiles package.
Group: Default
Requires: perl-Config-IniFiles = %{version}-%{release}

%description perl
perl components for the perl-Config-IniFiles package.


%prep
%setup -q -n Config-IniFiles-3.000003
cd %{_builddir}/Config-IniFiles-3.000003

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-IniFiles
cp %{_builddir}/Config-IniFiles-3.000003/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-IniFiles/38e94f89ec602e1a6495ef7c30477d01aeefedc9
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::IniFiles.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-IniFiles/38e94f89ec602e1a6495ef7c30477d01aeefedc9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
