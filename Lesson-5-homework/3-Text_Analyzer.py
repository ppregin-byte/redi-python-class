# Text Analyzer - Code Readability Exercise
def add_text():
   lines = []
   enter_count = 0
   print("Enter your text (press Enter twice to finish): ")
   while True:
      line = input()
      if line == '':
         enter_count += 1
         if enter_count == 2:
            break
      else:
         lines.append(line)
         enter_count = 0
   return "\n".join(lines)
# 1. **Basic Statistics:**
#    - Word count
def word_count(text):
   words = text.split()
   return len(words) 
#    - Character count (with and without spaces)
def char_count(text):
   char_spaces = len(text)
   char = len(text.replace(" ", "").replace("\n", ""))
   return char_spaces, char
#    - Sentence count
def sentence_count(text):
   sentences = text.replace("!", ".").replace("?", ".").replace("...",".").split(".")
   return len(sentences)
#    - Paragraph count
def paragraph_count(text):
   return text.count("\n") + 1
# 2. **Advanced Analysis:**
#    - Average words per sentence

def avg_words_sentence(text):
    sentences = text.replace("!", ".").replace("?", ".").replace("...",".").split(".") 
    count_word = []
    for sentence in sentences:
        sent = sentence.strip().split()
        if len(sent) > 0:
            count_word.append(len(sent))
    return sum(count_word) / len(count_word)

#    - Average word length
def avg_word_length(text):
   words = text.replace("!", "").replace("?", "").replace("...","").replace(":", "").replace(";", "").replace(",", "").split()
   words_dct = {word: len(word) for word in words}
   return sum(words_dct.values()) / len(words_dct)
#    - Reading difficulty estimate (based on average word length)
def reading_difficulty(text):
   words = text.replace(".", "").replace("!", "").replace("?", "").replace("...","").replace(":", "").replace(";", "").replace(",", "").split()    
   letters = [len(word) for word in words]
   count_easy = (letters.count(1) + letters.count(2) + letters.count(3))*100 / len(letters)    
   count_medium = (letters.count(4) + letters.count(5) + letters.count(6))*100 / len(letters)
   count_difficult = (len(letters) - count_easy - count_medium)*100 / len(letters)
   if count_easy >= 60: 
      return "Very easy"
   elif count_easy >= 50:
      return "Easy"       
   elif count_medium >= 50:
      return "Medium"
   elif count_medium >= 30:
      return "Above average"
   elif count_difficult >= 30:
      return "Difficult"      
   else:
      return "Very difficult"

#    - Text sentiment (simple positive/negative word counting)
def text_sentiment(text):
   positive = [
   "good", "great", "happy", "luck", "love", "excellent", "amazing", 
   "wonderful", "fantastic", "positive", "nice", "success", "joy", 
   "cheerful", "delight", "brilliant", "pleasure", "enjoy"
   ]

   negative = [
   "bad", "sad", "terrible", "awful", "horrible", "poor", "hate", 
   "angry", "upset", "negative", "fail", "pain", "disgust", "worse", 
   "boring", "unhappy", "problem", "depressing"
   ]
   words = text.lower().replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace(",", "").split()    
   pos = sum(1 for w in words if w in positive)
   neg = sum(1 for w in words if w in negative)
   if len(words) == 0:
      return "No words"
   pos_count = pos * 100 / len(words)
   neg_count = neg * 100 / len(words)
   if pos_count >= 20 and pos_count > neg_count: 
      return "positive", f"({pos_count:.1f}% positive words)"     
   elif neg_count >= 20 and neg_count > pos_count:
      return "negative", f"({neg_count:.1f}% negative words)"   
   else:
      return "neutral", f"({pos_count:.1f}% positive words, {neg_count:.1f}% negative words)"

#    - Most common words (top 5)
def common_words(text):
    words = text.lower().replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace(",", "").split()    
    words_dct = {word: words.count(word) for word in words}
    words_values = sorted(set(words_dct.values()), reverse=True)
    ind = 0
    top = 1
    words_top = {}
    while top <= 5 and ind < len(words_values):
        value = words_values[ind]
        keys = [k for k, v in words_dct.items() if v == value]
        for key in keys:
            if len(words_top) < 5:
                words_top[key] = value
        top += len(keys)
        ind += 1
    words_top_list = [(k, v) for k, v in words_top.items()]
    return(words_top_list)

#    - summary
def summary_text(reading, sentiment):
    tone = sentiment[0]
    if tone == "positive":
        return f"Your text is {reading.lower()} to read and has a positive tone."
    elif tone == "negative":
        return f"Your text is {reading.lower()} to read but has a negative tone."
    else:
        return f"Your text is {reading.lower()} to read with a neutral tone."
    
def print_report(text, total_words, char, sentences, paragraphs, average_setence, average_word, reading, sentiment, top_words, summary):
   print("\nTEXT ANALYSIS REPORT")
   print("="*20)
   print("\nBASIC STATISTICS:")
   print(f"- Total words: {total_words}")
   print(f"- Characters (with spaces): {char[0]}")
   print(f"- Characters (without spaces): {char[1]}")
   print(f"- Sentences: {sentences}")
   print(f"- Paragraphs: {paragraphs}")
   print("\nADVANCED ANALYSIS:")
   print(f"- Average words per sentence: {average_setence:.1f}")
   print(f"- Average word length: {average_word:.1f} characters")
   print(f"- Reading difficulty: {reading}")
   print(f"- Text sentiment: {sentiment[0]} {sentiment[1]}")
   print("\nMOST COMMON WORDS:")
   top = 1
   for word, count in top_words:
      print(f"{top}. '{word}' ({count} times)")
      top += 1
   print("\nSUMMARY:")
   print(summary)
   
def main():
   text = add_text()
   total_words = word_count(text)
   char = char_count(text)
   sentences = sentence_count(text)
   paragraphs = paragraph_count(text)
   average_setence = avg_words_sentence(text)
   average_word = avg_word_length(text)
   reading = reading_difficulty(text)
   sentiment = text_sentiment(text)
   top_words = common_words(text)
   summary = summary_text(reading, sentiment)
   print_report(text, total_words, char, sentences, paragraphs, average_setence, average_word, reading, sentiment, top_words, summary)

main()