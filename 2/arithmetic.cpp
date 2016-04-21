#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  // Enter your code here. Read input from STDIN. Print output to STDOUT

  double mealCost;
  int tipPercent;
  int taxPercent;

  cin >> mealCost;
  cin >> tipPercent;
  cin >> taxPercent;

  double cost = mealCost * (1 + (tipPercent + taxPercent) / 100.0);

  double totalCost = round(cost);

  // Print your result
  cout << "The total meal cost is " << totalCost << " dollars.";

  return 0;
}
