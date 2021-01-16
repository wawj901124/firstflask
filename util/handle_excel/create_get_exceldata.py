from util.handle_excel.operation_excel import OperationExcel   #导入OperationExcel

class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化



    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
                    
    def get_excel_0(self,row):
        col = 0  
        cell_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return cell_content
                
    def get_excel_1(self,row):
        col = 1  
        cell_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return cell_content
                
    def get_excel_2(self,row):
        col = 2  
        cell_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return cell_content
                
    def get_excel_3(self,row):
        col = 3  
        cell_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return cell_content
                

if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    pass