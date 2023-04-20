#include <iostream>
#define MAX 10
using namespace std;

struct queue
{       
	int data[MAX];
	int front,rear;
};

class Queue
{    
      struct queue q;
   public:
      Queue()
      {
      	q.front=q.rear=-1;
      }
      int isempty();
      int isfull();
      void enqueue(int);
      int delqueue();
      void display();
};

int Queue::isempty()
{
	if(q.front==q.rear)
		return 1;
	else
		return 0;
}

int Queue::isfull()
{   
	if(q.rear==MAX-1)
		return 1;
	else
		return 0;
}

void Queue::enqueue(int x)
{
	++q.rear;
	q.data[q.rear]=x;
}

int Queue::delqueue()
{
	int val=q.data[q.front];
	++q.front;
	return val;
}

void Queue::display()
{   int i;
    cout<<"\n";
    for(i=q.front+1;i<=q.rear;i++)
	     cout<<q.data[i]<<" ";
}

int main()
{      Queue obj;
	int ch,x;
	do{    cout<<"\n 1.Insert Job\n 2.Delete Job\n 3.Display\n 4.Exit\nEnter your choice : ";
	       cin>>ch;
	switch(ch)
	{  case 1: if (!obj.isfull())
		   {   
		   	cout<<"\nEnter data : \n";
			cin>>x;
			obj.enqueue(x);
			cout<<endl;
		   }
	          else
		      cout<< "Queue is overflow!!!\n\n";
	           break;
	   case 2: if(!obj.isempty())
			    cout<<"\nDeleted Element = "<<obj.delqueue()<<endl;
		    else
			{   cout<<"\nQueue is underflow!!!\n\n";  }
		    cout<<"\nRemaining Jobs : \n";
		    obj.display();
	           break;
	  case 3: if (!obj.isempty())
	        {  cout<<"\nQueue contains : \n";
		       obj.display();
	        }
	        else
		         cout<<"\nQueue is empty!\n\n";
	       break;
	  case 4: cout<<"\nExiting Program.....";
        }
      }while(ch!=4);
return 0;
}
