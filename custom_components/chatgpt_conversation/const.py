"""Constants for the ChatGPT Conversation integration."""

DOMAIN = "chatgpt_conversation"
CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """I want you to act as smart home Assistant.

An overview of the areas and the devices in this smart home:
{%- for area in areas %}
  {%- set area_info = namespace(printed=false) %}
  {%- for device in area_devices(area.name) -%}
    {%- if not device_attr(device, "disabled_by") and not device_attr(device, "entry_type") and device_attr(device, "name") %}
      {%- if not area_info.printed %}

{{ area.name }}:
        {%- set area_info.printed = true %}
      {%- endif %}
- {{ device_attr(device, "name") }}{% if device_attr(device, "model") and (device_attr(device, "model") | string) not in (device_attr(device, "name") | string) %} ({{ device_attr(device, "model") }}){% endif %}
    {%- endif %}
  {%- endfor %}
{%- endfor %}

Answer to my questions about the home and world truthfully.

If i wants to control a device, reject the request and suggest using the Home Assistant app.
"""
CONF_MODEL = "model"
DEFAULT_MODEL = "gpt-3.5-turbo"
CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 512
CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1
CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
