from util.handle_excel.operation_excel import OperationExcel

class CreateExcelFile:
    def __init__(self,file_name,sheet_id):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.oe = OperationExcel(file_name=file_name,sheet_id=sheet_id)   #实例化

    def create_get_exceldata_file(self):
        excel_lie_shu = self.oe.get_lies()
        file_name = "create_get_exceldata"
        mycontent_base = """from util.handle_excel.operation_excel import OperationExcel   #导入OperationExcel

class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化



    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
                """
        for i in range(0, int(excel_lie_shu)):
            one_add_content = """    
    def get_excel_%s(self,row):
        col = %d  
        cell_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return cell_content
            """ % (str(i), int(i))
            mycontent_base = mycontent_base + one_add_content

        mycontent_wei = """    

if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    pass"""

        mycontent_base = mycontent_base + mycontent_wei
        with open(file_name+'.py', 'w',encoding='utf-8') as f:
            f.write(mycontent_base)


    def create_return_exceldata_file(self):
        excel_lie_shu = self.oe.get_lies()
        file_name = "create_return_exceldata"
        mycontent_base = """from util.handle_excel.create_get_exceldata import GetData


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
            """
        for i in range(0, int(excel_lie_shu)):
            title_one = """            
            excel_%s = self.exceldata.get_excel_%s(i)
            """%(str(i),str(i))
            mycontent_base = mycontent_base+title_one

        for i in range(0, int(excel_lie_shu)):
            add_title_one = """
            if str(excel_%s).strip() == '':
                title_list.append('')
            else:
                title_list.append(str(excel_%s).strip())
            """%(str(i),str(i))
            mycontent_base = mycontent_base+add_title_one

        get_title_wei = """
        print(title_list)
        return title_list
        """

        mycontent_base = mycontent_base + get_title_wei

        read_data_tou = """
    def readData(self):
        """

        mycontent_base = mycontent_base + read_data_tou

        for i in range(0, int(excel_lie_shu)):
            read_data_define_list_one = """            
        excel_%s_list = [] 
            """%(str(i))
            mycontent_base = mycontent_base + read_data_define_list_one

        read_data_zhong = """
        all_list = []
        rows_count = self.exceldata.get_case_lines()   #获取表的行数
        for i in range(1,rows_count):   #循环遍历表数据
        """
        mycontent_base = mycontent_base + read_data_zhong

        for i in range(0, int(excel_lie_shu)):
            content_one = """            
            excel_%s = self.exceldata.get_excel_%s(i)
            """%(str(i),str(i))
            mycontent_base = mycontent_base+content_one

        for i in range(0, int(excel_lie_shu)):
            add_content_one = """            
            if str(excel_%s).strip()=='':
                excel_%s_list.append('')
            else:
                excel_%s_list.append(str(excel_%s).strip())
            """%(str(i),str(i),str(i),str(i))
            mycontent_base = mycontent_base+add_content_one

        for i in range(0, int(excel_lie_shu)):
            add_to_all_list_one = """
        all_list.append(excel_%s_list)
            """%str(i)
            mycontent_base = mycontent_base + add_to_all_list_one

        mycontent_wei ="""
        print('all_list')
        for one_list in all_list:
            print(one_list)
        return all_list


if __name__ == "__main__":
    pass
    file_name = r"D:\pycharmproject\firstflask\importexcel\chandao\excelbiaodata\Bug.xls"
    sheet_id = 0

    test_project = "M项目专用终端定制测试bug"
    test_module = "分组数据加密通信"
    readdata = ReadData(file_name=file_name,sheet_id=sheet_id,test_project=test_project,test_module=test_module)  #实例化
    # readdata.readData()
    readdata.getTitle()
        """
        mycontent_base = mycontent_base + mycontent_wei
        with open(file_name + '.py', 'w', encoding='utf-8') as f:
            f.write(mycontent_base)

    def run_create(self):
        self.create_get_exceldata_file()  #创建create_get_exceldata.py文件
        self.create_return_exceldata_file()   #创建create_return_exceldata.py文件





if __name__ == "__main__":

    file_name = r"D:\PycharmProjects\firstflask\util\handle_excel\exceldata\dataresult.xls"
    sheet_id = 0
    cef = CreateExcelFile(file_name=file_name,sheet_id=sheet_id)
    # cef.create_get_exceldata_file()
    # cef.create_return_exceldata_file()
    cef.run_create()

