%define		kdeplasmaver	5.5.4
%define		qtver		5.4.0
%define		kpname		kgamma5
Summary:	kgamma5
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a6d759ea14f106701202b8c536dfb62c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kgamma5

%prep
%setup -q -n %{kpname}-%{version}

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

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kgamma.so
%{_datadir}/kgamma/pics/background.png
%{_datadir}/kgamma/pics/cmyscale.png
%{_datadir}/kgamma/pics/darkgrey.png
%{_datadir}/kgamma/pics/greyscale.png
%{_datadir}/kgamma/pics/lightgrey.png
%{_datadir}/kgamma/pics/midgrey.png
%{_datadir}/kgamma/pics/rgbscale.png
%{_datadir}/kservices5/kgamma.desktop
