#include<stdio.h>
#include<stdlib.h>
#define Num 20

int data[Num] = {0};
int BinaryTree[Num] = {0};

void CreatBinaryTree(int data[], int n){
    int node = 1,i;
    for(i = 0; i < Num; i++){
        BinaryTree[i] = 0;
    }
    for(i = 0; i < n; i++){
        BinaryTree[node] = data[i];
        node = node + 1;
    }
}

void Preorder(int node){
    if(BinaryTree[node] != 0){
        if(BinaryTree[node] != 0){
            printf("%d ", BinaryTree[node]);
        }
        Preorder(2*node);
        Preorder(2*node + 1);
    }
}

int main(){
    int i, n;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf(" %d", &data[i]);
    }
    CreatBinaryTree(data, n);
    Preorder(1);

    return 0;
}