# coding=utf-8

cdef extern from "fun.c":
    double pi_fun(int n)
    int flb_fun(int n)

cpdef double pi(int n):
    return pi_fun(n)


cpdef int flb( int n):
    return flb_fun(n)
