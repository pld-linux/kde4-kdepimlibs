#
# Conditional build:
%bcond_with	kdepim44
#
%define		qtver		4.8.1
%define		_state		stable
%define		orgname		kdepimlibs
%define		akonadiver	1.11.0

Summary:	Personal Information Management (PIM) libraries for KDE
Summary(pl.UTF-8):	Biblioteki zarządzania informacjami osobistymi (PIM) dla KDE
Name:		kde4-kdepimlibs
Version:	4.12.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	4504f286a428c4b7ff31ef9f51e606c6
Patch100:	%{name}-branch.diff
Patch101:	kdepimlibs-strict-parsing.patch
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	akonadi-devel >= %{akonadiver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gpgme-devel >= 1:1.2.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libical-devel >= 0.43
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	prison-devel
BuildRequires:	pth-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{version}-%{release}
Requires:	akonadi-libs >= %{akonadiver}
Requires:	gpgme >= 1:1.2.0
Obsoletes:	kdepimlibs4
Conflicts:	kdepimlibs4
%if %{without kdepim44}
Conflicts:	kde4-kdepim < 4.5
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepimlibs is a collection of Personal Information Management (PIM)
libraries for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepimlibs to zestaw bibliotek PIM dla K Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE PIM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek KDE PIM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Requires:	kde4-nepomuk-core-devel >= %{version}

%description devel
This package contains header files needed if you wish to build
applications based on kdepimlibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
opartych na kdepimlibs.

%prep
%setup -q -n %{orgname}-%{version}
#%%patch100 -p0
%if %{with kdepim44}
%patch101 -p1 -R
%endif

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_benchmarker
%attr(755,root,root) %{_bindir}/akonadi2xml
%attr(755,root,root) %{_bindir}/akonaditest
%attr(755,root,root) %{_libdir}/libakonadi-calendar.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-calendar.so.4
%attr(755,root,root) %{_libdir}/libakonadi-kcal.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-kcal.so.4
%attr(755,root,root) %{_libdir}/libakonadi-notes.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-notes.so.4
%attr(755,root,root) %{_libdir}/libakonadi-socialutils.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-socialutils.so.4
%attr(755,root,root) %{_libdir}/libkabc.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc.so.4
%attr(755,root,root) %{_libdir}/libkabc_file_core.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_file_core.so.4
%attr(755,root,root) %{_libdir}/libkalarmcal.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libkalarmcal.so.2
%attr(755,root,root) %{_libdir}/libkcal.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcal.so.4
%attr(755,root,root) %{_libdir}/libkcalcore.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcalcore.so.4
%attr(755,root,root) %{_libdir}/libkcalutils.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcalutils.so.4
%attr(755,root,root) %{_libdir}/libkldap.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkldap.so.4
%attr(755,root,root) %{_libdir}/libkontactinterface.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkontactinterface.so.4
%attr(755,root,root) %{_libdir}/libkmbox.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmbox.so.4
%attr(755,root,root) %{_libdir}/libkresources.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkresources.so.4
%attr(755,root,root) %{_libdir}/libktnef.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libktnef.so.4
%attr(755,root,root) %{_libdir}/libkxmlrpcclient.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkxmlrpcclient.so.4
%attr(755,root,root) %{_libdir}/libgpgme++-pthread.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpgme++-pthread.so.2
%attr(755,root,root) %{_libdir}/libgpgme++.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpgme++.so.2
%attr(755,root,root) %{_libdir}/libkblog.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkblog.so.4
%attr(755,root,root) %{_libdir}/libkimap.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkimap.so.4
%attr(755,root,root) %{_libdir}/libkmime.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmime.so.4
%attr(755,root,root) %{_libdir}/libkpimidentities.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpimidentities.so.4
%attr(755,root,root) %{_libdir}/libkpimutils.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpimutils.so.4
%attr(755,root,root) %{_libdir}/libmailtransport.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libmailtransport.so.4
%attr(755,root,root) %{_libdir}/libqgpgme.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libqgpgme.so.1
%attr(755,root,root) %ghost %{_libdir}/libsyndication.so.4
%attr(755,root,root) %{_libdir}/libsyndication.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-contact.so.4
%attr(755,root,root) %{_libdir}/libakonadi-contact.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-kde.so.4
%attr(755,root,root) %{_libdir}/libakonadi-kde.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-kmime.so.4
%attr(755,root,root) %{_libdir}/libakonadi-kmime.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-kabc.so.4
%attr(755,root,root) %{_libdir}/libakonadi-kabc.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-xml.so.4
%attr(755,root,root) %{_libdir}/libakonadi-xml.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkholidays.so.4
%attr(755,root,root) %{_libdir}/libkholidays.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpimtextedit.so.4
%attr(755,root,root) %{_libdir}/libkpimtextedit.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libmicroblog.so.4
%attr(755,root,root) %{_libdir}/libmicroblog.so.4.*.*

%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_socialfeeditem.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_knut_resource.so
%attr(755,root,root) %{_libdir}/kde4/kabc_directory.so
%attr(755,root,root) %{_libdir}/kde4/kabc_file.so
%attr(755,root,root) %{_libdir}/kde4/kabc_ldapkio.so
%attr(755,root,root) %{_libdir}/kde4/kabc_net.so
%attr(755,root,root) %{_libdir}/kde4/kabcformat_binary.so
%attr(755,root,root) %{_libdir}/kde4/kcal_local.so
%attr(755,root,root) %{_libdir}/kde4/kcal_localdir.so
%attr(755,root,root) %{_libdir}/kde4/kcm_akonadicontact_actions.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kresources.so
%attr(755,root,root) %{_libdir}/kde4/kcm_mailtransport.so
%attr(755,root,root) %{_libdir}/kde4/kio_imap4.so
%attr(755,root,root) %{_libdir}/kde4/kio_ldap.so
%attr(755,root,root) %{_libdir}/kde4/kio_mbox.so
%attr(755,root,root) %{_libdir}/kde4/kio_nntp.so
%attr(755,root,root) %{_libdir}/kde4/kio_pop3.so
%attr(755,root,root) %{_libdir}/kde4/kio_sieve.so
%attr(755,root,root) %{_libdir}/kde4/kio_smtp.so

%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kholidayswidgets.so

%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/agents
%{_datadir}/akonadi/agents/knutresource.desktop
%dir %{_datadir}/apps/kabc
%{_datadir}/apps/kabc/*countrytransl.map
%dir %{_datadir}/apps/kabc/formats
%{_datadir}/apps/kabc/formats/*binary.desktop
%dir %{_datadir}/apps/akonadi
%{_datadir}/apps/akonadi/akonadi-xml.xsd
%{_datadir}/apps/akonadi_knut_resource
%{_datadir}/apps/akonadi/contact
%dir %{_datadir}/apps/akonadi/plugins
%dir %{_datadir}/apps/akonadi/plugins/serializer
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_socialfeeditem.desktop

%dir %{_datadir}/apps/akonadi-kde
%{_datadir}/apps/akonadi-kde/kcfg2dbus.xsl

%{_datadir}/apps/kconf_update/mailtransports.upd
%{_datadir}/apps/kconf_update/migrate-transports.pl
%{_datadir}/apps/libkholidays

%{_datadir}/config.kcfg/mailtransport.kcfg
%{_datadir}/config.kcfg/recentcontactscollections.kcfg
%{_datadir}/config.kcfg/resourcebase.kcfg
%{_datadir}/config.kcfg/specialmailcollections.kcfg

%{_datadir}/dbus-1/interfaces/org.kde.KResourcesManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.pim.IdentityManager.xml

%{_datadir}/kde4/services/imap.protocol
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

%{_datadir}/kde4/services/akonadicontact_actions.desktop
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
%{_datadir}/kde4/services/kresources/kcal/localdir.desktop
%{_datadir}/kde4/services/kresources/kcal_manager.desktop

%dir %{_datadir}/kde4/services/akonadi
%dir %{_datadir}/kde4/services/akonadi/contact
%{_datadir}/kde4/services/akonadi/contact/aimprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/gaduprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/googletalkprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/groupwiseprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/icqprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/ircprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/jabberprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/meanwhileprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/msnprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/skypeprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/smsprotocol.desktop
%{_datadir}/kde4/services/akonadi/contact/yahooprotocol.desktop

%{_datadir}/kde4/servicetypes/kaddressbookimprotocol.desktop
%{_datadir}/kde4/servicetypes/kontactplugin.desktop
%{_datadir}/kde4/servicetypes/kresources_manager.desktop
%{_datadir}/kde4/servicetypes/kresources_plugin.desktop
%lang(en) %{_kdedocdir}/en/kcontrol/kresources
%lang(en) %{_kdedocdir}/en/kioslave/imap
%lang(en) %{_kdedocdir}/en/kioslave/ldap
%lang(en) %{_kdedocdir}/en/kioslave/mbox
%lang(en) %{_kdedocdir}/en/kioslave/nntp
%lang(en) %{_kdedocdir}/en/kioslave/pop3
%lang(en) %{_kdedocdir}/en/kioslave/smtp
%lang(en) %{_kdedocdir}/en/kioslave/sieve

%{_datadir}/mime/packages/kdepimlibs-mime.xml
%{_datadir}/mime/packages/x-vnd.akonadi.socialfeeditem.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/KDE/Akonadi
%{_includedir}/KDE/KABC
%{_includedir}/KDE/KAlarmCal
%{_includedir}/KDE/KBlog
%{_includedir}/KDE/KCal
%{_includedir}/KDE/KCalCore
%{_includedir}/KDE/KCalUtils
%{_includedir}/KDE/KHolidays
%{_includedir}/KDE/KIMAP
%{_includedir}/KDE/KontactInterface
%{_includedir}/KDE/KLDAP
%{_includedir}/KDE/KMime
%{_includedir}/KDE/KPIMIdentities
%{_includedir}/KDE/KPIMTextEdit
%{_includedir}/KDE/KPIMUtils
%{_includedir}/KDE/KResources
%{_includedir}/KDE/KTNEF
%{_includedir}/KDE/Mailtransport
%{_includedir}/KDE/Syndication
%{_includedir}/akonadi
%{_includedir}/kabc
%{_includedir}/kalarmcal
%{_includedir}/kcal
%{_includedir}/kcalcore
%{_includedir}/kcalutils
%{_includedir}/kholidays
%{_includedir}/kimaptest
%{_includedir}/kontactinterface
%{_includedir}/kldap
%{_includedir}/kmbox
%{_includedir}/kresources
%{_includedir}/ktnef
%{_includedir}/syndication
%{_includedir}/kxmlrpcclient
%{_includedir}/gpgme++
%{_includedir}/kblog
%{_includedir}/kimap
%{_includedir}/kmime
%{_includedir}/kpimidentities
%{_includedir}/kpimtextedit
%{_includedir}/kpimutils
%{_includedir}/mailtransport
%{_includedir}/microblog
%{_includedir}/qgpgme

%dir %{_libdir}/gpgmepp
%{_libdir}/gpgmepp/*.cmake
%{_libdir}/cmake/KdepimLibs
%{_datadir}/apps/cmake/modules/*.cmake
