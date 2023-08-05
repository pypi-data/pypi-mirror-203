# I18n texts loader

Use `pip install i-texts`

- Requires `LOCALE` and `LOCALES_PATH` (default: `./locales`) environment variables.
- Loads texts from "{`LOCALES_PATH`}/{`LOCALE`}.yml"

## Example

```py
from i_texts import texts

assert texts.dict == {1: "1", "a": "a", "words": "a b c", "ru": "русский"}
assert texts[1] == "1"
assert texts["a"] == "a"
assert texts.get_words("words") == ["a", "b", "c"]
```
