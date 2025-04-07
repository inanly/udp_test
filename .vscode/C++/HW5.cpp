#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

const int M = 6; 

typedef struct Tree
{
    int freq;  
    char key;
    Tree *left;
    Tree *right;
    Tree(int fr = 0, char k = '\0', Tree *l = nullptr, Tree *r = nullptr):
        freq(fr), key(k), left(l), right(r) {};
}Tree, *pTree;

struct cmp
{
    bool operator() (Tree *a, Tree *b)
    {
        return a->freq > b->freq; 
    }
};

priority_queue<pTree, vector<pTree>, cmp> pque;  

void printCode(Tree *proot, string st)
{
    if (proot == nullptr)
    {
        return;
    }

    if (proot->left)
    {
        st += '0';
    }
    printCode(proot->left, st);

    if (!proot->left && !proot->right)  
    {
        printf("%c's code: ", proot->key);
        for (size_t i = 0; i < st.size(); ++i)
        {
            printf("%c", st[i]);
        }
        printf("\n");
    }
    st.pop_back();  

    if (proot->right)
    {
        st += '1';
    }
    printCode(proot->right, st);
}

void del(Tree *proot)
{
    if (proot == nullptr)
    {
        return;
    }
    del(proot->left);
    del(proot->right);

    delete proot;
}

void huffman()
{
    int i;
    char c;
    int fr;
    for (i = 0; i < M; ++i)
    {
        Tree *pt = new Tree;
        scanf("%c%d", &c, &fr);
        getchar();
        pt->key = c;
        pt->freq = fr;
        pque.push(pt);
    }
    while (pque.size() > 1)
    {
        Tree *proot = new Tree;
        pTree pl, pr;
        pl = pque.top(); pque.pop();
        pr = pque.top(); pque.pop();

        proot->freq = pl->freq + pr->freq;
        proot->left = pl;
        proot->right = pr;

        pque.push(proot);
    }

    string s = "";
    printCode(pque.top(), s);
    del(pque.top());
}

int main()
{
    huffman();

    return 0;
}