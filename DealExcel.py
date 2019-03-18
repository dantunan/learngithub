#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Tunan Dan'

from openpyxl import *
import re


class ExcelOperator:
    '''excel文件操作基类，定义了打开，关闭，保存，获取列值等操作'''
    def __init__(self, filename):
        self._filename = filename
        self._workbook = None
        self._worksheet  =None

    def open_excel(self):
        '''打开文件，并将打开的文件赋给_workbook, 将当前活动表单赋值给_worksheet'''
        try:
            self._workbook = load_workbook(filename=self._filename)
            self._worksheet = self._workbook.active
        except Exception as e:
            print('error at opening excel file', e)

    def close_excel(self):
        '''关闭excel文件'''
        self._workbook.close()

    def save_excel(self, filename=None):
        '''保存更改，如果没有指定文件名则默认更新当前文件'''
        if filename is None:
            filename = self._filename
        self._workbook.save(filename)

    def get_column(self, column_name):
        '''按照每列的第一行的单元中的内容寻找列，找到后以tuple返回列，第一行不返回'''
        for column in self._worksheet.columns:
            if column[0].value == column_name:
                return column[1:]


class SRD_ReqNumDict(ExcelOperator):
    '''SRD需求ID字典类，用于生成从WORD文档中的SRD的ID号到DOORS中SRD的ID号的对应查找表'''
    def __init__(self, filename):
        '''构造函数，输入参数为包含两类ID的excel文件'''
        super().__init__(filename)
        self.get_srd_num_dict()

    def get_srd_num_dict(self):
        '''生成ID字典，第一行为"ID_IN_MSWORD"的列包含WORD中SRD的ID，第一行为"ID_IN_DOORS"的列包含对应的DOORS中SRD的ID'''
        try:
            self.open_excel()
            num_in_msword = (cell.value for cell in self.get_column('ID_IN_MSWORD'))
            num_in_doors = (cell.value for cell in self.get_column('ID_IN_DOORS'))
            self._srdNumDict = dict(zip(num_in_msword, num_in_doors))
        except Exception as e:
            print('open excel file failed')
        else:
            self.close_excel()

    @property
    def srd_dict(self):
        '''以属性方式返回ID字典'''
        return self._srdNumDict


class ParseReqName:
    '''解析并修改SRD需求ID， 指定分隔符将多个ID分开，再利用正则表达式去掉需要删除的字符，只留数字'''
    srd = SRD_ReqNumDict('C:\\dtn\\Python\\study\\SRD.xlsx') #生成ID字典

    def __init__(self, delWords, delimeter):
        '''定义需要去除的字符和分隔符'''
        self._delWords = delWords
        self._delimeter = delimeter

    def __call__(self, rawText):
        '''先用分割符把ID隔开，再删除不想要的字符，最后再用空格将处理过的ID拼起来'''
        rm_delim = rawText.split(self._delimeter)
        rm_words = (re.sub(self._delWords, '', word) for word in rm_delim)
        replaced_words = [str(self.srd.srd_dict[word]) for word in rm_words if word in self.srd.srd_dict]
        ret_words = ' '.join(replaced_words)
        return ret_words


class DealExcel(ExcelOperator):
    '''将excel文件中的Link_ID列中WORD的SRD ID替换成DOORS中SRD的ID'''
    parseReq = ParseReqName('\s*SRD-', ',') #指定要删除的字符，以及分隔符

    def __init__(self, filename):
        super().__init__(filename)

    def update_srd_num(self):
        '''替换ID，更新并保存excel文件'''
        try:
            self.open_excel()
            column = self.get_column('Link_ID')
            for cell in column:
                cell.value = self.parseReq(cell.value)
            self.save_excel()
        except Exception as e:
            print("Excel operation failed", e)
        else:
            self.close_excel()

if __name__ == "__main__":
    d = DealExcel('C:\\dtn\\Python\\study\\Requirements.xlsx')
    d.update_srd_num()
