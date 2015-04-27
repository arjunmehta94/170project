#include <stdio.h>
#include <string.h>
#include <algorithm>
int main() {
    int T = 1; // number of test cases
    FILE * fout = fopen ("answer.out", "w");
    for (int t = 1; t <= T; t++) {
        char filename[10];
        sprintf (filename, "%d.in", t);
        FILE * fin = fopen(filename, "r");

        int N;
        fscanf(fin, "%d", &N);

        int d[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                fscanf(fin, "%d", *(d + i) + j);
            }
        }

        char c[N];
        fscanf(fin, "%s", &c);

        // find an answer here, and put into assign
        int assign[N];
        for (int i = 0; i < N; i++) {
            assign[i] = i+1;
        }

        fprintf(fout, "%d", assign[0]);
        for (int i = 1; i < N ;i++)
            fprintf(fout, " %d", assign[i]);
        fprintf(fout, "\n");
    }
    fclose(fout);
    return 0;
}