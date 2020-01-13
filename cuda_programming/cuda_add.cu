#include <iostream>
#include <math.h>

__global__
void add(unsigned long long int n,  float *x, float *y)
{
	int index = threadIdx.x;
	int stride = blockDim.x;
	for(unsigned long long int i = index; i<n; i+= stride)
		y[i]  = x[i]+ y[i];
}


int main(void)
{
		


	unsigned long long int N= 1<<29;
	float *x ,  *y;
	cudaMallocManaged(&x, N*sizeof(float));
	cudaMallocManaged(&y, N*sizeof(float));

	for(unsigned long long int i = 0; i<N; i++)
	{
		x[i] = 1.0f;
		y[i] = 2.0f;

	}

	add<<<1, 256>>>(N, x, y);

	cudaDeviceSynchronize();

	cudaFree(x);
	cudaFree(y);
	return 0;
}
