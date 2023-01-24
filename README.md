# Numeronymizer

A simple library to generate numeronyms.

## Example

### input
```
The utilization of this library can significantly enhance the accessibility of written content by abbreviating lengthy words. By reducing the number of characters in words such as internationalization, the overall readability and understandability of the text improves. Furthermore, it can also aid in reducing the amount of space required to display the text, which can be beneficial in digital contexts such as on websites or mobile devices.
```

### output
```
The u9n of this library can s11y enhance the a11y of written content by a10g lengthy words. By reducing the number of c8s in words such as i18n, the overall r9y and u15y of the text improves. F9e, it can also aid in reducing the amount of space required to display the text, which can be b8l in digital contexts such as on websites or mobile devices.
```

## Installation
```bash
pip install numeronymizer
```

## Usage
```python
from numeronymizer import numeronymize

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

numeronymized_text = numeronymize(text)
print(numeronymized_text)
# "Lorem ipsum dolor sit amet, c9r a8g elit, sed do eiusmod tempor i8t ut labore et dolore magna aliqua."

numeronymized_text = numeronymize(text, n=5)
print(numeronymized_text)
# "L3m i3m d3r sit amet, c9r a8g elit, sed do e5d t4r i8t ut l4e et d3re m3a a4a."
```

For example, you can use the following code to read a text file named `my_text.txt`, and replace its text. Additionally, you can also save the shortened text to another text file of your choice.

```python
from numeronymizer import numeronymize

with open("my_text.txt", "r", encoding='utf-8') as file:
    text = file.read()

numeronymized_text = numeronymize(text, n=10)
print(numeronymized_text)

with open("numeronymized.txt", "w", encoding='utf-8') as file:
    file.write(numeronymized_text)
```

## Function

```python
numeronymize(text:str, n:int=10)->str:
    """
    Numeronymize the words in text.
    :param text: input text.
    :param n: the number of characters (default value is 10).
    :return: replaced text.
    """
```
The function takes two arguments, the text you want to shorten and the number of characters, and returns the replaced text. The default number of characters is 10.

## License

This project is licensed under the 0BSD License.