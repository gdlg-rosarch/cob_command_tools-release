# Script generated with Bloom
pkgdesc="ROS - This package provides a simple GUI for operating Care-O-bot."
url='http://www.ros.org/wiki/cob_command_gui'

pkgname='ros-kinetic-cob-command-gui'
pkgver='0.6.7_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-pygraphviz'
'ros-kinetic-cob-msgs'
'ros-kinetic-cob-script-server'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=cob_command_gui
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_command_gui $srcdir/cob_command_gui
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

