bool IsSubtreeLesser(Node* root, int value);
bool isSubtreeGreater(Node* root, int value);
bool IsBinarySearchTree(Node* root);




bool IsSubtreeLesser(Node* root, int value) {
    if (root == NULL) return true;
    if (root->data <= value
        && IsSubtreeLesser(root->left, value)
        && IsSubtreeLesser(root->right, value))
        return true;
    else
        return false;
}

bool IsSubtreeGreater(Node* root, int value) {
    if (root == NULL) return true;
    if (root->data > value
        && isSubtreeGreater(root->left, value)
        && isSubtreeGreater(root->right, value))
        return true;
    else
        return false;
}


bool IsBinarySearchTree(Node* root, int minValue, int maxValue) {
    if (root->data > minValue
        && root->data < maxValue
        && IsBinarySearchTree(root->left, minValue, root->data)
        && IsBinarySearchTree(root->right, root->data, maxValue))
        return true;
    else
        return false;
}