#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;


int main() {
    int N;
    cin >> N;
    cin.ignore();

    string line;
    string first = "";
    string second = "";

	for (int i = 0; i < N; i++) {
      getline(cin, line);
      first = "";
      second = "";
      for (int c = 0; c < line.length(); c++) {
        if (c % 2 == 0) {
          first += line[c];
        } else {
          second += line[c];
        }
      }
      cout << first << " " << second << endl;
	}

    return 0;
}
