from util.handle_excel.create_get_exceldata import GetData


#对数据遍历入库
class ReadData:
    def __init__(self,file_name=None,sheet_id=None,test_project=None,test_module=None):
        if file_name==None:
            self.filename = '../data/exceldata/编写测试用例.xls'
        else:
            self.filename = file_name

        if sheet_id ==None:
            self.sheetid = 0
        else:
            self.sheetid = sheet_id
        self.test_project = str(test_project)
        self.test_module = str(test_module)
        self.exceldata = GetData(file_name=self.filename,sheet_id=self.sheetid)
        
    def getTitle(self):
        title_list = []
        for i in range(0, 1):  # 循环遍历表数据
                        
            excel_0 = self.exceldata.get_excel_0(i)
                        
            excel_1 = self.exceldata.get_excel_1(i)
                        
            excel_2 = self.exceldata.get_excel_2(i)
                        
            excel_3 = self.exceldata.get_excel_3(i)
                        
            excel_4 = self.exceldata.get_excel_4(i)
                        
            excel_5 = self.exceldata.get_excel_5(i)
                        
            excel_6 = self.exceldata.get_excel_6(i)
                        
            excel_7 = self.exceldata.get_excel_7(i)
                        
            excel_8 = self.exceldata.get_excel_8(i)
                        
            excel_9 = self.exceldata.get_excel_9(i)
                        
            excel_10 = self.exceldata.get_excel_10(i)
            
            if str(excel_0).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_0).strip())
            
            if str(excel_1).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_1).strip())
            
            if str(excel_2).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_2).strip())
            
            if str(excel_3).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_3).strip())
            
            if str(excel_4).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_4).strip())
            
            if str(excel_5).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_5).strip())
            
            if str(excel_6).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_6).strip())
            
            if str(excel_7).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_7).strip())
            
            if str(excel_8).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_8).strip())
            
            if str(excel_9).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_9).strip())
            
            if str(excel_10).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_10).strip())
            
        print(title_list)
        return title_list
        
    def readData(self):
                    
        excel_0_list = [] 
                        
        excel_1_list = [] 
                        
        excel_2_list = [] 
                        
        excel_3_list = [] 
                        
        excel_4_list = [] 
                        
        excel_5_list = [] 
                        
        excel_6_list = [] 
                        
        excel_7_list = [] 
                        
        excel_8_list = [] 
                        
        excel_9_list = [] 
                        
        excel_10_list = [] 
            
        all_list = []
        rows_count = self.exceldata.get_case_lines()   #获取表的行数
        for i in range(1,rows_count):   #循环遍历表数据
                    
            excel_0 = self.exceldata.get_excel_0(i)
                        
            excel_1 = self.exceldata.get_excel_1(i)
                        
            excel_2 = self.exceldata.get_excel_2(i)
                        
            excel_3 = self.exceldata.get_excel_3(i)
                        
            excel_4 = self.exceldata.get_excel_4(i)
                        
            excel_5 = self.exceldata.get_excel_5(i)
                        
            excel_6 = self.exceldata.get_excel_6(i)
                        
            excel_7 = self.exceldata.get_excel_7(i)
                        
            excel_8 = self.exceldata.get_excel_8(i)
                        
            excel_9 = self.exceldata.get_excel_9(i)
                        
            excel_10 = self.exceldata.get_excel_10(i)
                        
            if str(excel_0).strip()=='':
                excel_0_list.append('')
            else:
                excel_0_list.append(str(excel_0).strip())
                        
            if str(excel_1).strip()=='':
                excel_1_list.append('')
            else:
                excel_1_list.append(str(excel_1).strip())
                        
            if str(excel_2).strip()=='':
                excel_2_list.append('')
            else:
                excel_2_list.append(str(excel_2).strip())
                        
            if str(excel_3).strip()=='':
                excel_3_list.append('')
            else:
                excel_3_list.append(str(excel_3).strip())
                        
            if str(excel_4).strip()=='':
                excel_4_list.append('')
            else:
                excel_4_list.append(str(excel_4).strip())
                        
            if str(excel_5).strip()=='':
                excel_5_list.append('')
            else:
                excel_5_list.append(str(excel_5).strip())
                        
            if str(excel_6).strip()=='':
                excel_6_list.append('')
            else:
                excel_6_list.append(str(excel_6).strip())
                        
            if str(excel_7).strip()=='':
                excel_7_list.append('')
            else:
                excel_7_list.append(str(excel_7).strip())
                        
            if str(excel_8).strip()=='':
                excel_8_list.append('')
            else:
                excel_8_list.append(str(excel_8).strip())
                        
            if str(excel_9).strip()=='':
                excel_9_list.append('')
            else:
                excel_9_list.append(str(excel_9).strip())
                        
            if str(excel_10).strip()=='':
                excel_10_list.append('')
            else:
                excel_10_list.append(str(excel_10).strip())
            
        all_list.append(excel_0_list)
            
        all_list.append(excel_1_list)
            
        all_list.append(excel_2_list)
            
        all_list.append(excel_3_list)
            
        all_list.append(excel_4_list)
            
        all_list.append(excel_5_list)
            
        all_list.append(excel_6_list)
            
        all_list.append(excel_7_list)
            
        all_list.append(excel_8_list)
            
        all_list.append(excel_9_list)
            
        all_list.append(excel_10_list)
            
        print('all_list')
        for one_list in all_list:
            print(one_list)
        return all_list


if __name__ == "__main__":
    pass
    file_name = r"D:\pycharmprojectirstflask\importexcel\chandao\excelbiaodata\Bug.xls"
    sheet_id = 0

    test_project = "M项目专用终端定制测试bug"
    test_module = "分组数据加密通信"
    readdata = ReadData(file_name=file_name,sheet_id=sheet_id,test_project=test_project,test_module=test_module)  #实例化
    # readdata.readData()
    readdata.getTitle()
        