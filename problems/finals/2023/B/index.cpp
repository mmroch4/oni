#include <bits/stdc++.h>

using namespace std;

map<int, int> cells;
unordered_set<int> has_cells;

int find(int a)
{
  if (cells[a] < 0)
  {
    return a;
  }

  return find(cells[a]);
}

void unite(int a, int b)
{
  int c = find(a);
  int d = find(b);

  if (cells[d] < cells[c])
  {
    swap(c, d);
  }
  
  cells[c] += cells[d];
  cells[d] = c;
}

vector<pair<int, int>> get_neighbors(pair<int, int> a)
{
  return { {a.first - 1, a.second}, {a.first + 1, a.second}, {a.first, a.second - 1}, {a.first, a.second + 1} };
}

int main()
{
  int p, n, q, j, t, d, l, c;

  cin >> p >> n >> q;

  if (p == 1)
  {
    for (int i = 0; i < n; i++)
    {
      cin >> j;

      has_cells.insert(j);
      cells[j] = -1;

      if (has_cells.count(j - 1))
      {
        unite(j, j - 1);
      }

      if (has_cells.count(j + 1))
      {
        unite(j, j + 1);
      }
    }
    
    while (q--)
    {
      cin >> t >> d;

      if (t == 1)
      {
        has_cells.insert(d);
        cells[d] = -1;

        if (has_cells.count(d - 1))
        {
          unite(d, d - 1);
        }

        if (has_cells.count(d + 1))
        {
          unite(d, d + 1);
        }
      }
      else
      {
        if (has_cells.count(d))
        {
          cout << -1 * cells[find(d)] << "\n";
        }
        else
        {
          cout << 0 << "\n";
        }
      }
    }
  }
  else
  {
    set<pair<int, int>> grid;
    set<pair<int, int>> hasFourNeighbors;

    for (int i = 0; i < n; i++)
    {
      cin >> l >> c;

      grid.insert({l, c});
    }

    while (q--)
    {
      cin >> t >> l >> c;
      
      if (t == 1)
      {
        grid.insert({l, c});
      }
      else
      {
        if (!grid.count({l, c}))
        {
          cout << 0 << "\n";
        }
        else
        {
          int counter = 0;
          pair<int, int> a = {l, c};
          
          queue<pair<int, pair<int, int>>> nodes;
          set<pair<int, int>> visited_nodes;
          
          nodes.push({1, a});
          
          while (!nodes.empty())
          {
            auto x = nodes.front();
            bool has_four_neighbors = true;

            if (!hasFourNeighbors.count(x.second))
            {
              for (auto b : get_neighbors(x.second))
              {
                if (!grid.count(b))
                {
                  has_four_neighbors = false;
                  break;
                }
              }
              
              if (!has_four_neighbors)
              {
                counter = x.first - 1;
                break;
              }
            }

            hasFourNeighbors.insert(x.second);
            
            for (auto y : get_neighbors(x.second))
            {
              if (!visited_nodes.count(y))
              {
                nodes.push({x.first + 1, y});
              }
            }
            
            nodes.pop();
          }
          
          cout << 1 + 2 * counter << "\n";
        }
      }
    }
  }
}