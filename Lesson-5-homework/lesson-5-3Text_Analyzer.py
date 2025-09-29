# Text Analyzer - Code Readability Exercise

## Problem
You need to build a text analyzer that processes articles or documents and provides detailed statistics. 
This is a perfect example of how functions can transform a long, complex program into something readable and maintainable.

## Requirements
The program should analyze text and provide:

1. **Basic Statistics:**
   - Word count
   - Character count (with and without spaces)
   - Sentence count
   - Paragraph count

2. **Advanced Analysis:**
   - Average words per sentence
   - Most common words (top 5)
   - Reading difficulty estimate (based on average word length)
   - Text sentiment (simple positive/negative word counting)

3. **Formatted Report:**
   - Clean, professional output
   - Percentage breakdowns
   - Easy-to-read summary

## Expected Behavior
```
Text Analyzer
=============

Enter your text (press Enter twice to finish):
This is a sample text for analysis. It contains multiple sentences and various words. 
Some words are repeated to test the frequency analysis. This tool helps writers 
understand their writing style and improve readability.

TEXT ANALYSIS REPORT
====================

BASIC STATISTICS:
- Total words: 32
- Characters (with spaces): 159
- Characters (without spaces): 127
- Sentences: 3
- Paragraphs: 1

ADVANCED ANALYSIS:
- Average words per sentence: 10.7
- Average word length: 4.0 characters
- Reading difficulty: Easy
- Text sentiment: Positive (60% positive words)

MOST COMMON WORDS:
1. "and" (3 times)
2. "text" (2 times)
3. "analysis" (2 times)
4. "words" (2 times)
5. "writing" (2 times)

SUMMARY:
Your text is easy to read with a positive tone. Consider varying sentence length for better flow.
```

## The Challenge
This exercise demonstrates how a program that could be 100+ lines of messy code becomes clean and readable when broken into focused functions. 
Each function should have a single, clear purpose.