#include <iostream>
#include <math.h>

__global__
void add(int n, float *x, float *y)
{
	for(int i = 0; i<n; i++)
		y[i]  = x[i]+ y[i];
}


int main(void)
{
		auto start = high_resolution_clock::now();


	int N= 1<<20;
	float *x , float *y;
	cudaMallocManaged(&x, N*sizeof(float));
	cudaMallocManaged(&y, N*sizeof(float));

	for(int i = 0; i<N; i++)
	{
		x[i] = 1.0f;
		y[i] = 2.0f;

	}

	add<<<1, 1>>>(N, x, y);

	cudaDeviceSynchronize();

	cudaFree(x);
	cudaFree(y);
	return 0;
}
