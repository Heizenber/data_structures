#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    node *next;
} node;

node *head = NULL;
node *tail = NULL;

int add_node() {
    node *newnode, *temp;
    newnode = (node *) malloc(sizeof(node));
    if (newnode == NULL) {
        printf("\n\n\t Unable to allocate memory");
        return -1;
    }
    printf("\n\n\t Enter the data into the linkedlist:  ");
    scanf("%d", &newnode->data);
    newnode->next = NULL;
    if (head == NULL) {
        head = newnode;
        tail = newnode;
        return 1;
    } else {
        tail->next = newnode;
        tail = newnode;
    }
}

void display() {
    if (head == NULL) {
        printf("\n\n\t List is empty");
        return;
    }
    node *ptr = head;
    while (ptr != NULL) {
        printf("\n\n\t %d", ptr->data);
        ptr = ptr->next;
    }
}

int main() {
    int ch;
    do {
        printf("\n\n\t 1.create linkedlist");
        printf("\n\n\t 2.Display linkedlist");
        printf("\n\n\t 3.exit linkedlist");
        printf("\n\n\t Enter your choice(1-3): ");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            add_node();
            break;

        case 2:
            display();
            break;
        case 3:
            exit(1);
            break;
        
        default:
            printf("\n\n\t Wrong entry: Please enter correct option only (1-3)");
            break;
        }
    } while (ch != 3);
}