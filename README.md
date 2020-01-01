## C/Python Binding Demo

In this project, I'm trying to create a minimum working example of binding a C function to python, and prescribe a reasonable distribution method. Existing examples are either way too little or way too much. Some comments to outline how decisions are getting made:

 - I like that (at least so far) the C is very focused; it's just the actual function that I want to make available in Python, and not a ton of boilerplate. This is thanks to the wrapping made possible by the `ctypes` package, which we rely on here.
 - Also on the topic of `ctypes`, I like the very short toolchain - not too many moving parts to break or slide into obsolescence.
 - I like compiling with a Makefile; at least to me this is easiest to see what's going on in terms of compilation.
 - "Reasonable distribution method" means this should be as easy as possible for non-experts to install successfully on ubuntu-adjacent boxes. Do want to avoid making users do anything too hairy in terms of successful compilation and installation, do not care too much about extremely broad OS support (for now).
 
Please see and add discussion points in the issues.
 
## Usage

Clone this repo, and then:

install: `python3 setup.py install`

try it out: `python3 mwe.py` <-- should print out an array full of `2.`s
