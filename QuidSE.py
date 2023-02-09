import requests
print("*QuidSE*初始化成功\n欢迎使用查询工具，工具版本：v1")

while True:
    qq_id = input('请输入qq号:')
    get_data = requests.get('http://zy.xywlapi.cc/qqapi?qq='+ qq_id)
    data = (get_data.json())
    s = (int(data['status']))

    if s == 200:
        print("qq号: ", data['qq'])
        print("手机号: ", data['phone'])
        print("归属地:",data['phonediqu'])
    else:
        print('没有找到')
    a = int(input('继续查询请输入0，退出请输入1'))
    if a==1:
        print('退出成功')
        break
#by MeowMeow