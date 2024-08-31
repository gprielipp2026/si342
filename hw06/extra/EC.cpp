#include <iostream>
#include <fstream>
#include "Automaton.hpp"
#include "Parser.hpp"

int main()
{
  std::ifstream file("prob4.jff", std::ifstream::in);

  if(!file.is_open()) 
  {
    std::cout << "could not open file" << std::endl;
    exit(1);
  }

  Automaton* dfa = Parser::read(file);

  std::string input;

  std::cin >> input;

  if(dfa->run(input))
  {
    std::cout << "accept" << std::endl;
  }
  else
  {
    std::cout << "reject" << std::endl;
  }

  return 0;
}
