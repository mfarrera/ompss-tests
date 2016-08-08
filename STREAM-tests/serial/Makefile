CC = gcc
CFLAGS = -O3 -std=c99 -O3 -Wall -Wno-unused -mcmodel=large 

FF = g77
FFLAGS = -O2

all: stream_c.exe stream_t.exe stream_omp

stream_t.exe: stream_triad.c
	$(CC) $(CFLAGS) stream_triad.c -o stream_t.exe
stream_c.exe: stream.c
	$(CC) $(CFLAGS) stream.c -o stream_c.exe
stream_omp: stream_triad.c
	$(CC) $(CFLAGS) -fopenmp stream_triad.c -o stream_omp

clean:
	rm -f stream_c.exe stream_t.exe stream_omp *.o

# an example of a more complex build line for the Intel icc compiler
stream.icc: stream.c
	icc -O3 -xCORE-AVX2 -ffreestanding -qopenmp -DSTREAM_ARRAY_SIZE=80000000 -DNTIMES=20 stream.c -o stream.omp.AVX2.80M.20x.icc
