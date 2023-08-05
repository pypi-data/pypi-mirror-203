# A decorator that compiles C/C++ functions with Clang in Python

#### Like Numba, but Jerry-built and pre-alpha :) 

## pip install cooodecooo

#### Tested against Windows 10 / Python 3.10 / Anaconda


### Here are 2 examples:


#### Find RGB colors 


```python
import cv2
import numpy as np
from cooodecooo import ccoo

# The name of the variable needs to be `clangpath`, if you change it, it won't work
clangpath = r"C:\Program Files\LLVM\bin\clang.exe"

# The names of the 2 functions (Python / C) need to be equal (colorsearch2 - colorsearch2)
@ccoo
def colorsearch2(**kwargs): # put here always **kwargs
    # The variable that contains the C source code must be named - c_source_code -
    c_source_code = r"""
    __declspec(dllexport) void colorsearch2(unsigned char *pic, unsigned char *colors, int width, int totallengthpic, int totallengthcolor, int *outputx, int *outputy, int *lastresult) {
        int counter = 0;
        for (int i = 0; i <= totallengthcolor; i += 3) {
            int r = i;
            int g = i + 1;
            int b = i + 2;
            for (int j = 0; j <= totallengthpic; j += 3) {
                if ((colors[r] == pic[j]) && (colors[g] == pic[j + 1]) && (colors[b] == pic[j + 2])) {
                    int dividend = j / 3;
                    int quotient = dividend / width;
                    int remainder = dividend % width;
                    int upcounter = counter;
                    outputx[upcounter] = quotient;
                    outputy[upcounter] = remainder;
                    lastresult[0] = upcounter;
                    counter++;
                }
            }
        }
    }
    """
    # Where do you want to save the shared library? The name of the variable cannot be changed! It needs to be - c_save_path -
    c_save_path = "cloop.so"
	# That's it, no return value! Scroll down for more details.

def get_pixelcolor(pic, colors):
    totallenghtpic = (pic.shape[0] * pic.shape[1] * pic.shape[2]) - 1
    totallengthcolor = (colors.shape[0] * colors.shape[1]) - 1
    outputx = np.zeros(totallenghtpic, dtype=np.int32)
    outputy = np.zeros(totallenghtpic, dtype=np.int32)
    lastresult = np.zeros(1, dtype=np.int32)

    # Use the same signature as in the C function # unsigned char *pic, unsigned char *colors, int width, int totallengthpic, int totallengthcolor, int *outputx, int *outputy, int *lastresult
    # Pointers only work when numpy arrays are passed to the function
    varstopass = {
        "pic": pic,
        "colors": colors,
        "width": pic.shape[1],
        "totallengthpic": totallenghtpic,
        "totallengthcolor": totallengthcolor,
        "outputx": outputx,
        "outputy": outputy,
        "lastresult": lastresult,
    }

    # The compiled function doesn't return anything, it writes the results in  given numpy arrays by using pointers
    # In this example: outputx/outputy/lastresult
    _ = colorsearch2(**varstopass)
    return np.dstack([outputx[: lastresult[0] + 1], outputy[: lastresult[0] + 1]])[0]


picx = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
pic = cv2.imread(picx)
colors = np.array(
    [
        (66, 71, 69),
        (62, 67, 65),
        (144, 155, 153),
        (52, 57, 55),
        (127, 138, 136),
        (53, 58, 56),
        (51, 56, 54),
        (32, 27, 18),
        (24, 17, 8),
    ],
    dtype=np.uint8,
)
resu = get_pixelcolor(pic, colors)



```




### Levenshtein Distance


```python
import numpy as np
from cooodecooo import ccoo

clangpath = r"C:\Program Files\LLVM\bin\clang.exe"


@ccoo
def levenshtein_distance(**kwargs):
    c_source_code = r"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minim(int a, int b, int c)
{
    int m = a;
    if (b < m)
        m = b;
    if (c < m)
        m = c;
    return m;
}

__declspec(dllexport) void levenshtein_distance(char *s1, char *s2, int len1, int len2, int *resultsx)
{
    //printf("%d %d\n", len1, len2);
    int *d = (int *)malloc((len1 + 1) * (len2 + 1) * sizeof(int));
    int i, j;

    for (i = 0; i <= len1; i++)
        d[i * (len2 + 1) + 0] = i;

    for (j = 0; j <= len2; j++)
        d[0 * (len2 + 1) + j] = j;

    for (i = 1; i <= len1; i++)
    {
        for (j = 1; j <= len2; j++)
        {
            //printf("%c %c\n", s1[i - 1], s2[j - 1]);
            //fflush(stdout);
            int cost = (s1[i - 1] == s2[j - 1]) ? 0 : 1;
            d[i * (len2 + 1) + j] = minim((d[(i - 1) * (len2 + 1) + j] + 1),
                                          (d[i * (len2 + 1) + (j - 1)] + 1),
                                          (d[(i - 1) * (len2 + 1) + (j - 1)] + cost));
        }
    }

    resultsx[0] = d[len1 * (len2 + 1) + len2];
    printf("%d\n", resultsx[0]);
    free(d);
}
    """
    c_save_path = "levete.so"


s01 = ("kitten").encode()
s02 = ("sitting").encode()
s1 = np.array(list(s01), dtype=np.uint8)
s2 = np.array(list(s02), dtype=np.uint8)
len1 = len(s1)
len2 = len(s2)
resultsx = np.array([0], dtype=np.int32)
_ = levenshtein_distance(s1=s1, s2=s2, len1=len1, len2=len2, resultsx=resultsx)
print(resultsx)
```