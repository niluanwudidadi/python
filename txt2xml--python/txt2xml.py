# -*- encoding:utf-8 -*-
#!/usr/bin/env python

import os
import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='transfer txt file to xml file')
    parser.add_argument('--txt_path', dest='txt_path', help='txt file path',
                        default='./txt/', type=str)
    parser.add_argument('--xml_path', dest='xml_path', help='xml file path',
                        default="./xml/", type=str)
    args = parser.parse_args()
    return args

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    absolute_path = []
    # print "pathdir:", pathDir
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        absolute_path.append(child)
        # print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
    return absolute_path

# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r') # r 代表read
    line_list = []
    for eachLine in fopen:
        # print "读取到得内容如下：",eachLine
        eachline_list = eachLine.split(' ')
        each_temp = []
        # print "each:", eachline_list
        for each in eachline_list:

            each = re.sub("\W", "", each)
            each_temp.append(each)
        line_list.append(each_temp)
    # print line_list
    fopen.close()
    return line_list
    
# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename, width, height, class_list, location_list):
    # print filename
    xml_name = filename.replace("txt", "xml")
    name = filename.split("/")[-1]
    # print "class:",class_list
    # print "location:", location_list
    # print name[:-4]
    fopen = open(xml_name, 'w')
    fopen.write("<annotation>\n")
    fopen.write("\t<folder>" "VOC2007"  "</folder>\n")
    fopen.write("\t<filename>" + name[:-4] + ".jpg" + "</filename>\n")
    fopen.write("\t<source>\n\t\t<database>The VOC2007 Database</database>\n\t\t<annotation>PASCAL VOC2007</annotation>\n\t\t<image>flickr</image>\n\t\t<flickrid>341012865</flickrid>\n\t</source>\n\t<owner>\n\t\t<flickrid>Fried Camels</flickrid>\n\t\t<name>Jinky the Fruit Bat</name>\n\t</owner>")
    fopen.write("\n\t<size>\n\t\t<width>" + str(width) + "</width>" "\n\t\t<height>" + str(height) + "</height>" "\n\t\t<depth>3</depth>" + "\n\t</size>" + "\n\t<segmented>0</segmented>")
    for i in range(0, len(class_list)):
    	fopen.write("\n\t<object>" + "\n\t\t<name>" + str(class_list[i][0]) + "</name>" "\n\t\t<pose>Left</pose>" "\n\t\t<truncated>1</truncated>" "\n\t\t<difficult>0</difficult>" "\n\t\t<bndbox>" "\n\t\t\t<xmin>" + str(location_list[i][0]) + "</xmin>" "\n\t\t\t<ymin>" + str(location_list[i][1]) + "</ymin>" + "\n\t\t\t<xmax>" + str(location_list[i][2]) + "</xmax>" + "\n\t\t\t<ymax>" + str(location_list[i][3]) + "</ymax>" + "\n\t\t</bndbox>" "\n\t</object>")
    fopen.write("\n</annotation>")
    # fopen.write("\t<filename>" + string(pic[i],0,pic[i].size()-4) + ".jpg" + "</filename>")
    # print "\r请任意输入多行文字"," ( 输入 .号回车保存)"
    # while True:
    #     aLine = raw_input()
    #     if aLine != ".":
    #         fopen.write('%s%s' % (aLine, os.linesep))
    #     else:
    #         print "文件已保存!"
    #         break
    fopen.close()

if __name__ == '__main__':
    args = parse_args()
    txtPath = args.txt_path
    xmlPath = args.xml_path
    os.mkdir(args.xml_path)

    # read txt file absolute path
    txt_absolute_path = eachFile(txtPath)
    # print txt_absolute_path
    
    # read data by txt path
    file_data_list = []
    for txt in txt_absolute_path:
        # print txt
        line_list = readFile(txt)
        file_data_list.append(line_list)
  
    # print "line_list:", line_list
    # analyse txt data, add class to class_list, and add location to location_list 
    # print "len:", len(file_data_list)
    for i in range(0,len(file_data_list)):
        each_data = file_data_list[i]
        class_list = []
        location_list = []
        width = 0
        height = 0
        # print "each_data:",each_data
        for j in range(0,len(each_data)):
            # print "j", j
            if j == 0:
                width = each_data[j][0]
                height = each_data[j][1]
                # print "width", width
                # print "height", height
            elif j%2==1 :
                class_list.append(each_data[j])
                # print "class:", class_list
            elif j%2==0 :
                location_list.append(each_data[j])
        # print "class_list:", len(class_list)
        # print "location_list:", len(location_list)

        # print txt_absolute_path[i]
        writeFile(txt_absolute_path[i], width, height, class_list, location_list)


            # print "each_data:", each_data[j]
        # print "class_list:", len(class_list)
        # print "location_list:", len(location_list)

    # write xml according to data
    

    # print file_data_list[0]


    # writeFile(filePathI)