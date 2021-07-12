---
title: Example Tutorial
description: This is an example tutorial to test the layout and syntax highlighting.
date: 2021-07-13T16:00:00.000+00:00
lang: en
duration: 7min
cover: https://cdn.analyticsvidhya.com/wp-content/uploads/2019/06/Screenshot-from-2019-06-17-19-53-10.png
---

## Python 🚀

### Creating an NLP community 🤗

Here is how you create a NLP community in Python:

```python
class NLPCommunity:
    def __init__(self, lang):
        self.lang = lang

nlp_en_es = NLPCommunity(lang="es")
```


### How to annoy your colleagues 😡

Change the value of the `2` integer object to `42`:


```python
>>> import ctypes
>>> ctypes.c_int.from_address(id(2) + 24).value = 42
>>> 2 == 42
True
>>> 1 + 1
42
>>> 2 * 2
1764
```

### The object-type relationship in Python 🤯

The `object` and `type` types have an interesting relationship.

```python
>>> isinstance(object, type)
True
>>> isinstance(type, object)
True
>>> isinstance(type, type)
True
>>> isinstance(object, object)
True
>>> issubclass(type, object)
True
>>> issubclass(object, type)
False
```

## Syntax highlighting in other languages

The syntax highlighting also works for other languages.

### Rust 🦀

```rust
fn main() {
    let mut vec = vec![1, 5, 10, 2, 15];
    
    vec.sort();

    assert_eq!(vec, vec![1, 2, 5, 10, 15]);
}
```


### Javascript 😭

```javascript
> typeof NaN
'number'
> [] + []
''
> [] + {}
'[object Object]'
> {} + []
0
> 9 + "1"
'91'
```
