#include <iostream>
#include <math.h>
#include <chrono>
#include <algorithm>
using namespace std;
using namespace std::chrono;

void add(int n, float *x, float *y)
{
	for(int i = 0; i<n; i++)
		y[i]  = x[i]+ y[i];
}


int main(void)
{
		auto start = high_resolution_clock::now();


	int N= 1<<20;
	float *x = new float[N];
	float *y = new float[N];

	for(int i = 0; i<N; i++)
	{
		x[i] = 1.0f;
		y[i] = 1.0f;

	}

	add(N, x, y);

	
	delete [] x;
	delete [] y;
	auto stop = high_resolution_clock::now();
		auto duration = duration_cast<microseconds>(stop - start);

	cout<<duration.count()<<endl;
	return 0;
}
