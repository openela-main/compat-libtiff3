Summary: Compatibility package for libtiff 3
Name: compat-libtiff3
Version: 3.9.4
Release: 13%{?dist}

License: libtiff
Group: System Environment/Libraries
URL: http://www.remotesensing.org/libtiff/

Source: ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz
Patch1: libtiff-acversion.patch
Patch2: libtiff-mantypo.patch
Patch3: libtiff-scanlinesize.patch
Patch4: libtiff-getimage-64bit.patch
Patch5: libtiff-ycbcr-clamp.patch
Patch6: libtiff-3samples.patch
Patch7: libtiff-subsampling.patch
Patch8: libtiff-unknown-fix.patch
Patch9: libtiff-checkbytecount.patch
Patch10: libtiff-tiffdump.patch
Patch11: libtiff-CVE-2011-0192.patch
Patch12: libtiff-CVE-2011-1167.patch
Patch13: libtiff-CVE-2009-5022.patch
Patch14: libtiff-CVE-2012-1173.patch
Patch15: libtiff-CVE-2012-2088.patch
Patch16: libtiff-CVE-2012-2113.patch
Patch17: libtiff-CVE-2012-3401.patch
Patch18: libtiff-CVE-2012-4447.patch
Patch19: libtiff-CVE-2012-4564.patch
Patch20: libtiff-CVE-2012-5581.patch
Patch21: libtiff-tiffinfo-exif.patch
Patch22: libtiff-printdir-width.patch
Patch27: libtiff-CVE-2013-1960.patch
Patch28: libtiff-CVE-2013-1961.patch
Patch29: libtiff-CVE-2013-4231.patch
Patch30: libtiff-CVE-2013-4232.patch
Patch31: libtiff-CVE-2013-4244.patch
Patch32: libtiff-CVE-2013-4243.patch
Patch33: libtiff-CVE-2018-7456.patch
Patch34: libtiff-coverity.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel libjpeg-devel
BuildRequires: libtool automake autoconf

%global LIBVER %(echo %{version} | cut -f 1-2 -d .)

%description
The libtiff3 package provides libtiff 3, an older version of libtiff
library for manipulating TIFF (Tagged Image File Format) 
image format files. This version should be used only if you are unable
to use the current version of libtiff.

%prep
%setup -q -n tiff-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1

# Use build system's libtool.m4, not the one in the package.
rm -f libtool.m4

libtoolize --force  --copy
aclocal -I . -I m4
automake --add-missing --copy
autoconf
autoheader

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH make check

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# remove what we didn't want installed
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/{libtiff,libtiffxx}.so

rm -rf $RPM_BUILD_ROOT%{_datadir}/*
rm -rf $RPM_BUILD_ROOT%{_bindir}/*
rm -rf $RPM_BUILD_ROOT%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*

%changelog
* Wed Jun 12 2019 Nikola Forró <nforro@redhat.com> - 3.9.4-13
- Fix important Covscan defects
  related: #1687584

* Thu Jun 06 2019 Nikola Forró <nforro@redhat.com> - 3.9.4-12
- New package for RHEL 8.1.0
  resolves: #1687584
