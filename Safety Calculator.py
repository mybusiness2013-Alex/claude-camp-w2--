# 安全的四则运算计算器

print("=== 安全计算器（输入 quit 退出）===")

while True:
    num1 = input("请输入第一个数字： ").strip()
    if num1.lower() == "quit":
        print("👋 已退出计算器，再见！")
        break

    num2 = input("请输入第二个数字： ").strip()
    if num2.lower() == "quit":
        print("👋 已退出计算器，再见！")
        break

    op = input("请输入运算符 (+ - * /)： ").strip()
    if op.lower() == "quit":
        print("👋 已退出计算器，再见！")
        break

    # 尝试把输入转换为数字
    try:
        a = float(num1)
        b = float(num2)
    except ValueError:
        print("❌ 输入的不是数字，请重新输入。\n")
        continue

    # 运算逻辑
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("❌ 除数不能为 0，请重新输入。\n")
            continue
        result = a / b
    else:
        print("❌ 无效的运算符，请输入 + - * /。\n")
        continue

    print(f"结果：{result}\n")
