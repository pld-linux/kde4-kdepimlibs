#
# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
#
%define		_state		unstable

Summary:	Personal Information Management (PIM) libraries for KDE
Summary(pl.UTF-8):	Biblioteki zarządzania informacjami osobistymi (PIM) dla KDE
%define orgname kdepimlibs
Name:		kde4-kdepimlibs
Version:	4.0.60
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	ae5c708e6428a5a0fb677cd3a5464871
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel >= 4.2.0
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-dtd42-xml
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	gpgme-devel
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pth-devel
#BuildRequires:	qt-designer-libs
BuildRequires:	qt4-build
%{?with_apidocs:BuildRequires:	qt4-doc}
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kdepimlibs4
Conflicts:	kdepimlibs4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
kdepimlibs is a collection of Personal Information Management (PIM)
libraries for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepimlibs to zestaw bibliotek PIM dla K Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE PIM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek KDE PIM
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kde4-kdelibs-devel
Obsoletes:	indexlib-devel
Obsoletes:	kdepim-libkcal-devel
Conflicts:	kdenetwork-devel < 10:3.1.90

%description devel
This package contains header files needed if you wish to build
applications based on kdepimlibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
opartych na kdepimlibs.

%prep
%setup -q -n %{orgname}-%{version}

%build
export QTDIR=%{_prefix}
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkabc.so.4.*.*
%attr(755,root,root) %{_libdir}/libkabc_file_core.so.4.*.*
%attr(755,root,root) %{_libdir}/libkcal.so.4.*.*
%attr(755,root,root) %{_libdir}/libkldap.so.4.*.*
%attr(755,root,root) %{_libdir}/libkresources.so.4.*.*
%attr(755,root,root) %{_libdir}/libktnef.so.4.*.*
%attr(755,root,root) %{_libdir}/libkxmlrpcclient.so.4.*.*
%attr(755,root,root) %{_libdir}/libgpgme++-pthread.so.1.*.*
%attr(755,root,root) %{_libdir}/libgpgme++.so.1.*.*
%attr(755,root,root) %{_libdir}/libkblog.so.4.*.*
%attr(755,root,root) %{_libdir}/libkimap.so.4.*.*
%attr(755,root,root) %{_libdir}/libkmime.so.4.*.*
%attr(755,root,root) %{_libdir}/libkpimidentities.so.4.*.*
%attr(755,root,root) %{_libdir}/libkpimutils.so.4.*.*
%attr(755,root,root) %{_libdir}/libmailtransport.so.4.*.*
%attr(755,root,root) %{_libdir}/libqgpgme.so.1.*.*
%attr(755,root,root) %{_libdir}/libgpgme++-pth.so.1.*.*
%attr(755,root,root) %{_libdir}/libsyndication.so.4.*.*

%attr(755,root,root) %{_libdir}/libkabc.so.4
%attr(755,root,root) %{_libdir}/libkabc_file_core.so.4
%attr(755,root,root) %{_libdir}/libkcal.so.4
%attr(755,root,root) %{_libdir}/libkldap.so.4
%attr(755,root,root) %{_libdir}/libkresources.so.4
%attr(755,root,root) %{_libdir}/libktnef.so.4
%attr(755,root,root) %{_libdir}/libkxmlrpcclient.so.4
%attr(755,root,root) %{_libdir}/libkblog.so.4
%attr(755,root,root) %{_libdir}/libkimap.so.4
%attr(755,root,root) %{_libdir}/libkmime.so.4
%attr(755,root,root) %{_libdir}/libkpimidentities.so.4
%attr(755,root,root) %{_libdir}/libkpimutils.so.4
%attr(755,root,root) %{_libdir}/libmailtransport.so.4
%attr(755,root,root) %{_libdir}/libsyndication.so.4

%attr(755,root,root) %{_libdir}/kde4/kabc_directory.so
%attr(755,root,root) %{_libdir}/kde4/kabc_file.so
%attr(755,root,root) %{_libdir}/kde4/kabc_ldapkio.so
%attr(755,root,root) %{_libdir}/kde4/kabc_net.so
%attr(755,root,root) %{_libdir}/kde4/kabcformat_binary.so
%attr(755,root,root) %{_libdir}/kde4/kcal_local.so
%attr(755,root,root) %{_libdir}/kde4/kcal_localdir.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kresources.so
%attr(755,root,root) %{_libdir}/kde4/kcm_mailtransport.so
%attr(755,root,root) %{_libdir}/kde4/kio_imap4.so
%attr(755,root,root) %{_libdir}/kde4/kio_ldap.so
%attr(755,root,root) %{_libdir}/kde4/kio_mbox.so
%attr(755,root,root) %{_libdir}/kde4/kio_nntp.so
%attr(755,root,root) %{_libdir}/kde4/kio_pop3.so
%attr(755,root,root) %{_libdir}/kde4/kio_sieve.so
%attr(755,root,root) %{_libdir}/kde4/kio_smtp.so
                                                       
%dir %{_datadir}/apps/kabc
%{_datadir}/apps/kabc/countrytransl.map
%dir %{_datadir}/apps/kabc/formats
%{_datadir}/apps/kabc/formats/binary.desktop

%{_datadir}/apps/kconf_update/mailtransports.upd
%{_datadir}/apps/kconf_update/migrate-transports.pl

%{_datadir}/config.kcfg/mailtransport.kcfg
%{_datadir}/config.kcfg/pimemoticons.kcfg

%{_datadir}/dbus-1/interfaces/org.kde.KResourcesManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.pim.IdentityManager.xml

%{_datadir}/kde4/services/imap4.protocol
%{_datadir}/kde4/services/imaps.protocol
%{_datadir}/kde4/services/ldap.protocol
%{_datadir}/kde4/services/ldaps.protocol
%{_datadir}/kde4/services/mbox.protocol
%{_datadir}/kde4/services/nntp.protocol
%{_datadir}/kde4/services/nntps.protocol
%{_datadir}/kde4/services/pop3.protocol
%{_datadir}/kde4/services/pop3s.protocol
%{_datadir}/kde4/services/sieve.protocol
%{_datadir}/kde4/services/smtp.protocol
%{_datadir}/kde4/services/smtps.protocol

%{_datadir}/kde4/services/kcm_mailtransport.desktop
%{_datadir}/kde4/services/kresources.desktop
%dir %{_datadir}/kde4/services/kresources
%{_datadir}/kde4/services/kresources/kabc/dir.desktop
%dir %{_datadir}/kde4/services/kresources/kabc
%{_datadir}/kde4/services/kresources/kabc/file.desktop
%{_datadir}/kde4/services/kresources/kabc/ldapkio.desktop
%{_datadir}/kde4/services/kresources/kabc/net.desktop
%{_datadir}/kde4/services/kresources/kabc_manager.desktop
%dir %{_datadir}/kde4/services/kresources/kcal
%{_datadir}/kde4/services/kresources/kcal/local.desktop
%{_datadir}/kde4/services/kresources/kcal/localdir.desktop
%{_datadir}/kde4/services/kresources/kcal_manager.desktop

%{_datadir}/kde4/servicetypes/kresources_manager.desktop
%{_datadir}/kde4/servicetypes/kresources_plugin.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
#%{_includedir}/emailfunctions
%{_includedir}/kabc
%{_includedir}/kcal
%{_includedir}/kldap
%{_includedir}/kresources
%{_includedir}/ktnef
%{_includedir}/syndication
%{_includedir}/kxmlrpcclient
%{_includedir}/gpgme++
%{_includedir}/kblog
%{_includedir}/kimap
%{_includedir}/kmime
%{_includedir}/kpimidentities
%{_includedir}/kpimutils
%{_includedir}/mailtransport
%{_includedir}/qgpgme

%{_datadir}/apps/cmake/modules/*.cmake
                  
%{_datadir}/apps/libical
