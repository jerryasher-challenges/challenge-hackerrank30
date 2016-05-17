#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int N;
  cin >> N;

  string statement;

  if (0 == (N % 2)) {
    if (N < 6) {
      statement = "Not Weird";
    } else if (N <= 20) {
      statement = "Weird";
    } else {
      statement = "Not Weird";
    }
  } else {
    statement = "Weird";
  }
  
  // Print your result
  cout << statement;

  return 0;
}
