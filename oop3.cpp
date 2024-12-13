
//Addition of two complex number 
#include <iostream>
using namespace std;

class complex 
{
   public :
   int real,img;
   complex ()
   { 
    real=img=0;
   	
	}
    void accept()
    {
      cout<<"Enter real no = ";
      cin >> real;
      cout<<endl<<"Enter img no ";
      cin>>img;
	}
	void display ()
	{
		cout<<real<<"+"<<img<<"i";
	}
	complex operator +(complex x)
	{
		complex temp;
		temp.real=real+x.real;
		temp.img=img+x.img;
		return temp;
	}
	complex operator *(complex y)
	{
		complex temp;
		temp.real=(real*y.real)-(img*y.img);
		temp.img=(real*y.img)+(y.real*img);
	}
};

int main()
{ complex c1,c2,result;
  cout<<"Enter first complex number "<<endl;
  c1.accept();
  cout<<"Enter second complex number "<<endl;
  c2.accept();
  cout<<"First complex number = ";
  c1.display();
  cout<<endl<<"Second complex number is = ";
  c2.display();
  cout<<endl<<"Addition of two complex no is = ";
  result=c1+c2;  
  result.display();
  cout<<endl<<"multipication of two complex no is ";
  result=c1*c2;
  result.display();
}
