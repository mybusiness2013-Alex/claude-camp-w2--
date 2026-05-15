# 文本词频统计器

text = input("请输入一段英文文本：\n")

# 1. 全部转成小写，忽略大小写差异
text = text.lower()

# 2. 按空格分割成单词列表
words = text.split()

# 3. 用字典统计词频
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

# 4. 按出现次数从高到低排序
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 5. 输出结果
print("\n=== 词频统计结果（从高到低）===\n")
for word, count in sorted_words:
    print(f"{word}: {count}")