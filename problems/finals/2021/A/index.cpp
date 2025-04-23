#include <bits/stdc++.h>

using namespace std;

int main() {
  int p, n, v;
  vector<int> mountains;

  cin >> p >> n;

  for (int i = 0; i < n; i++)
  {
    cin >> v;

    mountains.push_back(v);
  }
  
  stable_sort(mountains.begin(), mountains.end());

  int counter = 1;
  int acc = 0;

  for (int i = 1; i < n; i++)
  {
    if (mountains[i] == mountains[i - 1]) {
      acc += counter;
      counter++;
    }
    else {
      counter = 1;
    }
  }
  
  cout << acc << "\n";
}


/*

long long fact(int n) {
  if (n <= 1) {
    return 1;
  }

  long long acc = 1;

  for (int i = 2; i <= (long long)n; i++)
  {
    acc *= (long long)i;
  }

  return acc;
}

int main() {
  int p, n, v;
  vector<int> values;
  cin >> p >> n;

  for (int i = 0; i < n; i++)
  {
    cin >> v;

    values.push_back(v);
  }
  
  if (p == 1) {
    stable_sort(values.begin(), values.end());

    int counter = -1;
    int current = -1;

    long long acc = 0;

    for (int i = 0; i < n; i++) {
      if (values[i] == current) {
        counter++;

        if (i == n - 1 && 2 <= counter) {
          acc += fact(counter) / (2 * fact(counter - 2));
        }

        continue;
      }

      if (2 <= counter) {
        acc += fact(counter) / (2 * fact(counter - 2));
      }

      counter = 1;
      current = values[i];
    }

    cout << acc << "\n";
  }
  else {
    int acc = n;
    int m = 0;
    vector<int> odd_nums, even_nums;

    for (int i = 0; i < n; i++) {
      if (i % 2 == 0) {
        even_nums.push_back(values[i]);
      }
      else {
        odd_nums.push_back(values[i]);
      }
    }
    
    
    for (int i = 0; i < (int)even_nums.size() - 1; i++) {
      int uni_i = 2 * i;

      // cout << "RODADA: " << i << ":\n";
      for (int p = i + 1; p < (int)even_nums.size(); p++) {
        int uni_p = 2 * p;
        int middle = uni_i + floor((uni_p - uni_i) / 2);
        
        // cout << "FROM: " << i << " (" << uni_i << ") TO: " << p << " (" << uni_p << ") \n";

        auto r = *max_element(values.begin() + uni_i, values.begin() + middle);
        auto l = *max_element(values.begin() + middle + 1, values.begin() + uni_p + 1);

        if (r < values[middle] && l < values[middle]) {
          acc++;

          int range = uni_p - uni_i + 1;
          // cout << "---- MATCH -----" << "\n"; 

          if (range > m) {
            m = range;
          }
        }

        // cout << "LEFT: " << l << "RIGHT: " << r << " MIDDLE: " << values[middle] << endl;
      }
      
      // cout << "--------------- \n";
    }

    for (int i = 0; i < (int)odd_nums.size() - 1; i++) {
      int uni_i = 2 * i + 1;

      // cout << "RODADA: " << i << ":\n";
      for (int p = i + 1; p < (int)odd_nums.size(); p++) {
        int uni_p = 2 * p + 1;
        int middle = uni_i + floor((uni_p - uni_i) / 2);
        
        // cout << "FROM: " << i << " (" << uni_i << ") TO: " << p << " (" << uni_p << ") \n";

        auto r = *max_element(values.begin() + uni_i, values.begin() + middle);
        auto l = *max_element(values.begin() + middle + 1, values.begin() + uni_p + 1);

        if (r < values[middle] && l < values[middle]) {
          acc++;

          // cout << "---- MATCH -----" << "\n"; 
          
          int range = uni_p - uni_i + 1;

          if (range > m) {
            m = range;
          }
        }

        // cout << "MAIOR: " << r << " MIDDLE: " << values[middle] << endl;
      }
      
      // cout << "--------------- \n";
    }
    

    cout << m << " " << acc << "\n";
  }
}
  */