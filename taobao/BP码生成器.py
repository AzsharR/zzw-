import re
url = input("请输入淘宝商品url(选择好鞋码和款式并在输入空格后在输入URL): ")
# url = "https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w5003-22606865535.1.662e174aLmBEJD&id=555426359283&scene=taobao_shop&skuId=4502054706437"
#

id = re.findall(r'BEJD&id=(.+?)&scene',url)
print(id)
skuid = re.findall(r'shop&skuId=(.+?)$',url)
print(skuid)


idz = ''.join(id)
skuidz = ''.join(skuid)


print("BP码是：https://h5.m.taobao.com/cart/order.html?itemId=%s&item_num_id=%s&_input_charset=utf-8&buyNow=true&v=0&skuId=%s&quantity=1&spm=a215p.8274340.4.d1&visa=701e9209f542c59d&_s"%(idz,idz,skuidz))

