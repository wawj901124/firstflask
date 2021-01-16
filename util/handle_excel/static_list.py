

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


if __name__ == '__main__':
    from importexcel.chandao.return_three_data import ReadData
    file_name = r"D:\pycharmproject\firstflask\importexcel\chandao\excelbiaodata\Bug.xls"
    sheet_id = 0

    test_project = "M项目专用终端定制测试bug"
    test_module = "分组数据加密通信"
    readdata = ReadData(file_name=file_name,sheet_id=sheet_id,test_project=test_project,test_module=test_module)  #实例化
    data_list_all = readdata.readData()

    pre_list = data_list_all[2]
    sl = StaticList()
    sl.QuCHongAndStaticNum(pre_list=pre_list)

