PROGRAM=stream_triad

TARGETS=$(PROGRAM)-p $(PROGRAM)-i $(PROGRAM)-d
TARGETS=$(PROGRAM)-8 $(PROGRAM)-16 $(PROGRAM)-32  $(PROGRAM)-64 $(PROGRAM)-128 $(PROGRAM)-256 $(PROGRAM)-512 $(PROGRAM)-1024 $(PROGRAM)-2048

BASE_DIR=../ompss-ee/
include $(BASE_DIR)/common-files/Makefile

CC = mcc

CFLAGS = --ompss 
CFLAGS_P =
CFLAGS_I = --instrument
CFLAGS_D = --debug

LIBS  = 
INCS  = 

EXTRA = -std=c99 -O3 -Wall -Wno-unused -mcmodel=large 

$(PROGRAM)-p: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-128: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=128 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-64: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=64 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-32: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=32 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-16: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=16 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-8: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=8 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-256: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=256 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-512: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=512 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-1024: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=1024 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-2048: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) -DNCHUNKS=2048 $(CFLAGS_P) $(EXTRA) $(INCS) -o $@ $< $(LIBS)


$(PROGRAM)-i: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) $(CFLAGS_I) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

$(PROGRAM)-d: $(PROGRAM).c
	$(CC) $(GFLAGS) $(CFLAGS) $(CFLAGS_D) $(EXTRA) $(INCS) -o $@ $< $(LIBS)

clean:
	rm -f $(CC)_* *.o *~ $(TARGETS) 

