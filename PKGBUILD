# Script generated with Bloom
pkgdesc="ROS - cob_monitoring"
url='http://ros.org/wiki/cob_monitoring'

pkgname='ros-kinetic-cob-monitoring'
pkgver='0.6.7_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-roscpp'
'ros-kinetic-topic-tools'
)

depends=('ipmitool'
'python2-mechanize'
'python2-psutil'
'ros-kinetic-actionlib'
'ros-kinetic-cob-light'
'ros-kinetic-cob-msgs'
'ros-kinetic-cob-script-server'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rostopic'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-topic-tools'
'sysstat'
)

conflicts=()
replaces=()

_dir=cob_monitoring
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_monitoring $srcdir/cob_monitoring
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

