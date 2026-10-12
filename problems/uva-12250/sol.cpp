#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    map<string, string> m = {{"HELLO", "ENGLISH"}, {"HOLA", "SPANISH"}, {"HALLO", "GERMAN"},
                             {"BONJOUR", "FRENCH"}, {"CIAO", "ITALIAN"}, {"ZDRAVSTVUJTE", "RUSSIAN"}};
    string s;
    int cs = 0;
    while (cin >> s && s != "#") {
        auto it = m.find(s);
        cout << "Case " << ++cs << ": " << (it == m.end() ? "UNKNOWN" : it->second) << "\n";
    }
}
