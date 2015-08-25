Name:           ros-indigo-cob-teleop
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS cob_teleop package

Group:          Development/Libraries
License:        LGPL
URL:            http://www.ros.org/wiki/cob_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-cob-script-server
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-script-server
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-trajectory-msgs

%description
teleop_node_of_v2

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Aug 25 2015 Florian Weisshardt, Maximilian Sieber <fmw@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Weisshardt, Maximilian Sieber <fmw@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

