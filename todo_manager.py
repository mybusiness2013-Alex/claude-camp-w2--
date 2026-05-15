import json
import os

FILE_NAME = "todos.json"

# -----------------------------
# 1. 加载本地文件（带异常处理）
# -----------------------------
def load_todos():
    if not os.path.exists(FILE_NAME):
        return []  # 文件不存在，返回空列表，不报错

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ 文件格式错误，已重置为空列表。")
        return []


# -----------------------------
# 2. 保存到本地文件
# -----------------------------
def save_todos(todos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# -----------------------------
# 3. 添加待办
# -----------------------------
def add_todo(todos):
    task = input("买牛奶、洗衣服、写代码：").strip()
    if not task:
        print("❌ 待办不能为空。")
        return

    todos.append(task)
    save_todos(todos)
    print(f"✅ 已添加：{task}")


# -----------------------------
# 4. 查看待办
# -----------------------------
def show_todos(todos):
    if not todos:
        print("📭 当前没有待办事项。")
        return

    print("\n=== 当前待办事项 ===")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")
    print()


# -----------------------------
# 5. 完成（删除）待办
# -----------------------------
def complete_todo(todos):
    show_todos(todos)
    if not todos:
        return

    try:
        index = int(input("请输入要完成的编号："))
        if 1 <= index <= len(todos):
            finished = todos.pop(index - 1)
            save_todos(todos)
            print(f"🎉 已完成：{finished}")
        else:
            print("❌ 编号超出范围。")
    except ValueError:
        print("❌ 请输入数字编号。")


# -----------------------------
# 6. 主程序循环
# -----------------------------
def main():
    todos = load_todos()

    while True:
        print("\n===== 待办事项清单 =====")
        print("1. 买牛奶、洗衣服、写代码")
        print("2. 查看清单")
        print("3. 完成待办")
        print("4. 退出程序")

        choice = input("请输入操作编号：").strip()

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            print("👋 已退出，下次会自动加载你的待办。")
            break
        else:
            print("❌ 无效输入，请输入 1-4。")


# 程序入口
main()
