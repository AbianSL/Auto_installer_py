/**
  * @name PED
  * @version 1.0
  * @description calculate the proximity edit distance between two strings
  * @date 2024-04-07
  * @param {string} string_1 - the first string
  * @param {string} string_2 - the second string
  * @returns {number} the proximity edit distance between the two strings
  *
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <string.h> 

/**
  * @ name min
  * @ description return the minimum value between three values
  * @ param {unsigned int} val_1 - the first value
  * @ param {unsigned int} val_2 - the second value
  * @ param {unsigned int} val_3 - the third value
  * @ returns {unsigned int} the minimum value between the three values
  * @ example min(1, 2, 3) -> 1
*/
unsigned int min(unsigned int val_1, unsigned int val_2, unsigned int val_3) {
  unsigned int min_val = val_1;
  if (val_2 < min_val) {
    min_val = val_2;
  }
  if (val_3 < min_val) {
    min_val = val_3;
  }
  return min_val;
}

unsigned int min_row_matrix(unsigned int row_pos, unsigned int cols, unsigned int matrix[row_pos][cols]) {
  unsigned int min_val = matrix[row_pos][0]; 
  for (int i = 0; i < cols; ++i) {
    if (matrix[row_pos][i] < min_val) {
      min_val = matrix[row_pos][i];
    }
  } 
  return min_val;
}

/**
  * @ name ped
  * @ description calculate the proximity edit distance between two strings
  * @ param {char[]} string_1 - the first string, that should be the prefix of the second string
  * @ param {char[]} string_2 - the second string
  * @ returns {unsigned int} the proximity edit distance between the two strings
*/
unsigned int ped(char string_1[], char string_2[]) {
  unsigned int size_string_1 = strlen(string_1) + 1;
  unsigned int size_string_2 = strlen(string_2) + 1;
  unsigned int matrix[size_string_1][size_string_2];
  printf("%d %d\n", size_string_1, size_string_2); 
  printf("%s %s\n", string_1, string_2);
  for (int i = 0; i < size_string_1; ++i) {
    matrix[i][0] = i;
  }

  for (int j = 0; j < size_string_2; ++j) {
    matrix[0][j] = j;
  }
  
  for (int i = 1; i < size_string_1; ++i) {
    for (int j = 1; j < size_string_2; ++j) {
      int cost = 0;
      if (string_1[i - 1] != string_2[j - 1]) {
        cost = 1;
      }

      matrix[i][j] = min(matrix[i - 1][j] + 1, 
                         matrix[i][j - 1] + 1, 
                         matrix[i - 1][j - 1] + cost);
    }
  }

  for (int i = 0; i < size_string_1; ++i) {
    for (int j = 0; j < size_string_2; ++j) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }

  return min_row_matrix(size_string_1, size_string_2 - 1, matrix);
}

static PyObject* Cped(PyObject* self, PyObject* args) {
  const char* string_1;
  const char* string_2;
  
  if (!PyArg_ParseTuple(args, "ss", &string_1, &string_2)) {
    return NULL;
  }
  
  unsigned int result = ped(string_1, string_2);

  return Py_BuildValue("i", result);
}

