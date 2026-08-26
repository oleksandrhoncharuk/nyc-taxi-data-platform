{% macro generate_schema_name(custome_schema_name, node) -%}

    {%- if custome_schema_name is none or custome_schema_name | trim == '' -%}
        {{ target.schema }}
    {%- else -%}
        {{ custome_schema_name | trim }}
    {%- endif -%}

{%- endmacro %}