#include <iostream>
using namespace std;


struct Node {
    int data;
    Node *left, *right;
};

Node* GetNewNode(int data);
Node** Insert(Node** root, int data);
bool Search(Node* root, int data);
void printTree(Node* root);

int main() {
    Node* root = NULL;
    Insert(&root, 15);
    Insert(&root, 10);
    Insert(&root, 20);
    Insert(&root, 25);
    Insert(&root, 8);
    Insert(&root, 12);
    printTree(root);

    while (true) {
        int number;
        cout << "\nEnter number to be searched: ";
        cin >> number;
        if (Search(root, number)) cout << "Found\n";
        else cout << "Not Found\n";
        cout << "Enter 1 to continue, 0 to exit: ";
        cin >> number;
        if (number == 0) break;
    }
    return 0;
}

Node* GetNewNode(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node** Insert(Node** root, int data) {
    if (*root == NULL) {
        *root = GetNewNode(data);
    } else if (data <= (*root)->data) {
        (*root)->left = *Insert(&(*root)->left, data);
    } else {
        (*root)->right = *Insert(&(*root)->right, data);
    }
    return root;
}


void printTree(Node* root) {
    if (root == NULL) return;
    printTree(root->left);
    cout << root->data << " ";
    printTree(root->right);
}

bool Search(Node* root, int data) {
    if (root == NULL) return false;
    else if (root->data == data) return true;
    else if (data <= root->data) return Search(root->left, data);
    else return Search(root->right, data);
}