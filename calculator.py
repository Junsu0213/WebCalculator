# 간 및 비장 부피 계산 함수들

import numpy as np

def calculate_liver_volume_hwt(sex, height, weight, percentile):
    """성별, 키, 체중을 사용한 간 부피 계산"""
    if sex == "Boy":
        if percentile == 5:
            return 10.8038 * weight + 2.410536 * height + 12.37625
        elif percentile == 50:
            return 15.92630 * weight + 1.54535 * height + 100.25660
        elif percentile == 95:
            return 20.55043 * weight + 1.935202 * height + 122.9082
    elif sex == "Girl":
        if percentile == 5:
            return 10.8038 * weight + 2.410536 * height - 30.5622
        elif percentile == 50:
            return 15.92630 * weight + 1.54535 * height + 64.07086
        elif percentile == 95:
            return 20.55043 * weight + 1.935202 * height + 58.21797

def calculate_spleen_volume_hwt(sex, height, weight, percentile):
    """성별, 키, 체중을 사용한 비장 부피 계산"""
    if sex == "Boy":
        if percentile == 5:
            return 1.654963 * weight + 0.148408 * height + 10.94101
        elif percentile == 50:
            return 2.31082 * weight + 0.359745 * height + 12.476075
        elif percentile == 95:
            return 3.50866 * weight + 0.934508 * height - 14.0141
    elif sex == "Girl":
        if percentile == 5:
            return 1.654963 * weight + 0.148408 * height + 1.827813
        elif percentile == 50:
            return 2.31082 * weight + 0.359745 * height - 1.205309
        elif percentile == 95:
            return 3.50866 * weight + 0.934508 * height - 41.2214

def calculate_liver_volume_wt(sex, weight, percentile):
    """성별, 체중만 사용한 간 부피 계산"""
    if sex == "Boy":
        if percentile == 5:
            return 14.46748 * weight + 192.55528
        elif percentile == 50:
            return 17.87202 * weight + 242.23512
        elif percentile == 95:
            return 22.72654 * weight+310.27668
    elif sex == "Girl":
        if percentile == 5:
            return 14.46748 * weight + 161.611
        elif percentile == 50:
            return 17.87202 * weight + 203.24089
        elif percentile == 95:
            return 22.72654 * weight+244.6817

def calculate_spleen_volume_wt(sex, weight, percentile):
    """성별, 체중만 사용한 비장 부피 계산"""
    if sex == "Boy":
        if percentile == 5:
            return 1.804170 * weight+  38.563420
        elif percentile == 50:
            return 2.763580 * weight + 45.428930
        elif percentile == 95:
            return 4.696970 * weight + 58.951510
    elif sex == "Girl":
        if percentile == 5:
            return 1.804170 * weight + 16.516670
        elif percentile == 50:
            return 2.763580 * weight + 32.309840
        elif percentile == 95:
            return 4.696970 * weight + 46.030300

def calculate_regression_lines(sex, age_group):
    weights = np.linspace(0, 200, 200)
    if sex == "Boy":
        if age_group == "under_6":
            height = 105
        elif age_group == "6_to_11":
            height = 135.95
        elif age_group == "12_and_above":
            height = 170
    elif sex == "Girl":
        if age_group == "under_6":
            height = 106
        elif age_group == "6_to_11":
            height = 135.6
        elif age_group == "12_and_above":
            height = 160

    # Liver volume regression lines
    liver_5 = 10.8038 * weights + 2.410536 * height + (12.37625 if sex == "Boy" else -30.5622)
    liver_50 = 15.92630 * weights + 1.54535 * height + (100.25660 if sex == "Boy" else 64.07086)
    liver_95 = 20.55043 * weights + 1.935202 * height + (122.9082 if sex == "Boy" else 58.21797)

    # Spleen volume regression lines
    spleen_5 = 1.654963 * weights + 0.148408 * height + (10.94101 if sex == "Boy" else 1.827813)
    spleen_50 = 2.31082 * weights + 0.359745 * height + (12.476075 if sex == "Boy" else -1.205309)
    spleen_95 = 3.50866 * weights + 0.934508 * height + (-14.0141 if sex == "Boy" else -41.2214)

    return {
        'liver': {'5th': liver_5, '50th': liver_50, '95th': liver_95},
        'spleen': {'5th': spleen_5, '50th': spleen_50, '95th': spleen_95}
    }