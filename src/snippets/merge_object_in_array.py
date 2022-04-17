# arr1のオブジェクトのリスト内で、
# idが同じものを一つのオブジェクトにマージしたい。

# AsIs
asis = [{
    "id": 1,
    "name1": "taro",
    "hoge_flag": True
},{
    "id": 9,
    "name1": "taro",
    "hoge_flag": True
}, {
    "id": 9,
    "name2": "hanako",
    "fuga_flag": True
}]
# ToBe こうしたい。
tobe = [{
    "id": 1,
    "name1": "taro",
    "hoge_flag": True
},{
    "id": 9,
    "name1": "taro",
    "hoge_flag": True,
    "name2": "hanako",
    "fuga_flag": True
}]

answer = []

# 9以外にもダブりがあるときどうしようか。。
duplicated_obj = [e for e in asis if e["id"] == 9]
records = [e for e in asis if e["id"] != 9]

# duplicated_objが3つ以上あるときとかどうしようか。。
records.append(dict(duplicated_obj[0], **duplicated_obj[1]))

# うーん、、、
print(records)
print(tobe == records)


# dict同士のマージ
sample1 = {
    "id": 9,
    "name1": "taro",
    "hoge_flag": True
}

sample2 = {
    "id": 9,
    "name2": "hanako",
    "fuga_flag": True
}

# dict同士のマージは、dict()で新たに生成できる。
# print(dict(sample1, **sample2))
