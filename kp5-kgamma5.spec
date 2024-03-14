#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.11
%define		qtver		5.15.2
%define		kpname		kgamma
Summary:	kgamma5
Name:		kp5-kgamma5
Version:	5.27.11
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/kgamma5-%{version}.tar.xz
# Source0-md5:	a7435647063fe5a4020135c8532d3d12
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a tool for monitor gamma correction. With proper gamma
settings, your display (websites, images, etc.) will look the same on
your monitor as on other monitors. It allows you to alter the
monitor's gamma correction of the X-Server. But that's not all to do.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_kgamma_init.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kgamma.so
%{_datadir}/kgamma
