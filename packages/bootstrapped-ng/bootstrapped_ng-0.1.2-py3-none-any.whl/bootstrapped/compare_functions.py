# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Various comparison functions for use in bootstrap a/b tests."""


def difference(test_stat, ctrl_stat):
    """Calculate the difference change - a good default.

    Args:
        test_stat: numpy array of test statistics
        ctrl_stat: numpy array of control statistics
    Returns:
        test_stat - ctrl_stat
    """
    return test_stat - ctrl_stat


def percent_change(test_stat, ctrl_stat):
    """Calculate the percent change.

    Args:
        test_stat: numpy array of test statistics
        ctrl_stat: numpy array of control statistics
    Returns:
        (test_stat - ctrl_stat) / ctrl_stat * 100
    """
    return (test_stat - ctrl_stat) * 100.0 / abs(ctrl_stat)


def ratio(test_stat, ctrl_stat):
    """Calculate the ratio between test and control.

    Args:
        test_stat: numpy array of test statistics
        ctrl_stat: numpy array of control statistics
    Returns:
        test_stat / ctrl_stat
    """
    return test_stat / ctrl_stat


def percent_difference(test_stat, ctrl_stat):
    """Calculate the ratio between test and control.

    Useful when your statistics might be close to zero. Provides a symmetric result.

    Args:
        test_stat: numpy array of test statistics
        ctrl_stat: numpy array of control statistics
    Returns:
        (test_stat - ctrl_stat) / ((test_stat + ctrl_stat) / 2.0) * 100.0
    """
    return (test_stat - ctrl_stat) / ((test_stat + ctrl_stat) / 2.0) * 100.0
