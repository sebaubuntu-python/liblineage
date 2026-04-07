#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: LGPL-3.0-or-later
#

from enum import Enum

class Period(Enum):
	"""Enum representing a build period"""
	NIGHTLY = "N"
	WEEKLY = "W"
	MONTHLY = "M"
