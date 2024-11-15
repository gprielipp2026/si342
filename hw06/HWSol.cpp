#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

template <typename T, typename K>
bool contains(std::unordered_map<T,K> map, T key)
{
  try {
    map[key];
    return true;
  } catch (...) {
    return false;
  }
  // get rid of warnings
  return false;
}

bool DFA(std::string str)
{
  // define transition function
  std::unordered_map<char, std::vector<int>> delta;
  delta = {
    {'a', {1,1,2,4,2}},
    {'b', {3,2,2,2,4}}
  };
  // define win/lose states
  std::unordered_map<int, bool> W;
  W = {
    {0, false},
    {1, true},
    {2, false},
    {3, false},
    {4, true}
  };
  // state 
  int s = 0;
  for(char c : str)
  {
    if(contains(delta, c))
      s = delta[c][s];
    else
    {
      std::cout << "error: invalid symbol '" << c << "'" << std::endl;
      exit(1);
    }
  }

  return W[s];
}

int main()
{
  std::string input;
  std::cin >> input;

  if(DFA(input))
    std::cout << "accept" << std::endl;
  else
    std::cout << "reject" << std::endl; 

  return 0;
}
