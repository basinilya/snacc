## Process this file with automake to produce Makefile.in

AUTOMAKE_OPTIONS = 1.3 foreign

SUBDIRS	= compiler c-lib c++-lib tbl-tools asn1specs @TCLDIRS@ doc
EXTRA_DIST = \
	c++-examples c-examples \
	version-gen \
	version.h policy.h snacc.h snacc.m4
bin_SCRIPTS = snacc-config
cpkgincludedir = $(pkgincludedir)/c
cpkginclude_HEADERS = policy.h snacc.h snaccconfig.h
cxxpkgincludedir = $(pkgincludedir)/c++
cxxpkginclude_HEADERS = $(cpkginclude_HEADERS)
m4datadir = $(datadir)/aclocal
m4data_DATA = snacc.m4

pkgconfigdir = $(libdir)/pkgconfig

pkgconfig_DATA = snacc-c-ebuf.pc

noinst_DATA = snacc-c-ebuf-uninstalled.pc

dist-hook:
	printf "%s\n" "$(VERSION)" >$(distdir)/.tarball-version
