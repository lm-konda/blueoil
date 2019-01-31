/* Copyright 2018 The Blueoil Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef DLK_FUNC_BATCH_NORMALIZATION_H_INCLUDED
#define DLK_FUNC_BATCH_NORMALIZATION_H_INCLUDED

#include "time_measurement.h"
#include "global.h"

void func_BatchNormalization(T_FLOAT input[], T_FLOAT gamma[], T_FLOAT beta[], T_FLOAT mean[], T_FLOAT variance[], T_FLOAT epsilon, T_FLOAT output[], T_UINT out_height, T_UINT out_width, T_UINT out_depth);

void func_BatchNormalization(T_FLOAT input[], T_FLOAT scale[], T_FLOAT shift[], T_FLOAT output[], T_UINT out_height, T_UINT out_width, T_UINT out_depth) {
  Measurement::Start("BatchNorm");
  
  T_UINT index = 0;
  for (T_UINT f = 0; f < out_height * out_width; f++) {
    for (T_UINT d = 0; d < out_depth; d++) {
      output[index] = input[index] * scale[d] + shift[d];
      index++;
    }
  }
  Measurement::Stop();
}

#endif // DLK_FUNC_BATCH_NORMALIZATION_H_INCLUDED
