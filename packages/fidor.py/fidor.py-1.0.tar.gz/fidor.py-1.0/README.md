# fidor
A generator for random words, sentences and paragraphs.

## Installation
```
pip3 install fidor
```
or
```
pip install fidor
```

## Example
```py
import fidor

print(fidor.generate_word())
# pudirik (wtf is this lmao)

print(fidor.generate_sentence(sentence_len=6)) 
# Diper, neducok fulitul yepiz eladu litoyi. (tottaly right 👍)

print(fidor.generate_paragraph(paragraph_len=1))
# Fidor tenaha, vas hadu ilah. Muhek habam kede... (agreed)
```