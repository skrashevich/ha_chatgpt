# ha_chatgpt

<!-- badges:start -->
[![GitHub stars](https://img.shields.io/github/stars/skrashevich/ha_chatgpt?style=flat-square)](https://github.com/skrashevich/ha_chatgpt/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/skrashevich/ha_chatgpt?style=flat-square)](https://github.com/skrashevich/ha_chatgpt/commits/main)
[![License](https://img.shields.io/github/license/skrashevich/ha_chatgpt?style=flat-square)](https://github.com/skrashevich/ha_chatgpt/blob/main/LICENSE)
<!-- badges:end -->

 ChatGPT Conversation for Home Assistant
## Installation

I recommend installing it through [HACS](https://github.com/hacs/integration)

### Installing via HACS

1. Go to HACS->Integrations
2. Add this repo into your HACS custom repositories
3. Search for ChatGPT and Download it
4. Restart your HomeAssistant
5. Go to Settings->Devices & Services
6. Shift reload your browser
7. Click Add Integration
8. Search for ChatGPT
9. Type your OpenAI API KEY and hit submit
10. Add
```yaml
conversation:
```
to configuration.yaml

11. You're all set

In some cases, you may need to remove the built-in OpenAI integration and restart the homemassistant twice
