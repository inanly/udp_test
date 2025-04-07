#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int n, m;
vector<pair<int, int>> ants, holes;
vector<vector<int>> edges;
vector<bool> visited;
vector<int> match;

int manhattan(pair<int, int> a, pair<int, int> b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

bool dfs(int u) {
    for (int v : edges[u]) {
        if (visited[v]) continue;
        visited[v] = true;
        if (match[v] == -1 || dfs(match[v])) {
            match[v] = u;
            return true;
        }
    }
    return false;
}

bool is_ok(int D) {
    edges.assign(n, vector<int>());
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (manhattan(ants[i], holes[j]) <= D)
                edges[i].push_back(j);

    match.assign(m, -1);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        visited.assign(m, false);
        if (dfs(i)) cnt++;
    }
    return cnt >= min(n, m);
}

int main() {
    cin >> n >> m;
    ants.resize(n);
    holes.resize(m);
    for (int i = 0; i < n; i++) cin >> ants[i].first >> ants[i].second;
    for (int i = 0; i < m; i++) cin >> holes[i].first >> holes[i].second;

    //binary search
    int left = 0, right = 220000, best = -1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (is_ok(mid)) {
            best = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    //run again
    is_ok(best);
    vector<int> result(n, -1);
    for (int j = 0; j < m; j++) {
        if (match[j] != -1) {
            result[match[j]] = j;
        }
    }

    for (int i = 0; i < n; i++) {
        if (result[i] != -1) {
            cout << i + 1 << " " << result[i] + 1 << endl;
        }
    }

    return 0;
}