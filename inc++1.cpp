#include <iostream>
using namespace std;

int main() {
// problem 1 
  for (int i = 1; i <=5; i=i*2) {
  cout << i << "\n";
}
// His time complexity is O(logn)
// Because here is i is increment by 2 in each itration


// problem :2 
for (int i = 1; i < 10; i++) {   // O(n)
	for (int j = 0; i < 5; i=i*2) { //O(logn)
  cout << i << "\n";
}
}
// so total time complexity is nlogn 
  return 0;
  
  
  
}
