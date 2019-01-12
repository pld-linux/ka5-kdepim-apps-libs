%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kdepim-apps-libs
Summary:	kdepim apps libs
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	05b9fa51c2ace10bae8f15112ef1a8c9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kservice-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-prison-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains mail-related libraries.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kdepim-apps-lib.categories
/etc/xdg/kdepim-apps-lib.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5FollowupReminder.so.5
%attr(755,root,root) %{_libdir}/libKF5FollowupReminder.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KaddressbookGrantlee.so.5
%attr(755,root,root) %{_libdir}/libKF5KaddressbookGrantlee.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KaddressbookImportExport.so.5
%attr(755,root,root) %{_libdir}/libKF5KaddressbookImportExport.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KdepimDBusInterfaces.so.5
%attr(755,root,root) %{_libdir}/libKF5KdepimDBusInterfaces.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5SendLater.so.5
%attr(755,root,root) %{_libdir}/libKF5SendLater.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/FollowupReminder
%{_includedir}/KF5/KAddressBookImportExport
%{_includedir}/KF5/KaddressbookGrantlee
%{_includedir}/KF5/KdepimDBusInterfaces
%{_includedir}/KF5/SendLater
%{_includedir}/KF5/followupreminder
%{_includedir}/KF5/followupreminder_version.h
%{_includedir}/KF5/kaddressbookgrantlee
%{_includedir}/KF5/kaddressbookgrantlee_version.h
%{_includedir}/KF5/kaddressbookimportexport
%{_includedir}/KF5/kaddressbookimportexport_version.h
%{_includedir}/KF5/kdepimdbusinterfaces
%{_includedir}/KF5/kdepimdbusinterfaces_version.h
%{_includedir}/KF5/sendlater
%{_includedir}/KF5/sendlater_version.h
%{_libdir}/cmake/KF5FollowupReminder
%{_libdir}/cmake/KF5KaddressbookGrantlee
%{_libdir}/cmake/KF5KaddressbookImportExport
%{_libdir}/cmake/KF5KdepimDBusInterfaces
%{_libdir}/cmake/KF5SendLater
%attr(755,root,root) %{_libdir}/libKF5FollowupReminder.so
%attr(755,root,root) %{_libdir}/libKF5KaddressbookGrantlee.so
%attr(755,root,root) %{_libdir}/libKF5KaddressbookImportExport.so
%attr(755,root,root) %{_libdir}/libKF5KdepimDBusInterfaces.so
%attr(755,root,root) %{_libdir}/libKF5SendLater.so
%{_libdir}/qt5/mkspecs/modules/qt_FollowupReminder.pri
%{_libdir}/qt5/mkspecs/modules/qt_KaddressbookGrantlee.pri
%{_libdir}/qt5/mkspecs/modules/qt_KaddressbookImportExport.pri
%{_libdir}/qt5/mkspecs/modules/qt_KdepimDBusInterfaces.pri
%{_libdir}/qt5/mkspecs/modules/qt_SendLater.pri
