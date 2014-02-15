#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import httplib2

h = httplib2.Http()
#豆腐模具
(resp_headers, content) = h.request("http://s.taobao.com/search?initiative_id=staobaoz_20140216&js=1&q=%B6%B9%B8%AF%C4%A3%BE%DF&stats_click=search_radio_all%3A1", "GET")
url = content[content.index('p4pItems'):content.index('p4pShop')-1]
url = url[url.index(':') + 1:].strip()[1:-2]

(resp_headers, content) = h.request(url, "GET")
p4p_sidebar = content[content.index("["): content.index("__p4p_bottom__")]
p4p_bottom = content[content.index("__p4p_bottom__") + 17:content.index("_back")]

#TODO
'''
获取到p4p_sider_item_info，需要转换成加密字符串，并构造点击请求
'''
print content