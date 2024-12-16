#include<iostream>
#include<fstream>
using namespace std;

class student
{
  string name;
  int roll_no;
  char division;
  
  public:
  void getdata()
  {
    ofstream out ("stud",ios::app);
    for(int i=0;i<3;i++)
    {
      cout<<"Enter Name\n";
      cin>>name;
      cout<<"Enter Roll No\n";
      cin>>roll_no;
      cout<<"Enter Division\n";
      cin>>division;
      out<<name<<"\t"<<roll_no<<"\t"<<division<<"\n";
    }
    out.close();
  }
  
  void display()
  {
    char line[20];
    ifstream in("stud");
    while(in)
    {
      in.getline(line,20);
      cout<<line<<endl;
    }
    for(int i=0;i<3;i++)
    {
      in>>name>>roll_no>>division;
      cout<<name<<"\t"<<roll_no<<"\t"<<division<<"\n";
    }
    in.close();
  }
};

int main()
{
  student s1;
  s1.getdata();
  s1.display();
  
  return 0;
}
