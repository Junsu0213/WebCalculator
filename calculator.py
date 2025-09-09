# Functions for calculating liver and spleen volumes

import numpy as np

def calculate_liver_volume_hwt(sex, height, weight, percentile):
    """Calculate liver volume using sex, height, and weight"""
    if sex == "Boy":
        if percentile == 5:
            return 10.8038 * weight + 2.410536 * height + 12.37625
        elif percentile == 25:
            return 14.06 * weight + 1.18 * height + 60.76
        elif percentile == 50:
            return 15.92630 * weight + 1.54535 * height + 100.25660
        elif percentile == 75:
            return 17.69 * weight + 1.60 * height + 117.65
        elif percentile == 95:
            return 20.55043 * weight + 1.935202 * height + 122.9082
    elif sex == "Girl":
        if percentile == 5:
            return 10.8038 * weight + 2.410536 * height - 30.5622
        elif percentile == 25:
            return 14.06 * weight + 1.18 * height + 26.27
        elif percentile == 50:
            return 15.92630 * weight + 1.54535 * height + 64.07086
        elif percentile == 75:
            return 17.69 * weight + 1.60 * height + 61.21
        elif percentile == 95:
            return 20.55043 * weight + 1.935202 * height + 58.21797

def calculate_spleen_volume_hwt(sex, height, weight, percentile):
    """Calculate spleen volume using sex, height, and weight"""
    if sex == "Boy":
        if percentile == 5:
            return 1.654963 * weight + 0.148408 * height + 10.94101
        elif percentile == 25:
            return 2.13 * weight + 0.08 * height + 31.01
        elif percentile == 50:
            return 2.31082 * weight + 0.359745 * height + 12.476075
        elif percentile == 75:
            return 2.97 * weight + 0.34 * height + 21.47
        elif percentile == 95:
            return 3.50866 * weight + 0.934508 * height - 14.0141
    elif sex == "Girl":
        if percentile == 5:
            return 1.654963 * weight + 0.148408 * height + 1.827813
        elif percentile == 25:
            return 2.13 * weight + 0.08 * height + 22.95
        elif percentile == 50:
            return 2.31082 * weight + 0.359745 * height - 1.205309
        elif percentile == 75:
            return 2.97 * weight + 0.34 * height + 6.14
        elif percentile == 95:
            return 3.50866 * weight + 0.934508 * height - 41.2214

def calculate_liver_volume_wt(sex, weight, percentile):
    """Calculate liver volume using sex and weight only"""
    if sex == "Boy":
        if percentile == 5:
            return 14.46748 * weight + 192.55528
        elif percentile == 25:
            return 16.29 * weight + 227.59
        elif percentile == 50:
            return 17.87202 * weight + 242.23512
        elif percentile == 75:
            return 19.40 * weight + 278.90
        elif percentile == 95:
            return 22.72654 * weight + 310.27668
    elif sex == "Girl":
        if percentile == 5:
            return 14.46748 * weight + 161.611
        elif percentile == 25:
            return 16.29 * weight + 201.15
        elif percentile == 50:
            return 17.87202 * weight + 203.24089
        elif percentile == 75:
            return 19.40 * weight + 217.10
        elif percentile == 95:
            return 22.72654 * weight + 244.6817

def calculate_spleen_volume_wt(sex, weight, percentile):
    """Calculate spleen volume using sex and weight only"""
    if sex == "Boy":
        if percentile == 5:
            return 1.804170 * weight + 38.563420
        elif percentile == 25:
            return 2.21 * weight + 38.56
        elif percentile == 50:
            return 2.763580 * weight + 45.428930
        elif percentile == 75:
            return 3.43 * weight + 50.22
        elif percentile == 95:
            return 4.696970 * weight + 58.951510
    elif sex == "Girl":
        if percentile == 5:
            return 1.804170 * weight + 16.516670
        elif percentile == 25:
            return 2.21 * weight + 31.01
        elif percentile == 50:
            return 2.763580 * weight + 32.309840
        elif percentile == 75:
            return 3.43 * weight + 36.45
        elif percentile == 95:
            return 4.696970 * weight + 46.030300
