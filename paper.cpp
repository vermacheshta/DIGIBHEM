#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
        srand(time(NULL));    
        int user = 0;
        int computer = 0;
        cout << "stone paper scissor game" <<endl;
        cout << "1) rock" <<endl;
        cout << "2) paper" <<endl;
        cout << "3) scissor" <<endl;
        cin >> user;

        if(user == 1)
        {
            cout <<"you choose rock" <<endl;
        }
        else if(user == 2)
        {
            cout <<"you choose paper" <<endl;
        }
        else
        {
            cout <<"you choose scissor" << endl;
        }

        computer = rand()%3+1;
        if(computer == 1)
        {
            cout <<"computer choose rock" <<endl;
        }
        else if(computer == 2)
        {
            cout <<"computer choose paper" <<endl;
        }
        else
        {
            cout <<"computer choose scissor"<<endl;
        }

        //match
        if(user == computer)
        {
            cout <<"match tie"<<endl;
        }
        // user --> rock
        else if(user == 1)
        {
            if(computer == 2)
            {
                cout <<"you lose!" <<endl;
            }
            if(computer == 3)
            {
                cout <<"you win!" << endl;
            }
        }
        // user --> paper
         else if(user == 2)
        {
            if(computer == 1)
            {
                cout <<"you win!" <<endl;
            }
            if(computer == 3)
            {
                cout <<"you lose!" << endl;
            }
        }
        //user -->scissor
         else if(user == 3)
        {
            if(computer == 1)
            {
                cout <<"you lose!" <<endl;
            }
            if(computer == 2)
            {
                cout <<"you win!" << endl;
            }
        }
        return 0;

}














