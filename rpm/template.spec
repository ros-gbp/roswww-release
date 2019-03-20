Name:           ros-melodic-roswww
Version:        0.1.12
Release:        0%{?dist}
Summary:        ROS roswww package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roswww
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-rosbridge-server
Requires:       ros-melodic-rosgraph
Requires:       ros-melodic-rospack
BuildRequires:  python-catkin_pkg
BuildRequires:  python-selenium
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-rostest

%description
Feathery lightweight web server for ROS, that is based on Tornado web server
module.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Mar 20 2019 Isaac I.Y. Saito <iisaito@kinugarage.com> - 0.1.12-0
- Autogenerated by Bloom

