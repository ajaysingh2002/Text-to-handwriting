import pywhatkit as py

text="""
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
Its high-level built in data structures, combined with ..
"""

py.text_to_handwriting(text,"demo.png",[0,0,138])
print("end")