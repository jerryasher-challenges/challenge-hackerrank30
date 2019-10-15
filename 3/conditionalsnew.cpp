#include <bits/stdc++.h>

using namespace std; 

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
      string result;

  if (0==(N % 2)) {
    if (N < 6) {
      result = "Not Weird";
    } else if (N <= 20) {
      result = "Weird";
    } else {
      result = "Not Weird";
    }
  } else {
    result = "Weird";
  }
  
  // Print your result
  cout << result;

    return 0;
}
