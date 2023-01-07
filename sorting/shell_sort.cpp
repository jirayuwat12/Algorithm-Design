//shell sort
//shell sort is a variation of insertion sort
//key
// letting G = some large value less than N and 
// let split data into G sublists and sort each sublist using insertion sort
// then reduce G and repeat the process
// when G = 1, the whole array is sorted

// the key is to choose a good value for G
// the good one for G is 3*G + 1
// the worst value for G is 1
// the average value for G is 2^(k-1) - 1
// where k is the number of times we divide G by 2

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void insertion_sort(vector<int> &v, int start, int gap)
{
    for (int i = start + gap; i < v.size(); i += gap)
    {
        int j = i;
        while (j >= gap && v[j] < v[j - gap])
        {
            swap(v[j], v[j - gap]);
            j -= gap;
        }
    }
}

void shell_sort(vector<int> &v)
{
    int gap = v.size() / 2;
    while (gap > 0)
    {
        for (int i = 0; i < gap; ++i)
        {
            insertion_sort(v, i, gap);
        }
        gap /= 2;
    }
}

int main()
{
    vector<int> v = { 1, 3, 2, 5, 4, 7, 6, 9, 8, 10 };
    //show the original vector
    cout<<"original vector: ";
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << endl;

    shell_sort(v);
    cout<<"sorted vector: ";
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}