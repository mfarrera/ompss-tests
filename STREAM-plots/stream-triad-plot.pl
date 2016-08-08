set style line 1 linecolor rgbcolor "#000000"
set style line 2 linetype -1 pointtype 5 linewidth 6
set style line 3 linetype 1 pointtype 9 linewidth 6 linecolor rgbcolor "#FFAA00"
set style line 4 linetype 18 pointtype 7 linewidth 6 linecolor rgbcolor "#AA00AA"
set style line 5 linetype 1 pointtype 13 linewidth 6 linecolor rgbcolor "#1188DD"
set style line 6 linetype 7 pointtype 5 linewidth 6 linecolor rgbcolor "#33FF33"
set style line 7 linetype 2 pointtype 13 linewidth 6 linecolor rgbcolor "#FFAA00"
#set key bottom right
set key top left
#set key outside center bottom
#set key outside center bottom box
#set key top left boxi

#set term postscript enhanced eps color size 12 cm, 9 cm font "Helvetica" 26
#set output "test.eps"


#set terminal pdf
#set output "latency-darwin.pdf"

set title "STREAM Triad performance (in MN)"
set xrange [524288:134217728]
##set yrange [0:256]
##set logscale
set log x
set xlabel "Block Size (in bytes)"
set ylabel "Memory Throughput (MB/s)"
##iset xtics ("100^{2}" 10, "160^{2}" 20, "200^{2}" 30, "320^{2}" 40, "400^{2}" 50)
##set ytics 20 
plot "stream-results-ompss.txt" using 2:3 with lines title "OmpSS",\
     "stream-results-serial.txt" using 2 with lines title "Serial"
