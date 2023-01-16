#include <iostream>
#include <vector>
using namespace std;
#define FOR(i, n) for (int i = 0; i < n; i++)

void merge_sort(vector<int> &a){
    if (a.size() <= 1) return;
    int mid = a.size() / 2;
    // devide
    vector<int> left(a.begin(), a.begin() + mid);
    vector<int> right(a.begin() + mid, a.end());
    merge_sort(left);
    merge_sort(right);
    // conquer
    int i = 0, j = 0, k = 0;
    while (i < left.size() && j < right.size()){
        if (left[i] < right[j]){
            a[k++] = left[i++];
        }
        else{
            a[k++] = right[j++];
        }
    }
    while (i < left.size()){
        a[k++] = left[i++];
    }
    while (j < right.size()){
        a[k++] = right[j++];
    }
}

int main(){
    vector<int> a;
    // random input
    for (int i = 0; i < 10; i++){
        a.push_back(rand() % 100);
    }
    // print input
    for (int i = 0; i < a.size(); i++){
        cout << a[i] << " ";
    }
    cout << endl;
    // sort
    merge_sort(a);

    // print output
    for (int i = 0; i < a.size(); i++){
        cout << a[i] << " ";
    }
    cout << endl;

    // check if it sorted
    int t = a[0];
    for(int i = 1;i<10;i++){
        if(a[i] < t) {
            cout<<"Not sorted";
            break;
        }
        if(i == 9) cout<<"Sorted";
    }
}