#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *left, *right;
};

Node *GetNewNode(int data);
Node **Insert(Node **root, int data);
bool Search(Node *root, int data);
void printTree(Node *root);

class BinarySearchTree
{
private:
    Node *root;

public:
    BinarySearchTree()
    {
        root = NULL;
    }
    void Insert(int data)
    {
        if (root == NULL)
        {
            root = GetNewNode(data);
        }
        else if (data <= root->data) {

        }
    }

    Node *GetNewNode(int data)
    {
        Node *newNode = new Node();
        newNode->data = data;
        newNode->left = newNode->right = NULL;
        return newNode;
    }

    void printTree(Node *root)
    {
        if (root == NULL)
            return;
        printTree(root->left);
        cout << root->data << " ";
        printTree(root->right);
    }

    bool Search(Node *root, int data)
    {
        if (root == NULL)
            return false;
        else if (root->data == data)
            return true;
        else if (data <= root->data)
            return Search(root->left, data);
        else
            return Search(root->right, data);
    }
};

int main()
{
    Node *root = NULL;
    Insert(&root, 15);
    Insert(&root, 10);
    Insert(&root, 20);
    Insert(&root, 25);
    Insert(&root, 8);
    Insert(&root, 12);
    depthInOrderTraversal(root);

    while (true)
    {
        int number;
        cout << "\nEnter number to be searched: ";
        cin >> number;
        if (Search(root, number))
            cout << "Found\n";
        else
            cout << "Not Found\n";
        cout << "Enter 1 to continue, 0 to exit: ";
        cin >> number;
        if (number == 0)
            break;
    }
    return 0;
}

Node *GetNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node **Insert(Node **root, int data)
{
    if (*root == NULL)
    {
        *root = GetNewNode(data);
    }
    else if (data <= (*root)->data)
    {
        (*root)->left = *Insert(&(*root)->left, data);
    }
    else
    {
        (*root)->right = *Insert(&(*root)->right, data);
    }
    return root;
}

void depthInOrderTraversal(Node *root)
{
    if (root == NULL)
        return;
    printTree(root->left);
    cout << root->data << " ";
    printTree(root->right);
}

bool Search(Node *root, int data)
{
    if (root == NULL)
        return false;
    else if (root->data == data)
        return true;
    else if (data <= root->data)
        return Search(root->left, data);
    else
        return Search(root->right, data);
}

int findMin(Node *root)
{
    if (root == NULL)
        throw "Tree is empty";
    else if (root->left == NULL)
        return root->data;
    return findMin(root->left);
}

int findMax(Node *root)
{
    if (root == NULL)
        throw "Tree is empty";
    else if (root->right == NULL)
        return root->data;
    return findMax(root->right);
}

int findHeight(Node *root)
{
    if (root == NULL)
        return -1;
    return max(findHeight(root->left), findHeight(root->right)) + 1;
}