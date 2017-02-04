import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

from mitie import *
import nltk

ner = named_entity_extractor("testmodel1.dat")

desc = """Minimum 4 Years of active web development experience in a team atmosphere along with 3 Years active WordPress development
Knowledge and proficiency in the following application development languages: PHP, HTML5 / CSS3
Javascript / JQuery
MySQL
Advanced knowledge of WordPress including administration and security
Experience developing custom WordPress themes and plug-ins
Knowledge of how to interact with RESTful APIs and formats (JSON, XML)
Understanding of the entire LAMP Stack (Linux/Apache/MySql/PHP)
Strong knowledge of web application testing methodologies and ability to self-certify developed code for production
Experience implementing LMS, CRM and e-commerce systems an asset
Understanding and application of Responsive Design
Job Type: Full-time

Salary: $70,000.00 /year

Job Location:
    
    Ottawa, ON
    Required education:
    
    Bachelor's
    Required experience:
    
    Web Development: 3 years"""


tokens = mitie.tokenize(desc.replace('/', ','))

print tokens

entities = ner.extract_entities(tokens)

for e in entities:
    range = e[0]
    tag = e[1]
    entity_text = " ".join(tokens[i] for i in range)
    print ("    " + tag + ": " + entity_text)
