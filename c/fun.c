#include "stdio.h"
#include "math.h"

static double pi_fun(int n){
	double s = 0.0;
	for (int i = 0; i < n+1; ++i)
	{
		s += 1.0/(2*i+1)/(2*i+1);
	}
	return sqrt(8*s);
}

static int flb_fun(int n){
	if (n == 0){
		return 0;
	}
	if (n == 1){
		return 1;
	}
	return flb_fun(n-1)+flb_fun(n-2);
}