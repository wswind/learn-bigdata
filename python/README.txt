pip安装：

pacman -S python-pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

python -m venv .venv
source .venv/bin/activate

退出venv：
deactivate

pip install pyspark

提交 python：
spark-submit wordcount-spark.py


使用hdfs地址：
 """3. 具体的逻辑编写"""
    input_rdd: RDD = spark.sparkContext.textFile('hdfs://node1:8020/datas/input/spark by wiki.txt')

    # 进行具体的切割
    res_df = (input_rdd
              .flatMap(lambda line: re.split('\\s+', line))
              .filter(lambda word: word != '')
              .map(lambda word: (word, 1))
              .reduceByKey(lambda tmp, value: value + tmp)
              .sortBy(lambda pair: pair[1], ascending=False)
              .take(5))

    print(res_df)

>>  [('Spark', 67), ('the', 67), ('a', 54), ('and', 51), ('of', 50)]