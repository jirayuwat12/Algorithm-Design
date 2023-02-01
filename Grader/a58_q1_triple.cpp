#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool findTriplet(vector<int> l, int target) {
    for (int i = 0; i < l.size() - 1; i++) {
        int second = i + 1;
        int third = l.size() - 1;
        while (second < third) {
            int sum = l[i] + l[second] + l[third];
            if (sum == target) {
                return true;
            }
            else if (sum < target) {
                second++;
            }
            else {
                third--;
            }
        }
    }
    return false;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> l(n);
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }

    vector<int> targets(m);
    for (int i = 0; i < m; i++) {
        cin >> targets[i];
    }

    int min_sum = l[0] + l[1] + l[2];
    int max_sum = l[n - 1] + l[n - 2] + l[n - 3];

    for (int target : targets) {
        if (target < min_sum || target > max_sum) {
            cout << "NO" << endl;
            continue;
        }
        if (findTriplet(l, target)) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
