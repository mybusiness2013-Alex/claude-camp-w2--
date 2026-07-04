# test_todo_manager.py
# 用 pytest 测试 todo_manager.py 里的"用户反馈"功能。
# 运行方法：在本文件夹打开终端，输入  python -m pytest
#
# 小知识：tmp_path 是 pytest 送给我们的"临时文件夹"，
# 每个测试用一个全新的空文件夹，测试完自动清理，
# 这样测试就不会弄脏真正的 feedback.json。

from todo_manager import save_feedback, load_feedback


# --- 正常情况 ---

def test_保存一条反馈成功(tmp_path):
    file = str(tmp_path / "feedback.json")
    result = save_feedback("界面很好用！", filename=file)

    assert result is True                     # 保存应该成功
    feedback_list = load_feedback(file)
    assert len(feedback_list) == 1            # 文件里应该有 1 条
    assert feedback_list[0]["内容"] == "界面很好用！"
    assert "时间" in feedback_list[0]          # 每条反馈都要带时间


def test_多条反馈会追加而不是覆盖(tmp_path):
    file = str(tmp_path / "feedback.json")
    save_feedback("第一条", filename=file)
    save_feedback("第二条", filename=file)

    feedback_list = load_feedback(file)
    assert len(feedback_list) == 2
    assert feedback_list[0]["内容"] == "第一条"
    assert feedback_list[1]["内容"] == "第二条"


# --- 边界情况 ---

def test_首尾空格会被去掉(tmp_path):
    file = str(tmp_path / "feedback.json")
    save_feedback("  有空格的反馈  ", filename=file)

    assert load_feedback(file)[0]["内容"] == "有空格的反馈"


def test_没有反馈文件时返回空列表(tmp_path):
    file = str(tmp_path / "不存在的文件.json")
    assert load_feedback(file) == []


# --- 异常情况 ---

def test_空反馈被拒绝(tmp_path):
    file = str(tmp_path / "feedback.json")

    assert save_feedback("", filename=file) is False      # 空字符串
    assert save_feedback("   ", filename=file) is False   # 只有空格
    assert save_feedback(None, filename=file) is False    # None
    assert load_feedback(file) == []                      # 什么都没保存


def test_文件损坏时不会报错(tmp_path):
    file = str(tmp_path / "feedback.json")
    # 故意写入一段不是 JSON 的内容，模拟文件损坏
    with open(file, "w", encoding="utf-8") as f:
        f.write("这不是JSON{{{")

    assert load_feedback(file) == []                      # 损坏 → 当作空列表
    assert save_feedback("损坏后还能继续用", filename=file) is True
    assert len(load_feedback(file)) == 1
