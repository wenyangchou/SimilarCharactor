# SimilarCharactor
基于音形码，EditDistance的字符串纠正相似度算法

音形码格式：【韵母，声母，结构，四角编码，笔画数】 共8位

音形码相似度算法 参考博客https://blog.csdn.net/chndata/article/details/41114771  
TODO 字符串错误匹配算法 参考

结构、四角编码 抓取http://zidian.miaochaxun.com 数据  
韵母、声母 使用pinyin包  
笔画数抓取https://bihua.51240.com 数据

入口函数在string_similarity.py

繁简切换 Done 
ongoing 相似度分值映射调整(sigmoid函数映射)
TODO 字符串包含关系 
ongoing 相似度算法添加与调整(bm25)  
TODO 字符串错位  

===============================================================================  

本人邮箱: wenyang.chou@foxmail.com

由于现在不做文本处理工作，所以理论不再继续研究

如果有idea可以联系本人邮箱，我会不定期接收算法理论并更新代码
