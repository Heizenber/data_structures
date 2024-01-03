#include <iostream>
using namespace std;

struct Node
{
    int value;
    Node *next;
};

class CircularQueue
{
private:
    Node *tail;
    int size;

public:
    CircularQueue()
    {
        tail = NULL;
        size = 0;
    }

    bool isEmpty()
    {
        return size == 0;
    }

    int length()
    {
        return size;
    }

    void enqueue(int value)
    {
        Node *temp = new Node();
        temp->value = value;
        if (tail == NULL)
        {
            tail = temp;
            tail->next = tail;
        }
        else
        {
            temp->next = tail->next;
            tail->next = temp;
            tail = temp;
        }
        size++;
    }

    int dequeue()
    {
        if (tail == NULL)
            throw "Queue is empty";
        int value = tail->next->value;
        if (tail->next == tail)
        {
            delete tail;
            tail = NULL;
        }
        else
        {
            Node *temp = tail->next;
            tail->next = tail->next->next;
            delete temp;
        }
        size--;
        return value;
    }

    int first()
    {
        if (tail == NULL)
            throw "Queue is empty";
        return tail->next->value;
    }

    void rotate()
    {
        if (tail == NULL)
            throw "Queue is empty";
        tail = tail->next;
    }
};

int main()
{
    CircularQueue q;
    while (true)
    {
        int option, value;
        cout << "\nEnter:" 
                "\n1 to enqueue"
                "\n2 to dequeue"
                "\n3 to get first element"
                "\n4 to rotate"
                "\n5 to get length"
                "\n6 to check if empty"
                "\n0 to exit\n";
        cin >> option;
        switch (option)
        {
        case 1:
            cout << "Enter value: ";
            cin >> value;
            q.enqueue(value);
            break;
        case 2:
            cout << "Dequeued: " << q.dequeue() << endl;
            break;
        case 3:
            cout << "First element: " << q.first() << endl;
            break;
        case 4:
            q.rotate();
            break;
        case 5:
            cout << "Length: " << q.length() << endl;
            break;
        case 6:
            cout << "Empty: " << (q.isEmpty() ? "true" : "false") << endl;
            break;
        case 0:
            return 0;
        default:
            cout << "Invalid option\n";
        }


    }
    return 0;

}
