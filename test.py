def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag
    dagParams = DefaultDagParams()
    result = dag(dagParams, pinyinList, path_num=1, log=True)#10代表侯选值个数
    for item in result:
        socre = item.score
        res = item.path # 转换结果
        print(socre, res)

pinyin_2_hanzi(['hao kai xin'])