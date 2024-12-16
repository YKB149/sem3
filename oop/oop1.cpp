#include<iostream>
using namespace std;
class Student
{
    static int count;
    string name;
    int rollNumber;
    string Class;
    char division;
    string dateOfBirth;
    string bloodGroup;
    string contactAddress;
    int telephoneNumber;
    string drivingLicienceNumber;
    public:
    static void counter()
    {

        cout<<"\nNumber of Students are"<<count;
    }
    Student()//default constructor
    {
        Class="SE";
        division='B';
    }
    void getdata()
    {
        cout<<"Enter name";
        cin>>name;
        cout<<"Enter Rollno";
        cin>>rollNumber;
        cout<<"Enter Date of Birth";
        cin>>dateOfBirth;
        cout<<"Enter Blood Group";
        cin>>bloodGroup;
        cout<<"Enter Contact Address";
        cin>>contactAddress;
        cout<<"Enter Telephone Number";
        cin>>telephoneNumber;
        cout<<"Enter dribing licience number";
        cin>>drivingLicienceNumber;


    }
    void display()
    {
        cout<<"name is::"<<name<<endl;
        cout<<"roll Number is::"<<rollNumber<<endl;
        cout<<"class is::"<<Class<<endl;
        cout<<"division is::"<<division<<endl;
        cout<<"date of birth is::"<<dateOfBirth<<endl;
        cout<<"blood group is::"<<bloodGroup<<endl;
        cout<<"contact address is::"<<contactAddress<<endl;
        cout<<"telephone number is::"<<telephoneNumber<<endl;
        cout<<"driving licience number is::"<<drivingLicienceNumber<<endl;
        count++;
    }
    ~Student()
    {
    cout<<"\nObject Destroyed"<<endl;
    }
    Student(Student&i)
    {
        name=i.name;
        rollNumber=i.rollNumber;
        Class=i.Class;
        division=i.division;
        dateOfBirth=i.dateOfBirth;
        bloodGroup=i.bloodGroup;
        contactAddress=i.contactAddress;
        telephoneNumber=i.telephoneNumber;
        drivingLicienceNumber=i.drivingLicienceNumber;
    }
    friend class Exam;
};

class Exam
{
    int marks;
    public:
    void test(Student s1)
    {

        cout<<"Enter the marks for given rollno"<<s1.rollNumber;
        cout<<"Enter Marks";
        cin>>marks;
    }
};
int Student::count;
int main()
{
    Student s1,s3;
    Exam s;
    s1.getdata();
    //s3.getdata();
    Student s2(s1);
    s1.display();
    s2.display();
    //s3.display();
    Student::counter();
    s.test(s1);
    return 0;
}

