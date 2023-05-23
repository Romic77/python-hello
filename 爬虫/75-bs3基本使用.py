from bs4 import BeautifulSoup

# 解析本地文件 对基础语法进行讲解
soup = BeautifulSoup(open('75-bs4的基本使用.html', 'r', encoding='utf-8'), 'lxml')
print(soup)

print(soup.a.attrs)

# bs4 函数
print(soup.find('a', title='a2'))

print(soup.find('a', class_='a1'))

print(soup.findAll('a'))

print(soup.findAll('a', limit=1))

print(soup.select('a'))

print(soup.select('.a1'))

print(soup.select('li[id="l2"]'))

# 获取div下面的所有li
print(soup.select('div li'))

# 获取ul下面的li
print(soup.select('ul>li'))

# 找到li标签和a标签
print(soup.select('div a,li'))

print(soup.select('#d1')[0].get_text())

obj = soup.select('#p1')[0]
print(obj.name)
print(obj.attrs.get('class'))
