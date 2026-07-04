import json
import os
from datetime import datetime

FILE_NAME = "todos.json"
FEEDBACK_FILE = "feedback.json"  # 用户反馈保存在这个文件里

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
# 6. 用户反馈
# -----------------------------
# 把"逻辑"和"交互"分开写成两个函数，是为了方便测试：
# - save_feedback() 只负责保存，不用 input()，测试时可以直接调用
# - give_feedback() 负责跟用户对话，再调用上面的函数
def load_feedback(filename=FEEDBACK_FILE):
    """读取所有历史反馈，文件不存在或损坏时返回空列表（和 load_todos 同样的思路）。"""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_feedback(text, filename=FEEDBACK_FILE):
    """
    保存一条用户反馈。

    返回:
    - True  保存成功
    - False 内容为空，拒绝保存
    """
    text = text.strip() if text else ""
    if not text:
        return False

    feedback_list = load_feedback(filename)
    feedback_list.append({
        "内容": text,
        "时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(feedback_list, f, ensure_ascii=False, indent=2)
    return True


def give_feedback():
    """菜单里的"反馈按钮"：问用户要一句反馈，然后保存。"""
    text = input("💬 请写下你的意见或建议：")
    if save_feedback(text):
        print("🙏 感谢反馈，已保存！")
    else:
        print("❌ 反馈不能为空。")


# -----------------------------
# 7. 主程序循环
# -----------------------------
def main():
    todos = load_todos()

    while True:
        print("\n===== 待办事项清单 =====")
        print("1. 买牛奶、洗衣服、写代码")
        print("2. 查看清单")
        print("3. 完成待办")
        print("4. 意见反馈")
        print("5. 退出程序")

        choice = input("请输入操作编号：").strip()

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            give_feedback()
        elif choice == "5":
            print("👋 已退出，下次会自动加载你的待办。")
            break
        else:
            print("❌ 无效输入，请输入 1-5。")


# 程序入口
# if __name__ == "__main__" 的意思是：只有"直接运行"这个文件时才启动主循环；
# 如果是被测试文件 import 进去，就不会自动运行，方便单独测试每个函数。
if __name__ == "__main__":
    main()
