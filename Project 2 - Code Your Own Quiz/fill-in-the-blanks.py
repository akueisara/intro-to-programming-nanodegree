# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

blanks = ["___1___", "___2___", "___3___", "___4___"]

easy_quiz = '''___1___ is a high-level, interpreted, interactive and object-oriented ___2___ language. Its design philosophy emphasizes code readability, and its ___3___ allows programmers to express concepts in ___4___ lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale. Source: Wikipedia and Tutorialspoint''' 
medium_quiz = '''Python supports multiple programming ___1___, including object-oriented, imperative and ___2___ programming or procedural styles. It features a dynamic type system and automatic ___3___ management and has a large and comprehensive standard ___4___. Source: Wikipedia''' 
hard_quiz = '''Python interpreters are available for installation on many operating systems, allowing Python code execution on a wide variety of systems. Using third-party tools, such as ___1___ or ___2___, Python code can be ___3___ into stand-alone executable programs for some of the most popular operating systems, allowing the distribution of Python-based software for use on those environments without requiring the installation of a Python interpreter. ___4___, the reference implementation of Python, is free and open-source software and has a community-based development model, as do nearly all of its alternative implementations. Source: Wikipedia'''

easy_answers = ["Python", "programming", "syntax", "fewer"]
medium_answers = ["paradigms", "functional", "memory", "library"]
hard_answers = ["py2exe", "pyinstaller", "packaged", "CPython"]	

# Makes the player input their name and returns the player input
def get_name():
    name = raw_input("Please enter your name: ")
    if (name == ""):
        print "Name can't be empty.\n"
        get_name()
    else:
        print "Hello " + name + ", "
        return name

# Makes the player input the level of the quiz and returns the player input
def get_level():
    level = raw_input("Please select a difficulty level for your quiz (easy, medium, or hard): ")
    if level.lower() in ["easy", "medium", "hard"]:
        print "You chose " + level.lower() + "\n"
        return level.lower()
    else:
        print "You entered an invalid difficulty level.\n"
        get_level()

# Checks if a word in parts_of_speech is a substring of the word passed in.		
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Fills in the blank with the correct anwser of the quiz 	
def fill_in(quiz, blank, answer):
    quiz = quiz.split()
    replaced = []
    for word in quiz:
        if (word == blank):
            word = word.replace(blank, answer)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

# Makes the player input the answer for the specifc blank	
def quiz_check(quiz, answers):
    i = 0
    for blank in blanks:
        player_answers = raw_input("\nPlease fill in blank # " + str(i+1) + ": ")
        while player_answers.lower() != answers[i].lower():
            print "\nYour answer was wrong. Please try again."
            player_answers = raw_input("Type it here again: ")
        print "\nAwesome, that's correct!\n"
        quiz = fill_in(quiz, blank, answers[i])
        print "QUIZ\n" + quiz
        i += 1

# According the level, returns the quiz and answers 		
def setup_quiz(level):
    if(level == "easy"):
        print "QUIZ\n"+ easy_quiz
        return easy_quiz, easy_answers
    elif(level == "easy"):
        print "QUIZ\n"+ medium_quiz
        return medium_quiz, medium_answers
    else:
        print "QUIZ\n"+ hard_quiz
        return hard_quiz, hard_answers

# Plays the game!
def play_quiz():
    name = get_name()
    level = get_level()
    quiz, answers = setup_quiz(level)
    quiz_check(quiz, answers)
    print "\nCongrats, " + name + ", You've finished the quiz!\n"	

play_quiz()