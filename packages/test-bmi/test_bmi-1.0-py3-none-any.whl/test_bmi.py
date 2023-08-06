#!/usr/bin/env python
import argparse

def calculate_bmi(weight, height):
    """
    計算 BMI 值
    :param weight: 體重，單位：公斤
    :param height: 身高，單位：公分
    :return: BMI 值
    """
    height_in_meters = height / 100.0  # 將身高從公分換算成公尺
    bmi = weight / (height_in_meters ** 2)  # 計算 BMI 值
    return bmi
    
def main():
    # 建立命令列解析器
    parser = argparse.ArgumentParser(description='BMI 計算器')

    # 設定命令列參數
    parser.add_argument('--weight', type=float, required=True, help='您的體重（公斤）')
    parser.add_argument('--height', type=float, required=True, help='您的身高（公分）')

    # 解析命令列參數
    args = parser.parse_args()

    # 計算 BMI 值
    bmi = calculate_bmi(args.weight, args.height)

    # 輸出結果
    print(f"您的 BMI 值為 {bmi:.2f}")

if __name__ == '__main__':
    main()
    