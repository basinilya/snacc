Name:           snacc
Version:        1.3.1_16_g23ba7a6
Release:        2%{?dist}
Summary:        Sample Neufeld ASN.1 to C Compiler

Group:          Applications/System
License:        GPLv2+
URL:            http://packages.debian.org/source/sid/snacc
Source0:        %{name}-%{version}.tar.gz
#Patch0:         snacc-bts-442873.patch

BUILDROOT:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf automake libtool flex bison

# In RHEL6.5 it's part of flex package. In later releases it's part of flex-devel
BuildRequires:  %{_libdir}/libfl.a

%description
Snacc is Sample Neufeld ASN.1 to C compiler that can produce C, C++ routines
or type tables for BER encoding, decoding, printing and freeing.

%package devel
Summary:        Header files for snacc development
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release} 

%description devel
The %{name}-devel package contains the header files
for snacc development.

%prep
if true; then
%setup
else
:
#%setup -D -T -n snacc-git
#git pull --rebase
fi

# ---- Build ----


%build
#autoreconf -fi
# configure without tcl
%configure CFLAGS="$CFLAGS -O0" TCLSH=false
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} INSTALL="%{_bindir}/install -p" install DESTDIR=%{buildroot}
%{__rm} -f `find %{buildroot} -name *.a`
%{__rm} -f `find %{buildroot} -name *.la`

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING doc/snacc-a5.ps
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/asn1
%{_bindir}/%{name}
%{_bindir}/berdecode
%{_bindir}/mkchdr
%{_bindir}/ptbl
%{_bindir}/pval
%{_mandir}/man1/mkchdr.1.gz
%{_mandir}/man1/ptbl.1.gz
%{_mandir}/man1/pval.1.gz
%{_mandir}/man1/snacc.1.gz
%{_mandir}/man1/snacced.1.gz
%{_mandir}/mann/snacc.n.gz
%{_libdir}/libasn1c++.so.0.0.0
%{_libdir}/libasn1cCebuf.so.0.0.0
%{_libdir}/libasn1cebuf.so.0.0.0
%{_libdir}/libasn1cmbuf.so.0.0.0
%{_libdir}/libasn1csbuf.so.0.0.0
%{_libdir}/libasn1ctbl.so.0.0.0
%{_libdir}/libasn1c++.so.0
%{_libdir}/libasn1cCebuf.so.0
%{_libdir}/libasn1cebuf.so.0
%{_libdir}/libasn1cmbuf.so.0
%{_libdir}/libasn1csbuf.so.0
%{_libdir}/libasn1ctbl.so.0

%files devel
%defattr(-,root,root,-)
%doc c-examples/ c++-examples/
%{_bindir}/snacc-config
%{_datadir}/aclocal/snacc.m4
%{_includedir}/%{name}/c
%{_includedir}/%{name}/c++
%{_libdir}/libasn1c++.so
%{_libdir}/libasn1cCebuf.so
%{_libdir}/libasn1cebuf.so
%{_libdir}/libasn1cmbuf.so
%{_libdir}/libasn1csbuf.so
%{_libdir}/libasn1ctbl.so
%{_libdir}/pkgconfig/snacc-c-ebuf.pc

%changelog
* Tue Nov 24 2015 me 1.3-1
- migrate from fc13 srpm
