#include<iostream>

using namespace std;

class EXP
{
	private:
		char post[40];
		int top,st[20];
	public:
		EXP()
		{
			top=0;
		}
		void postfix(char inf[40]);
		void push(int);
		char pop();
};

void EXP::postfix(char inf[40])
{
	int i,j=0;
	for(i=0;inf[i]!='\0';i++)
	{
	switch(inf[i])
	{
		case '+': while(st[top]>=1)
			  post[j++] = pop();
			  push(1);
			  break;
			  
		case '-': while(st[top]>=1)
			  post[j++] = pop();
			  push(2);
			  break;
			  
		case '*': while(st[top]>=3)
			  post[j++] = pop();
			  push(3);
			  break;
			  
		case '/': while(st[top]>=3)
			  post[j++] = pop();
			  push(4);
			  break;
			  
		case '^': while(st[top]>=4)
			  post[j++] = pop();
			  push(5);
			  break;
		
		case '(': push(0);
			  break;
			
		case ')': while(st[top]!=0)
			  post[j++] = pop();
			  top--;
			  break;
		default : post[j++] = inf[i];
	}
	}
	while(top>0)
	post[j++]=pop();
	cout<<"\nPostfix expression is => "<<post<<endl;
}

void EXP::push(int ele)
{
	top++;
	st[top]=ele;
}

char EXP::pop()
{
	int el;
	char e;
	el = st[top];
	top--;
	switch(el)
	{
		case 1: e = '+';
			break;
		case 2: e = '-';
			break;
		case 3: e = '*';
			break;
		case 4: e = '/';
			break;
		case 5: e = '^';
			break;
		
	}
	return(e);
}

int main(void)
{	
	EXP obj;
	char inf[40];
	//clrscr();
	cout<<"Enter the infix expression: ";
	cin>>inf;
	cout<<"The infix expression entered by you is..."<<inf;
	obj.postfix(inf);
	//getch();
	in
}
