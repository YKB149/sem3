#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Student {
public:
    string name;
    float dob;
    long int number;

    void getData() {
        cout << "Enter Name, Date of Birth, Telephone Number::\n";
        cin >> name >> dob >> number;
    }

    string getName() {
        return name;
    }

    friend void search(vector<Student>& v, string name);
    friend void display(Student& s);
    friend bool compareByName(Student& s1, Student& s2);
};

void display(Student& s) {
    cout << s.name << "\t" << s.dob << "\t" << s.number << "\n";
}

bool compareByName(Student& s1, Student& s2) {
    return s1.name < s2.name; // Sort in ascending order
}

void search(vector<Student>& v, string name) {
    auto p = find_if(v.begin(), v.end(), [name](Student& s) {
        return s.getName() == name;
    });

    if (p != v.end()) {
        cout << "Student Found:\n";
        display(*p);
    } else {
        cout << "Student with name " << name << " not found\n";
    }
}

int main() {
    vector<Student> v1;
    Student s1;

    cout << "Insert Element in Vector :\n";
    for (int i = 0; i < 3; i++) {
        s1.getData();
        v1.push_back(s1);
    }

    cout << "Displaying the Elements in the vector::\n";
    for_each(v1.begin(), v1.end(), display);
    cout << "\n";

    cout << "Sorting using name::\n";
    sort(v1.begin(), v1.end(), compareByName);
    for_each(v1.begin(), v1.end(), display);
    
    string nameToBeSearched;
    cout << "Enter name to be searched: ";
    cin >> nameToBeSearched;
    search(v1, nameToBeSearched);

    return 0;
}

