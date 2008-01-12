# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden'
					# & '--fvisibility-inlines-hidden'
					# to g++

%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	Personal Information Management (PIM) for KDE
Summary(ko.UTF-8):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl.UTF-8):	Manadżer informacji osobistej (PIM) dla KDE
Summary(ru.UTF-8):	Персональный планировщик (PIM) для KDE
Summary(uk.UTF-8):	Персональный планувальник (PIM) для KDE
%define orgname kdepimlibs
Name:		kdepimlibs4
Version:	4.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	1a68662230fcd4ec8cea90bb780f920e
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel >= 4.2.0
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtXml-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-dtd42-xml
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gpgme-devel
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs4-devel >= %{_minlibsevr}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pth-devel
#BuildRequires:	qt-designer-libs
BuildRequires:	qt4-build
%{?with_apidocs:BuildRequires:	qt4-doc}
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	akregator
Obsoletes:	kdeaddons-kontact
Obsoletes:	kdepim-kontact
Obsoletes:	kdepim-korganizer
Obsoletes:	kdepim-kresources
Obsoletes:	kdepim-ksync
#Obsoletes:	kdepim-libkcal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%description -l ru.UTF-8
kdepim - это набор утилит для управления персональной информацией для
K Desktop Environment (KDE).

%description -l uk.UTF-8
kdepim - це набір утиліт для керування персональною информацією для K
Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl.UTF-8):	Pliki nagłówkowe do KDE pim
Summary(ru.UTF-8):	Файлы разработки для kdepim
Summary(uk.UTF-8):	Файли розробки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs4-devel >= %{_minlibsevr}
Obsoletes:	indexlib-devel
Obsoletes:	kdepim-libkcal-devel
Conflicts:	kdenetwork-devel < 10:3.1.90

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
bazujących na kdepim.

%description devel -l uk.UTF-8
Цей пакет містить файли заголовків необхідні для побудови програм,
базованих на kdepim.

%description devel -l ru.UTF-8
Этот пакет содержит файлы заголовков необходимые для построения
программ, основанных на kdepim.

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
%{_libdir}/*.so
