Summary:	GNU Binary Utility Development Utilities
Summary(de):	GNU Binary Utility Development Utilities
Summary(fr):	Utilitaires de développement binaire de GNU
Summary(pl):	Narzêdzia GNU dla programistów
Summary(tr):	GNU geliþtirme araçlarý
Name:		crossmipsel-binutils
Version:	2.11.90.0.8
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/binutils-%{version}.tar.bz2 	
Patch0:		%{name}-info.patch
URL:		http://sourceware.cygnus.com/binutils/
Prereq:		/sbin/ldconfig
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl
BuildRequires:	bash
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		mipsel-pld-linux
%define		arch		%{_prefix}/%{target}

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- c++filt - a filter for demangling encoded C++ symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

Cross version for MIPS Little Endian.

%description -l pl
Pakiet binutils zawiera zestaw narzêdzi umo¿liwiaj±cych kompilacjê
programów. Znajduj± siê tutaj miêdzy innymi assembler, konsolidator
(linker), a tak¿e inne narzêdzia do manipulowania binarnymi plikami
programów i bibliotek.

Wersja cross generuj±ca dla MIPS Little Endian.

%prep
%setup -q -n binutils-%{version}

%build
# ldscripts won't be generated properly if SHELL is not bash...
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
%ifarch sparc
sparc32 \
%endif
./configure \
	--disable-shared \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--target=%{target}

%{__make} tooldir=%{_prefix} EXEEXT="" all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	tooldir=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{target}-*
%{_libdir}/ldscripts/*
%{_mandir}/man?/%{target}-*
