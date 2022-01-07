# Bash drill

A basic drill for getting reps on shell commands. And some food for
thought.

- [The drill](#the-drill)
- [To Ponder](#to-ponder)
- [Variations on the drill](#variations-on-the-drill)

## The drill

Open a terminal.

> Below is working code. Lines that start with `#` are code comments
> (i.e. they will not be executed).

```
# Unix is profound
whoami

# Where am I? You're in your home directory!
pwd

# What dirs/files do you see?
ls

# Random tidbit: To clear your shell
clear # or CTRL + l

# Let's create a code directory
mkdir code

# What happens if you try to create it again?
mkdir code

# Be more forgiving (commands have flags!)
mkdir -p code

# What is that flag all about? Are there other options?
man mkdir # or you can use the Internet

# Hit "q" to exit out of the manual for mkdir!

# The manual can be quite long for some commands
man find

# Don't forget to hit "q" to exit the manual!

# OK, back to our previously scheduled program...

# Navigate to the code directory
cd code

# Print working directory
pwd

# Create a new directory
mkdir bash-drill

# Navigate into the new directory
cd bash-drill

# Echo echoes...to the shell. It really is useful. Trust us.
echo dog

# Create an empty file
touch animals.txt

# ...but echo can send text to a file with
echo dog > animals.txt

# Print file contents to shell
cat animals.txt

# Append "bird" to animals.txt
# NOTE: We're using ">>" to append.
#  Otherwise it overwrites!
echo bird >> animals.txt

# Append "hamster" to animals.txt
echo hamster >> animals.txt

# Count the lines in animals.txt
wc -l animals.txt

# You can also print the first few lines of
# a file using "head" (first 10 by default)
head animals.txt

# You can configure head, e.g. to just
# output the first line
head -1 animals.txt

# Or print the last lines of a file
tail -1 animals.txt

# Search the file for the word dog
grep dog animals.txt

# Sort the words in the file
sort animals.txt

# Note this doesn't change the underlying file
cat animals.txt

# Sort the animals.txt and save the sorted list to animals_sorted.txt
sort animals.txt > animals_sorted.txt

# Rename animals.txt to pets.text
mv animals.txt pets.txt

# Copy animals_sorted.txt to animals.txt
cp animals_sorted.txt animals.txt

# List the directory contents
ls

# List with file details
ls -l

# List file details in human-readable way
ls -lh

# Delete animals.txt
rm animals.txt

# List the directory contents
ls

# Navigate to the parent directory
cd ..

# Print working dir (should be in ~/code)
pwd

# List directory contents (should see code/ dir)
ls

# NOTE: Store all your code in this directory going forward!!

# Create a symlink, or shortcut, to code/ dir from your Desktop
ln -s ~/code ~/Desktop/code

# Check out the symlink
cd ~/Desktop
ls -l code

# Navigate into shortcut dir to verify it works
cd code
ls  # you should see bash-drill/

# OK, let's clean up now.  Delete the directory (this will fail)
rmdir bash-drill/

# List contents of bash-drill
ls bash-drill/

# Remove all contents of bash-drill
rm bash-drill/*

# Remove the dir
rmdir bash-drill/

# Verify bash-drill is gone
ls

# Unix/bash has built-in variables
# For example
echo $HOME  # (told ya echo was handy)

# Print all variables in your env. Whaaaaat?????
env

# Print your env and filter the
# output for just the PATH variable
env | grep PATH

# Or just echo $PATH
echo $PATH
```

## To ponder

Some things to consider/discuss/research:

- What happens if I `echo 'foo' > animals.txt'`? What's the difference between `>` and `>>`?
- What is that pipe thing ("|") all about?
- What are shell environment variables (aka output from `env`)?
- Why does echo print environment variables when prefixed with the `$`
  sign? E.g. `echo $PATH`
- What other commands are "built-in" and automatically available on Unix?

## Variations on the drill

The [Bash Drill](#the-drill) provides a short crash course on basic shell usage and Unix commands. 
We'll do this drill several times over the quarter to build muscle memory on the command line. The first few passes through the drill will be slow-going as we work through snags and take time to discuss questions
that arise along the way.

As everyone becomes more comfortable on the command line, we'll go "off script" and apply one or more of the following variations to the exercise.

- **Rotating leads**. We'll rotate drill leaders for entirety of exercise or even during a single run of the exercise (i.e. have multiple leads during a single walk-through).
- **Blind-folded**. Drill leader will not screenshare and will instead speak the commands. At the end of drill, we'll see if everyone ended up with same results.
- **Plain English**. Drill leader will *describe* the commands to type rather than specifying the precise sytnax. For example, she will say "*Navigate* to your code directory" rather than "*cd* to the code directory". Combine this with the **Blind-folded** method to better test mental translation and recall.
- **Ad lib**. Drill leader will make up ad hoc commands rather than using the commands specified on this page.
- **Berserk**. Drill leader will **Ad Lib** quickly and won't stop for questions or help on fixes. Errors will be made. Let's embrace them.


