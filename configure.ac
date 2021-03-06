dnl Process this file with autoconf to produce a configure script.
dnl ---
dnl	$Log: configure.ac,v $
dnl	Revision 1.3  2002/11/19 20:28:12  debacle
dnl	libtool changes.
dnl	
dnl	Revision 1.2  2002/11/19 19:37:38  debacle
dnl	Auto-tools stuff.
dnl	
dnl	Revision 1.1  2002/11/19 19:18:04  debacle
dnl	New autoconf.
dnl	
dnl	Revision 1.13  1997/09/04 13:54:04  wan
dnl	A little more portability
dnl
dnl	Revision 1.12  1997/02/28 13:39:35  wan
dnl	Modifications collected for new version 1.3: Bug fixes, tk4.2.
dnl
dnl	Revision 1.11  1997/02/16 16:50:27  rj
dnl	made return *this after calling abort()'' a compile time option.
dnl
dnl	Revision 1.10  1997/02/15 20:06:27  rj
dnl	adjust to changed AC_TRY_COMPILE macro
dnl
dnl	Revision 1.9  1997/02/15 20:01:38  rj
dnl	check whether the compiler supports volatile functions (and whether abort() is volatile).
dnl
dnl	Revision 1.8  1997/01/01 19:57:01  rj
dnl	changes for autoconf version 2.12
dnl
dnl	Revision 1.7  1995/09/07  18:36:47  rj
dnl	psbook and psnup are looked for (used by .../doc/makefile)
dnl
dnl	Revision 1.6  1995/07/24  14:44:47  rj
dnl	don't use gcc/g++ with -pipe, compiling some files may exceed virtual memory.
dnl
dnl	look for tclsh(1). tcl-lib uses it to construct the tclIndex file. don't look for Tcl/Tk if the tclsh is absent.
dnl
dnl	look for patch(1). the c-lib uses it to patch tbl.h.
dnl
dnl	search for tree-3.6's libtktree.a and set TREELIBS in .../makehead accordingly.
dnl
dnl	check for memset(3), memcpy(3) and memcmp(3). .../snacc.h reverts to bzero(3), bcopy(3) and bcmp(3) if necessary.
dnl
dnl	Revision 1.5  1995/02/20  11:18:41  rj
dnl	cpp switch HAVE_VARIABLE_SIZED_AUTOMATIC_ARRAYS added.
dnl	check for isinf(3) and finite(3) added.
dnl
dnl	Revision 1.4  1995/02/17  15:15:44  rj
dnl	hack to let makedepend find .h files the way gcc does.
dnl
dnl	Revision 1.3  1995/02/17  14:26:40  rj
dnl	adjustments for autoconf 2.x
dnl
dnl	Revision 1.2  1994/10/08  04:29:37  rj
dnl	search for Tcl/Tk
dnl
dnl	Revision 1.1  1994/09/01  00:51:22  rj
dnl	first check-in (new file).
dnl
AC_INIT( compiler/core/snacc.c, m4_esyscmd([./version-gen]))
AC_REVISION($Revision: AC_PACKAGE_VERSION $)
AM_INIT_AUTOMAKE(snacc, AC_PACKAGE_VERSION)
AM_MAINTAINER_MODE
AC_CONFIG_HEADER(config.h)
dnl --- alternative programs:
AC_PROG_MAKE_SET
AC_PROG_CC
AC_ISC_POSIX
dnl if CDPATH is set, the configure script might fail
unset CDPATH
dnl if test -n "$GCC"; then
dnl   saveCC="$CC"
dnl   CC="$CC -pipe"
dnl   AC_MSG_CHECKING( whether $saveCC takes -pipe)
dnl   AC_TRY_LINK( , , [AC_MSG_RESULT( yes)], [AC_MSG_RESULT( no); CC="$saveCC"])
dnl fi
AC_PROG_GCC_TRADITIONAL
AC_MSG_CHECKING( whether ANSI or K&R style C)
AC_TRY_COMPILE([ ], [void *p; p = "test";], [
AC_MSG_RESULT(ANSI)
AC_DEFINE( __USE_ANSI_C__)
], [
AC_MSG_RESULT(K&R)
])
AC_PROG_CXX
AC_LANG_CPLUSPLUS
dnl if test -n "$GCC"; then
dnl   saveCXX="$CXX"
dnl   CXX="$CXX -pipe"
dnl   AC_MSG_CHECKING( whether $saveCXX takes -pipe)
dnl   AC_TRY_LINK( , , [AC_MSG_RESULT( yes)], [AC_MSG_RESULT( no);CC="$saveCC"])
dnl fi
AC_MSG_CHECKING( for bool built-in)
AC_TRY_COMPILE( , bool b = false;, [AC_DEFINE( BOOL_BUILTIN) AC_MSG_RESULT( yes)], AC_MSG_RESULT( no))
AC_MSG_CHECKING( for variable sized automatic arrays)
AC_TRY_COMPILE( , changequote(<,>)int i = 42; char a[++i]; *a = i;changequote([,]), [AC_DEFINE( HAVE_VARIABLE_SIZED_AUTOMATIC_ARRAYS) AC_MSG_RESULT( yes)], AC_MSG_RESULT( no))
AC_MSG_CHECKING( for volatile functions)
AC_TRY_COMPILE( , changequote(<,>)abort();changequote([,]), [AC_MSG_RESULT( yes)], [AC_DEFINE( COMPILER_WITHOUT_VOLATILE_FUNCTIONS) SNACC_NOVOLAT=-novolat; AC_SUBST( SNACC_NOVOLAT) AC_MSG_RESULT( no)])
saveCXXFLAGS="$CXXFLAGS"; CXXFLAGS="$CXXFLAGS -fpermissive"
AC_TRY_COMPILE([ ], [int i;], [], [CXXFLAGS="$saveCXXFLAGS"])
AC_LANG_C
AM_PROG_LEX
case "$LEX" in
  lex)
    LFLAGS="-Nc10000"
  ;;
  flex)
    CFLAGS="$CFLAGS -DFLEX_IN_USE"
esac
AC_SUBST( LFLAGS)
AC_SUBST( CFLAGS)
# the boot strapping code in .../c-lib/ needs patch:
AC_CHECK_PROGS( PATCH, patch, false)
AC_PROG_YACC
AC_PROG_LN_S
AC_PROG_INSTALL
dnl --- header files:
AC_HEADER_TIME
AC_HEADER_DIRENT
AC_TYPE_SIZE_T
AC_TYPE_UID_T
AC_HEADER_STDC
AC_CHECK_HEADERS( unistd.h memory.h string.h malloc.h fcntl.h)
AC_FUNC_VPRINTF
dnl --- system and compiler characteristics:
AC_C_CONST
AC_C_BIGENDIAN
AC_CHECK_SIZEOF(short, 2)
AC_CHECK_SIZEOF(int, 4)
AC_CHECK_SIZEOF(long, 4)
AC_CHECK_SIZEOF(double, 8)
AC_CHECK_LIB( m, sin)
AC_CHECK_FUNCS( isinf finite)
AC_CHECK_FUNCS( memset memcpy memcmp)
dnl ---
AC_PATH_X
AC_PATH_XTRA
AC_CHECK_PROGS( TCLSH, tclsh, false)
if test "$TCLSH" != false && test "x$no_x" != "xyes"; then
  AC_CHECK_HEADER(
    tcl.h,
    [AC_CHECK_LIB( ld, ldopen, TCLOTHERLIBS=-lld)
    AC_CHECK_LIB(
      tcl,
      Tcl_CreateInterp,
      [saveCFLAGS="$CFLAGS"
      CFLAGS="$CFLAGS $X_CFLAGS"
      AC_CHECK_LIB(
	tk,
	Tk_CreateWindow,
	[AC_DEFINE( HAVE_TCL)
	TCLLIBS="-ltk -ltcl $TCLOTHERLIBS"
	CXXTCLDIR="tcl"
	TCLDIRS="tcl-lib tcl-asn tcl-example"
	AC_LANG_CPLUSPLUS
	AC_CHECK_LIB(
	  TkTree,
	  Tree_Init,
	  [TREELIBS="-lTkTree"],
	  [AC_MSG_RESULT( [tcl/tk libs found, but tree widget is missing])],
	  -lTkTree -ltk -ltcl $TCLOTHERLIBS $X_LIBS $X_PRE_LIBS -lX11 $X_EXTRA_LIBS)
	AC_LANG_C],
	[AC_MSG_RESULT( [tcl lib found, but tk lib is missing])],
	-ltcl $TCLOTHERLIBS $X_LIBS $X_PRE_LIBS -lX11 $X_EXTRA_LIBS)
      CFLAGS="$saveCFLAGS"],
      [AC_MSG_RESULT( [tcl library not found])],
      $TCLOTHERLIBS -lm)])
fi
AC_SUBST( CXXTCLDIR)
AC_SUBST( TCLDIRS)
AC_SUBST( TCLLIBS)
AC_SUBST( TREELIBS)
dnl ---
AC_CHECK_PROGS( LATEX, latex, false)
AC_CHECK_PROGS( BIBTEX, bibtex, false)
AC_CHECK_PROGS( DVIPS, dvips, false)
AC_CHECK_PROGS( DETEX, detex2 detex, false)
AC_CHECK_PROGS( PSPREVIEW, ghostview gs, true)
AC_CHECK_PROGS( PSBOOK, psbook, false)
AC_CHECK_PROGS( PSNUP, psnup, false)
AC_CHECK_PROGS( SPELL, ispell spell, spell)
dnl ---

dnl Configure for libtool.
AC_PROG_LIBTOOL

dnl Generate the C library build directories.
linked_files=`cd c-lib/src && ls *.c`
for dir in Cebuf ebuf mbuf sbuf tbl; do
  if test -d c-lib/$dir; then :; else
    echo creating c-lib/$dir
    mkdir c-lib/$dir
  fi
  (cd c-lib/$dir && touch Makefile.am && rm -f Makefile.in $linked_files && $LN_S ../src/*.c . )
  sed_code="-e s/libasn1cbuf/libasn1c$dir/g"
  case $dir in
  Cebuf) 
    (cd c-lib/$dir && rm -f asn-useful.c asn-useful.h tbl.c tbl.h && $LN_S ../boot/asn* ../boot/tbl* .)
    sed_code="$sed_code -e s/^.*asn-useful\.c:/neverA:/ -e s/^.*tbl\.c:/neverB:/"
    BUFFLAGS="-DCOMPILER -DUSE_NIBBLE_MEMORY=0 -DUSE_EXP_BUF -I\$(top_srcdir)/compiler/core"
    ;;
  ebuf) BUFFLAGS="-DUSE_EXP_BUF" ;;
  mbuf) BUFFLAGS="-DUSE_MIN_BUF" ;;
  sbuf) BUFFLAGS="-DUSE_SBUF" ;;
  tbl) BUFFLAGS="-DUSE_GEN_BUF -DTTBL" ;;
  esac
  echo "BUFFLAGS = $BUFFLAGS" >> c-lib/$dir/Makefile.in
  eval sed $sed_code < c-lib/src/Makefile.in >> c-lib/$dir/Makefile.in
done

dnl Generate the C++ and Tcl library build directories.
linked_files=`cd c++-lib/src && ls *.c *.C`
for dir in c++ tcl; do
  if test -d c++-lib/$dir; then :; else
    echo creating c++-lib/$dir
    mkdir c++-lib/$dir
  fi
  (cd c++-lib/$dir && touch Makefile.am && rm -f Makefile.in $linked_files && $LN_S ../src/*.c ../src/*.C .)
  sed_code="-e s/libasn1cxxtcl/libasn1$dir/g"
  case $dir in
  c++) BUFFLAGS="-DMETA=0" sed_code="$sed_code -e s/noinst/lib/g";;
  tcl) BUFFLAGS="-DTCL" sed_code="$sed_code -e s/noinst/lib/g";;
  esac
  echo "BUFFLAGS = $BUFFLAGS" >> c++-lib/$dir/Makefile.in
  eval sed $sed_code < c++-lib/src/Makefile.in >> c++-lib/$dir/Makefile.in
done  

dnl Generate snaccconfig.h.  The whether-to-generate logic is cribbed
dnl from glib-1.2.1's configure.in.  See that file for an explanation.
AC_OUTPUT_COMMANDS([
          
## Generate `snaccconfig.h' in two 
## cases:
## 1. `config.status' is run either explicitly, or via configure.
##     Esp. not when it is run in `Makefile' to generate makefiles and
##     config.h
## 2. CONFIG_OTHER is set explicitly
##
## Case 1 is difficult.  We know that `automake' sets one of
## CONFIG_FILES or CONFIG_HEADERS to empty.  This heuristic works
## only when AM_CONFIG_HEADER is set, however.

case "x$CONFIG_OTHER" in
*snaccconfig.h) gen_snaccconfig_h=yes
;;
esac
if test -n "${CONFIG_FILES}" && test -n "${CONFIG_HEADERS}"; then
  # Both CONFIG_FILES and CONFIG_HEADERS are non-empty ==> Case 1
  if test "x${CONFIG_OTHER}" = x; then
    gen_snaccconfig_h=yes
  fi
fi

## If we're generating snaccconfig.h:
## FIXME - currently, snaccconfig.h is just the normal
## config.h wrapped.  this is because the user include
## files use the normal config.h symbol names, and I 
## haven't changed those yet.
if test "x$gen_snaccconfig_h" = xyes; then
  outfile=snaccconfig.h
  echo creating $outfile
  cat <<SNACCEOF > ${outfile}-tmp
/* snaccconfig.h
 * 
 * This is an automatically generated file - please modify 'configure.in'.
 */

#ifndef _SNACCCONFIG_H
#define _SNACCCONFIG_H

SNACCEOF
  egrep -v 'PACKAGE|VERSION' config.h >> ${outfile}-tmp
  cat <<SNACCEOF >> ${outfile}-tmp

#endif /* !_SNACCCONFIG_H */
SNACCEOF
  if cmp -s ${outfile}-tmp $outfile; then
    echo $outfile is unchanged
    rm -f ${outfile}-tmp
  else
    mv ${outfile}-tmp ${outfile}
  fi
fi
])

dnl Writes files.
AC_OUTPUT(Makefile
          compiler/Makefile
          compiler/back-ends/c++-gen/Makefile
          compiler/back-ends/c-gen/Makefile
          compiler/back-ends/idl-gen/Makefile
          compiler/back-ends/Makefile
          compiler/core/Makefile
	  c-lib/Makefile
	  c-lib/inc/Makefile
	  c-lib/src/Makefile
	  c-lib/Cebuf/Makefile
	  c-lib/ebuf/Makefile
	  c-lib/mbuf/Makefile
	  c-lib/sbuf/Makefile
	  c-lib/tbl/Makefile
	  c++-lib/Makefile
	  c++-lib/inc/Makefile
	  c++-lib/src/Makefile
	  c++-lib/c++/Makefile
	  c++-lib/tcl/Makefile
          asn1specs/Makefile
          tbl-tools/berdecode/Makefile
          tbl-tools/mkchdr/Makefile
          tbl-tools/ptbl/Makefile
          tbl-tools/pval/Makefile
          tbl-tools/Makefile
          doc/Makefile
          snacc-config
		  snacc-c-ebuf.pc
		  snacc-c-ebuf-uninstalled.pc
		  ,
[if test -f snacc-config; then chmod +x snacc-config; fi])
dnl --- finis
