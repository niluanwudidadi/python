#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
#include <dirent.h>
#include <set>


struct point
{
	point(int a, int b, int c, int d):x1(a),y1(b),x2(c),y2(d){}
	int x1;
	int y1;
	int x2;
	int y2;
};
using namespace std;

int main(int argc, char** argv)
{
	vector<string> nameTxt;
	vector<string> pic;
	set<string> typeName;
	DIR* path = opendir("./txt/");
	 
	if(!path)
		return -1;
	struct dirent* dir = readdir(path);
	//cout << "flag_1" << endl;
	while(dir)
	{
		if(dir->d_type != DT_DIR)
		{
			ostringstream name;
			ostringstream name1;
			name << "./txt/" << string(dir->d_name);
			name1 << string(dir->d_name);
			//cout << name.str() << endl;
			nameTxt.push_back(name.str());
			pic.push_back(name1.str());
		}
		dir = readdir(path);
	}
	closedir(path);
	//cout << "flag_2" << endl;

        //cout << nameTxt.size() << endl;
	
	for(int i = 0; i < nameTxt.size(); i++)
	{
		string imgName(pic[i], 0, pic[i].size()-4);
		//cout << imgName << endl;
                
		ifstream readTxt((nameTxt[i]).c_str());
                //cout << "../label/txt/"+nameTxt[i] << endl;
		ofstream writeXml(("./Annotations/"+imgName+".xml").c_str());
		
		vector<string> type;
		vector<point> position;
		int width;
		int height;
		readTxt >> width >> height;
		//width /=2;
		//height /=2;
		while(!readTxt.eof())
		{
			string t;
			int x1,y1,x2,y2;
			readTxt >> t >> x1 >> y1 >> x2 >> y2;

                       	if(readTxt.fail())
				break;

			if(t == string())
			{
				cout << imgName << "type empty, " << "label is error, delete the jpg and xml!" << endl;
			}
			if(t == "I")
			{
				t = "i";
				cout << imgName << "DAXIE " << endl;
			}

			typeName.insert(t);
                        
                        
			if(x1<=0)
				x1 = 1;
			if(y1<=0)
				y1 = 1;
			if(x2>=width)
				x2 = width-1;
			if(y2>=height)
				y2 = height-1;
			if(x1 >= x2 || y1 >= y2)
			{
				cout << imgName << " error" << endl;
				break;
			}

			

			type.push_back(t);
			position.push_back(point(x1,y1,x2,y2));
		
		}

		//cout << type.size() << endl;
    	//for(auto i=type.begin();i!=type.end();i++)
		//	cout << *i << " ";
		//cout << endl;
		//cout << endl;
    	//for(auto i=position.begin();i!=position.end();i++)
		//{
		//	cout << (*i).x1 << " " << (*i).y1 << " " <<(*i).x2 << " " << (*i).y2 << " ";
		//	cout << endl;
		//}
		//cout << endl;
		readTxt.close();
		writeXml << "<annotation>" << endl;
		writeXml << "\t<folder>" "VOC2007"  "</folder>" << endl;
		writeXml << "\t<filename>" + string(pic[i],0,pic[i].size()-4) + ".jpg" + "</filename>" << endl;
		writeXml << "\t<source>\n\t\t<database>The VOC2007 Database</database>\n\t\t<annotation>PASCAL VOC2007</annotation>\n\t\t<image>flickr</image>\n\t\t<flickrid>341012865</flickrid>\n\t</source>\n\t<owner>\n\t\t<flickrid>Fried Camels</flickrid>\n\t\t<name>Jinky the Fruit Bat</name>\n\t</owner>";
		writeXml <<"\n\t<size>\n\t\t<width>" << width << "</width>" "\n\t\t<height>" << height << "</height>" "\n\t\t<depth>3</depth>" << "\n\t</size>" << "\n\t<segmented>0</segmented>";
		//cout << "type.size(): " << type.size() << endl;
		for(int i=0;i<type.size();i++)
		{
			writeXml << "\n\t<object>" << "\n\t\t<name>"<< type[i] << "</name>" "\n\t\t<pose>Left</pose>" "\n\t\t<truncated>1</truncated>" "\n\t\t<difficult>0</difficult>" "\n\t\t<bndbox>" "\n\t\t\t<xmin>" << position[i].x1 << "</xmin>" "\n\t\t\t<ymin>" << position[i].y1 << "</ymin>" << "\n\t\t\t<xmax>" << position[i].x2 << "</xmax>" << "\n\t\t\t<ymax>" << position[i].y2 << "</ymax>" << "\n\t\t</bndbox>" "\n\t</object>"; 
		}
		writeXml << "\n</annotation>" << endl;

		writeXml.close();
	
	}

    cout << "There are " << typeName.size() << " classes" << endl;
    cout << "Please ckeck the class number!!!" << endl;
    cout << "(" ;
    for(auto it = typeName.begin(); it != typeName.end(); ++it)
    {
	//cout << "'" << *it << "'" << "," << " ";
        cout << "'"<< *it << "'" << "," << " ";
    }
    cout << ")" << endl;
    return 0;
	
}
