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

#include "global.h"
#include "inputs/{{ node.name }}.h"

{% if node.is_scalar -%}

{{ node.dtype.cpptype() }} {{ node.name }} = {{ node.data[0] }};

{% else -%}

{{ node.dtype.cpptype() }} {{ node.name }}[] = {
  {% for d in node.data.flatten() -%}
  {{- d -}},
  {%- endfor %}
};

{% if node.scale_data %}
{{ node.dtype.cpptype() }} {{ node.name }}_scale[] = {
  {% for d in node.scale_data -%}
  {{- d -}},
  {%- endfor %}
};
{% endif %}

{% if node.shift_data %}
{{ node.dtype.cpptype() }} {{ node.name }}_shift[] = {
  {% for d in node.shift_data -%}
  {{- d -}},
  {%- endfor %}
};
{% endif %}

{%- endif %}
