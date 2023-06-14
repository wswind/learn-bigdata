def main():
    str = """Hello World
    Bye World
    Hello Hadoop
    Bye Hadoop
    """
    # 文本前期处理
    strl_ist = str.replace('\n', '').lower().split(' ')
    while "" in strl_ist:
        strl_ist.remove("")

    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for str in strl_ist:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    for key,value in count_dict.items():
        print(key + "" + value)

if __name__ == "__main__":
    main()
