

class StaticList:

    #根据一个列表然后去重，并且统计重复的个数
    def QuCHongAndStaticNum(self,pre_list):
        static_list = []
        yuan_list = pre_list
        quchong_list = []
        quchong_tongji_num_list = []  #去重统计的列表个数
        print("原始列表：")
        print(yuan_list)
        for one in yuan_list:
            if one not in quchong_list:
                quchong_list.append(one)
        print("去重后列表：")
        print(quchong_list)

        for item in quchong_list:
            quchong_tongji_num_list.append(yuan_list.count(item))

        print("去重后列表元素在原列表中的个数统计列表：")
        print(quchong_tongji_num_list)
        static_list.append(quchong_list)
        static_list.append(quchong_tongji_num_list)
        print("返回的列表：")
        print(static_list)
        return static_list

    #返回一个列表去重后的列表
    def quChong(self,yuan_list):
        yuan_list = yuan_list
        quchong_list = []
        for one in yuan_list:
            if one not in quchong_list:
                quchong_list.append(one)
        print("去重后列表：")
        print(quchong_list)
        return quchong_list

    #返回一个元素在列表中所有下标的列表
    def getXiaBiaoList(self,yuan_list,yuansu):
        lst = yuan_list
        toFind = yuansu
        # 利用list(range(len(lst)))创建下标列表，再利用filter函数筛选出所有满足条件的下标
        mubiao_list = list(filter(lambda x: lst[x] == toFind, list(range(len(lst)))))
        print("元素【%s】在列表【%s】中的所有下表组成的列表数据："%(str(toFind),str(lst)))
        print(mubiao_list)
        return mubiao_list


    #一个列表数据为维度，统计其在另一个列表中的个数
    def getOneInOtherOneCount(self,one_list,other_one_list):

        one_in_other_num_list = []
        one_list = self.quChong(one_list)
        other_one_list = other_one_list
        for item in one_list:
            one_in_other_num_list.append(other_one_list.count(item))

        print("统计维度列表内容：")
        print(one_list)
        print("对应的个数：")
        print(one_in_other_num_list)
        return one_in_other_num_list


    #处理两列数据并返回，返回的数据，第一列为去重后的主列表数据，第二列为去重后的统计维度，之后为每个维度的个数
    def handleTwoList(self,zhu_list,fu_list):
        static_list = []
        zhu_list = zhu_list
        fu_list = fu_list
        zhu_quchong_list = self.quChong(yuan_list=zhu_list)
        fu_quchong_list = self.quChong(yuan_list=fu_list)
        static_list.append(zhu_quchong_list)
        static_list.append(fu_quchong_list)
        #以主列表为维度，统计辅列表中的数据
        for one in zhu_quchong_list:
            print(one)
            one_erci_fu_list = []   #一次数据，二次辅列表的数据

            #获取数据在原主列表中的下表
            one_index_list = self.getXiaBiaoList(yuan_list=zhu_list,yuansu=one)
            print(one_index_list)

            #根据获取的下标，找出对应的辅列表的数据
            for one_index in one_index_list:
                one_erci_fu_list.append(fu_list[one_index])

            print("二次辅列表中的数据：")
            print(one_erci_fu_list)

            #以去重后的辅助列表为维度，统计二次辅列表中的个数
            static_one_list = self.getOneInOtherOneCount(one_list=fu_quchong_list,other_one_list=one_erci_fu_list)
            static_list.append(static_one_list)

        #static_list数据，第一列为去重后的主列表数据，第二列为去重后的统计维度，之后为每个维度的个数
        print(static_list)
        return static_list
















if __name__ == '__main__':
    from util.handle_excel.create_return_exceldata import  ReadData
    file_name = r"D:\PycharmProjects\firstflask\util\handle_excel\exceldata\dataresult.xls"
    sheet_id = 0

    test_project = "M项目专用终端定制测试bug"
    test_module = "分组数据加密通信"
    readdata = ReadData(file_name=file_name,sheet_id=sheet_id,test_project=test_project,test_module=test_module)  #实例化
    data_list_all = readdata.readData()

    zhu_list = data_list_all[0]
    print("主列表：")
    print(zhu_list)
    fu_list = data_list_all[3]
    print(fu_list)
    sl = StaticList()
    # sl.QuCHongAndStaticNum(pre_list=pre_list)
    sl.handleTwoList(zhu_list=zhu_list,fu_list=fu_list)


