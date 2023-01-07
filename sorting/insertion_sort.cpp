//insertion sort
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

void insertion_sort(vector<int> &v, int &swap_count, int &time_count){
    int n = v.size();
    for(int i = 1; i < n; i++){
        int key = v[i];
        int j = i - 1;
        while(++time_count && j >= 0 && v[j] > key){
            v[j + 1] = v[j];
            j--;
            swap_count++;
        }
        v[j + 1] = key;
    }
}

int main(){
    cout << "Enter the number of elements: ";
    int n;
    cin >> n;
    vector<int> v;
    if(n <= 0){
        //random  elements
        n = 20;
        for(int i = 0; i < n; i++){
            v.push_back(rand() % 100);
        }
    }else{
        cout << "Enter the elements: ";
        for(int i = 0; i < n; i++){
            int x;
            cin >> x;
            v.push_back(x);
        }
    }
    cout<< "size of vector: " << v.size() << endl;
    cout << "Unsorted array: ";
    for(int i = 0; i < n; i++){
        cout << v[i] << " ";
    }
    cout << endl;

    int swap_count = 0;
    int time_count = 0;

    insertion_sort(v, swap_count, time_count);

    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << v[i] << " ";
    }
    cout << endl;

    cout << "Time count: " << time_count << endl;
    cout << "Swap count: " << swap_count << endl;
    return 0;
}