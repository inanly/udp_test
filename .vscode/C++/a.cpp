#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> candidate = {1, 5, 10, 50};
vector<vector<int>> result;

void combinationSum(vector<int> &current, int start, int target)
{
    if (target == 0)
    {
        result.push_back(current);
        return;
    }
    for (int i = start; i < candidate.size(); i++)
    {
        if (candidate[i] > target)
            break;
        current.push_back(candidate[i]);
        combinationSum(current, i, target - candidate[i]);
        current.pop_back();
    }
}

int main()
{
    vector<int> current;
    int coin;
    cin >> coin;
    combinationSum(current, 0, coin);

    printf("$50\t$10\t$5\t$1\n");
    printf("--------------------------\n");

    for (int i = result.size() - 1; i >= 0; i--)
    {
        vector<int> count(4, 0);

        for (int j = 0; j < result[i].size(); j++)
        {
            for (int k = 0; k < candidate.size(); k++)
            {
                if (result[i][j] == candidate[k])
                    count[k]++;
            }
        }

        for (int j = count.size() - 1; j >= 0; j--)
        {
            printf("%d\t", count[j]);
        }
        printf("\n");
    }
    return 0;
}