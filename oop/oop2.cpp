#include<iostream>
using namespace std;

class Publication
{
    string title;
    float price;
    public:
    void getdata()
    {
        cout<<"\nEnter the title of the book:";
        cin>>title;
        cout<<"\nEnter the price of the book:";
        cin>>price;
    }
    void display()
    {
        cout<<"\nTitle is :"<<title;
        cout<<"\nPrice is :"<<price;
    }
};

class Book: public Publication
{
    int page_count;
    public:
    void getbookdata()
    {
        cout<<"\nEnter the page count :";
        cin>>page_count;
    }
    void display_Book()
    {
    cout<<"\nPage count is :"<<page_count;
    }
};

class Tape: public Publication
{
    float time;
    public:
    void gettimedata()
    {
        cout<<"\nEnter the playing time of the Tape:";
        cin>>time;
    }
    void display_time()
    {
        cout<<"\nplaying time is:"<<time;
    }
};

int main()
{
    Book b1;
    Tape t1;
    b1.getdata();
    b1.display();
    b1.getbookdata();
    b1.display_Book();
    t1.gettimedata();
    t1.display_time();
    return 0;
}
