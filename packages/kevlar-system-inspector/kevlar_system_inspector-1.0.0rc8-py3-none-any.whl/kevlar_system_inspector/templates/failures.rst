=======
Details
=======

{% for module in report.modules.values() %}

.. class:: test-category {{ module.tags | join(" ") }}

{%      if module.documentation is not none %}
{{ module.documentation }}
{%      else %}
-------------------------------------------------
Undocumented module: {{ module.module.__name__ }}
-------------------------------------------------
{%      endif %}

{%      for nodeid, failure in module.failures.items() %}

.. class:: test-item {{ failure.tags | join(" ") }}

{%          if failure.documentation is none %}
Undocumented test: {{ nodeid }}
===============================

**Missing documentation**
{%           else %}
{{ failure.documentation }}
{%           endif %}

Issues Identified
-----------------

{%          for cause in failure.causes %}
.. admonition:: {{ "Issue" if not cause.is_internal else "Internal Error" }}
   :class: test-issue

{{              cause.message | indent(width=3, first=true) }}
{%          endfor %}

{%      endfor %}
{% endfor %}
