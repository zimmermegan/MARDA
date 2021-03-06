# Project MARDA
Medical Assistant Robotic Drug Administer project files, implementing drug databases with a syntactic parser to create a platform for a medical assistant robot which helps monitor intake of specific drugs.


##Project Idea & Goals:
The project so far is designed to be a medical assistive robot directed primarily at the elderly. The robot will need to be able to take in verbal commands from the user regarding medical needs and take the best course of action based on that input. Things like opening a child safety locked medicine bottle and giving the correct amount of medicine to the user will be essential.

##To Do
- [ ] Generate a bunch of sample sentences to use with the parser - http://nlp.stanford.edu/software/lex-parser.shtml
- [ ] Explore the [CHEMDNER](http://mldata.org/repository/data/viewslug/chemdner-training/) Training Set, and developer a way to build some sort of decision tree to use for classification and such. 


##For CHEMDNER
- CHEMDNER uses the [BL-Evaluate Library](http://www.biocreative.org/resources/biocreative-ii5/evaluation-library/) as well as [Matplotlib](http://matplotlib.sourceforge.net/users/installing.html)
- Instructions to install: http://matplotlib.org/users/installing.html

##For Stanford NLP
- Github Page is here: https://github.com/stanfordnlp/CoreNLP
- Link to the core Jar File is here: http://search.maven.org/#browse%7C304784840
- Jar File Name is: `stanford-corenlp-3.5.1.jar`
- Documentation is found here: http://nlp.stanford.edu/software/corenlp.shtml
- Build in Eclipse, import the project via Eclipse Git Manager, and add the External Jar File to your Build Path, in order to run the executable Driver File
 


