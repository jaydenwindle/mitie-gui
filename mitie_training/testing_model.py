# -*- coding: utf-8 -*-
import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

from mitie import *
import nltk

def custom_tokenize(s):
    s = s.replace(';', ' , ')
    s = s.replace('/', ' , ')
    s = mitie.tokenize(s)
    return s

ner = named_entity_extractor("25_dev.dat")

desc = """

 What will you do?
  
  Implement various application components and perform integration and performance testing.
  Responsible for development, enhancement and maintenance of client-facing web-components, that may be internally developed or vendor applications.
  Work with Business Analysts to come up with optimal IT solutions for business problems
  Perform design and code reviews and prepare technical documentations
  Work with Information Security to review and implement controls and procedures for securely handling data
  Develop, code, document and execute unit test, system, integration and acceptance test using different languages and testing tools for functions of high complexity.
  Develop detailed plans and accurate estimates for completion of build, system testing and implementation phases of project.
  Provide on-call L4 support of applications, database
  Ability to work with offshore team members.
  Validate overall application design and make sure that applicable technologies are being used.
   
   What do you need to succeed?
    
    Must Have
    2-5 years of experience in software web development cycle using OO concepts using mainstream languages
    In depth experience with Microsoft.NET development stack using C#, ASP.NET, ASP.NET MVC
    Working experience in client scripting languages and framework such as JavaScript, JQuery,  AngularJS, Bootstrap
    In depth experience in database development using SQL Server 2008/2012
    Strong SQL skills (on Sybase or SQL Server platforms)
    Frameworks/APIs: .NET, Web Services
    OS & Tools: Visual Studio 2010+, Eclipse, SVN, UNIX, & DevXPress
    Design and develop distributed scalable applications using Microsoft .NET
    Experience in MS Technologies (ex. MS IIS Server, SSRS, SSIS, etc.)

"""


tokens = custom_tokenize(desc)

print tokens

entities = ner.extract_entities(tokens)

for e in entities:
    r = e[0]
    tag = e[1]
    entity_text = " ".join(tokens[i] for i in r)
    if len(entity_text) > 1:
        print ("    " + tag + ": " + entity_text)
        
