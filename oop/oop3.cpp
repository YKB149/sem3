#include <iostream>
using namespace std;
class complex
{
int r, i;
public:
complex() : r(0), i(0) {}
complex(int real, int imag) : r(real), i(imag) {}
void display()
{
cout << "Complex number is: " << r << "+" << i << "i" << endl;
}
friend istream& operator>>(istream &in, complex &c);
friend ostream& operator<<(ostream &out,complex &c);
friend complex operator+(complex &c1,complex &c2);
};
istream& operator>>(istream &in, complex &c)
{
cout << "Enter real part: ";
in >> c.r;
cout << "Enter imaginary part: ";
in >> c.i;
return in;
}
ostream& operator<<(ostream &out,complex &c)
{
out << c.r << "+" << c.i << "i";
return out;
}
complex operator+(complex &c1, complex &c2)
{
return complex(c1.r + c2.r, c1.i + c2.i);
}
int main()
{
complex c1, c2;
cout << "Enter the first complex number:" << endl;
cin >> c1;
cout << "Enter the second complex number:" << endl;
cin >> c2;
complex c3 = c1 + c2;
cout << "The sum of the complex numbers is: " << c3 << endl;
return 0;
}
