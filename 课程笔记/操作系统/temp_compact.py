import re

with open('进程与内存流程总览.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 去除连续3个或更多换行符，保留最多2个
content = re.sub(r'\n{3,}', '\n\n', content)

# 去除列表项之间的空行（数字列表项后不应该有空行，除非是新的段落）
lines = content.split('\n')
result = []
i = 0
while i < len(lines):
    result.append(lines[i])
    # 如果当前行是列表项（以数字开头），且下一行是空行，再下一行也是列表项，则删除空行
    if re.match(r'^\d+\.', lines[i]) and i + 1 < len(lines) and lines[i + 1].strip() == '':
        if i + 2 < len(lines) and re.match(r'^\d+\.', lines[i + 2]):
            i += 1  # 跳过空行
            continue
    i += 1

content = '\n'.join(result)

# 再次去除连续3个或更多换行符
content = re.sub(r'\n{3,}', '\n\n', content)

with open('进程与内存流程总览.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("完成！")

