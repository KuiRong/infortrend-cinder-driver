#!/bin/bash -xe

export CINDER_DIR=./cinder
export CINDER_REPO_URL=https://git.openstack.org/openstack/cinder
export CINDER_TEST_DIR=cinder/tests/unit/volume/drivers/infortrend
export INFORTREND_DRIVER_DIR=cinder/volume/drivers/infortrend

if [ -d "$CINDER_DIR" ]; then
    rm -rf $CINDER_DIR
fi

git clone $CINDER_REPO_URL --depth=1

if [ ! -d "$CINDER_DIR/$INFORTREND_DRIVER_DIR" ]; then
    mkdir $CINDER_DIR/$INFORTREND_DRIVER_DIR
fi

cp ./src/* $CINDER_DIR/$INFORTREND_DRIVER_DIR/ -r
cp ./test/* $CINDER_DIR/$CINDER_TEST_DIR/ -r

cd $CINDER_DIR

./run_tests.sh -V test_infortrend_cli
./run_tests.sh test_infortrend_common
# flake8
./run_tests.sh -p

cd ..
