# 爬虫相关基础

## 请求头里的Header

- Accept：文本格式
- Accept-Encoding：编码格式
- Connection：长连接， 端连接
- Cookie：验证用的
- Host： 域名
- Referer：标志从哪个页面跳转过来的
- User-Agent：浏览器和用户的信息

## 爬虫的分类

- 通用爬虫
  - 搜索引擎
  - 开放， 速度快
  - 目标不明确
  - 返回内容不精确
 - 聚焦爬虫
   - 目标明确
   - 对用户需求很精准
   - 返回内容固定

## 传参

### GET&POST

- 汉字报错：解释器ascii没有汉字，需要转码
  - urllib.parse.quote(safe='string.printable')
- 字典传参
  - urllib.parse.urlencode()

### User-Agent

模拟真实的浏览器器发送请求

### IP代理

PROXY_HANDLER