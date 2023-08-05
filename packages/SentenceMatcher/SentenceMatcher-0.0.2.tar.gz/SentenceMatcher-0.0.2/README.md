# SentenceMatcher
### A simple yet useful module that allows you to match a sentence against a list of sentences and return the closest match

<br>

Sample Code:
```python
from sentencematcher import SentenceMatch
list_of_sentences = ["Hey there!", "How're you?", "How's your day going?", "So tell me about yourself please!"]
sentence = "Please tell me about you."

output, accr = SentenceMatch(sentence, list_of_sentences)
print("Closest Match:", sentence)
print("Accuracy:", accr)
```

Output:
```
Closest Match: So tell me about yourself please!
Accuracy: 80.0
```

<br>

## Explanation
The module contains only one function: SentenceMatch(to_be_matched, list_to_match_against)
The first parameter is for the sentence that you want to match against a list of sentences, and the second parameter is for that list of sentences. The function returns 2 values, the output followed by the accuracy of the output.
Behind the scenes, the function matches the sentence against every sentence in the list of sentences and calculates a percentage (accuracy) value for each. It then returns the sentence with the highest accuracy and returns both the sentence and that accuracy.

HOWEVER:
Common symbols aren't taken into account, and the case of the letters isn't taken into account as well. It's better to avoid symbols anyways.

<br>
<h2 style="text-align:center">Mahdi Tajwar, 2023</h2>
<br><br>


# License
Copyright 2023 Mahdi Tajwar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.