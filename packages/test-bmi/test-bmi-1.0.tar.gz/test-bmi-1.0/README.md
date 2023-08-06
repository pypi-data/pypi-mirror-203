BMI 計算器

這是一個簡單的命令列 BMI 計算器，它可以通過使用者輸入自己的體重和身高來計算出其 BMI 值。
如何使用

使用者可以在命令列中運行該腳本，並傳遞 --weight 和 --height 兩個參數。例如：

shell

python bmi_calculator.py --weight 65 --height 170

將會輸出：

shell

您的 BMI 值為 22.49

參數說明

    --weight：使用者的體重，單位為公斤。
    --height：使用者的身高，單位為公分。

函數說明
calculate_bmi(weight, height)

這是一個計算 BMI 值的函數。它接受兩個參數，即使用者的體重和身高，並返回其 BMI 值。
參數

    weight：使用者的體重，單位為公斤。
    height：使用者的身高，單位為公分。

返回值

返回使用者的 BMI 值。
main()

這是該腳本的主函數，它使用 argparse 模塊來解析命令列參數，並調用 calculate_bmi() 函數來計算 BMI 值，最終將其輸出到命令列中。
備註

    該腳本運行時需要 Python 3.6 或以上版本。
    如果使用者未傳遞 --weight 或 --height 參數，腳本將會報錯。
    該腳本是一個非常簡單的 BMI 計算器，不包含任何錯誤處理或邊界檢查功能。
