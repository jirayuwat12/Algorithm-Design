// selection sort

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>


using namespace std;
// selection sort function with time and swap count
void selection_sort(vector<int> &v, int &swap_count, int &time_count){
    int n = v.size();
    for(int i = 0; i < n; i++){
        int min_index = i;
        for(int j = i + 1; j < n; j++){
            if(++time_count &&  v[j] < v[min_index] ){
                min_index = j;
            }
        }
        swap(v[i], v[min_index]);
        swap_count++;
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

    selection_sort(v, swap_count, time_count);

    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << v[i] << " ";
    }
    cout << endl;
    cout << "Number of swaps: " << swap_count << endl;
    cout << "Number of comparisons: " << time_count << endl;
}