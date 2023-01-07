//heap sort
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// heapify function aka fix heap
void heapify(vector<int> &v, int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && v[l] > v[largest])
        largest = l;

    if (r < n && v[r] > v[largest])
        largest = r;

    if (largest != i)
    {
        swap(v[i], v[largest]);
        heapify(v, n, largest);
    }
}

void heapSort(vector<int> &v, int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        // fix heap from bottom to top
        heapify(v, n, i);

    for (int i = n - 1; i >= 0; i--)
    {
        swap(v[0], v[i]);
        // fix heap from top to bottom
        heapify(v, i, 0);
    }
}

int main()
{
    vector<int> v = {12, 11, 13, 5, 6, 7};
    int n = v.size();

    heapSort(v, n);

    cout << "Sorted array is \n";
    for (int i = 0; i < n; ++i)
        cout << v[i] << " ";
    cout << endl;
}