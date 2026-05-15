# 客人名册管理器 Guest Manager

guest_book = {}  # 使用字典存储客人信息

def add_guest():
    name = input("请输入客人姓名：").strip()
    email = input("请输入邮箱：").strip()
    date = input("请输入加入日期（YYYY-MM-DD）：").strip()

    if not name or not email or not date:
        print("❌ 信息不能为空，请重新输入。")
        return

    guest_book[name] = {
        "email": email,
        "date": date
    }
    print(f"✅ 已成功添加：{name}")

def search_guest():
    name = input("请输入要查询的客人姓名：").strip()
    if name in guest_book:
        print("🔎 查询结果：")
        print(f"姓名：{name}")
        print(f"邮箱：{guest_book[name]['email']}")
        print(f"加入日期：{guest_book[name]['date']}")
    else:
        print("❌ 未找到该客人。")

def delete_guest():
    name = input("请输入要删除的客人姓名：").strip()
    if name in guest_book:
        del guest_book[name]
        print(f"🗑️ 已删除：{name}")
    else:
        print("❌ 名册中没有该客人。")

def main():
    while True:
        print("\n===== 客人名册管理器 =====")
        print("1. 添加客人")
        print("2. 查询客人")
        print("3. 删除客人")
        print("4. 退出系统")

        choice = input("请输入操作编号：").strip()

        if choice == "1":
            add_guest()
        elif choice == "2":
            search_guest()
        elif choice == "3":
            delete_guest()
        elif choice == "4":
            print("👋 系统已退出，再见！")
            break
        else:
            print("❌ 输入无效，请输入 1-4 之间的数字。")

# 程序入口
main()
