#ifndef PARSER_HPP
#define PARSER_HPP

#include <iostream>
#include <string>
#include <sstream>
#include "State.hpp"
#include "Transition.hpp"
#include "Automaton.hpp"

#include <algorithm>
#include <cctype>
#include <locale>
void trim(std::string& str)
{
  //stackoverflow.com/questions/216823/how-to-trim-a-stdstring
  // trim left
  str.erase(str.begin(), std::find_if(str.begin(), str.end(), [](unsigned char c) { return !std::isspace(c); }));
  // trim right
  str.erase(std::find_if(str.rbegin(), str.rend(), [](unsigned char c) { return !std::isspace(c); }).base(), str.end());
}

class Parser
{
  public:
    static Automaton* read(std::istream& is)
    {
      std::string line;
      Automaton* dfa = new Automaton();
      std::stringstream newStream("");
      while(!is.eof())
      {
        std::getline(is, line);
        trim(line);

        //std::cout << "read line: " << "\"" << line << "\"" << std::endl;
          
        newStream << line << std::endl;  
       
        //std::cout << (line == "<transition>") << std::endl;

        if(line == "<transition>")
        {
          newStream = std::stringstream("");
          newStream << line << std::endl;;
        } else if(line == "</transition>")
        {
          //std::cout << "\ntransition complete\n" << newStream.str() << std::endl << std::endl;
          dfa->addTransition(Transition::read(newStream));
        }

        else if(line.find("<state") != std::string::npos)
        {
          newStream = std::stringstream("");
          newStream << line << std::endl;
        } else if(line == "</state>")
        {
          //std::cout << "\nstate complete\n" << newStream.str() << std::endl;
          dfa->addState(State::read(newStream));
        }
      
      }
    
      return dfa;
    }
};

#endif//PARSER_HPP
