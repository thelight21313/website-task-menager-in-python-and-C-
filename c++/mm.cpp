#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdexcept>

using namespace std;

void read(vector<string>& spisok) {
    ifstream file("/Users/ilya/PycharmProjects/pythonProject28/task1.txt");
    if (!file.is_open()) {
        cout << "Error: I can't open file for reading" << endl;
        return;
    }

    string line;
    while (getline(file, line)) {
        spisok.push_back(line);
    }
    file.close();
}//read file and writes it on the list-"spisok"
void write(vector<string>& spisok){
    ofstream outfile("/Users/ilya/PycharmProjects/pythonProject28/task1.txt");
    if (!outfile.is_open()) {
        cout << "Error: I can't open file for reading" << endl;
        return;
    }
    for (size_t i = 0; i < spisok.size(); i++) {
        outfile << spisok[i] << endl;
    }
    outfile.close();
}//writes list in to file


int main() {
    string input;
    getline(cin, input); //Get input from python script
    vector<string> spisok = {};
    string check = input.substr(input.length() - 3);//last 3 input simbols
    input = input.substr(0, input.length() - 3);//input without last 3 simbols

    if (check == "add") {
        read(spisok);
        spisok.push_back(input);
        write(spisok);
    }
    else if (check == "rem") {
        read(spisok);
        try {
            int number = stoi(input);//we are converting input from string to integer
            spisok.erase(spisok.begin() + number - 1);
            write(spisok);

        } 
        catch (const invalid_argument& e) {
            cout << "Error: failed to convert input to number" << endl;
            return 1;
        }
    }
    return 0;
}