# western-occult-magick

This repository is for helping you to learn about yourself and the world (micro- and macro-cosm) using the four basic occult sciences of the 
Western Mystery Tradition which has its roots in Egypt:

- Tarot
- Astrology
- Qaballah
- Numerology

The first of these I'm working on is Numerology.  The bith-path script is partially complete, it needs to be updated with details
about the meaning of the numbers.  Next will be the Life Path script.

The Numerology script will be able to give you a full reading about your nature and abilities.  Eventually the goal is for it to 
give you a ful 365 day calendar of the daily numbers as well as your daily numbers for various use cases.  I would also like
to be able to give it a decent interface as a program or on a website instead of just being run in the command-line.

6/25 - Found an issue with the birth-path script which reduces even a master number if there are more than two digits.  Not an issue
      in the usage of this script but will look for ways to improve the code so that it works better.
    
6/27 - The life-path script is getting close, however I'm running into an issue similar to above in which a master number is being
      reduced when it should not.  Looking for an improvement so that it adds each number up as it goes through the for loop so
      that it doesn't get too big and reduces incorrectly.
      
6/28 - The life-path script is complete except for adding more details about what the numbers actually mean.  I'll probably have more
      completed on this tomorrow.
      
7/6 - Reading up on my Numerology today I realized I have made some glaring errors as far as Numerology is concerned.  I am re-focusing my efforts
      on fixing this issue as I believe it is important.  What I was calling the birth-path (because it is determined by the numbers of the birthday) 
      is actually the Life Path and the majority of the necessary information to determine personality and abilities.  There is also the Soul's Urge
      (which I was calling the life-path) and it has to do with the person's Name at birth.  There is also the Expression and the Birthday which also
      play a part in determining the character and gifts of the person.  As I said I am excited to keep learning more Numerology AND Python and how
      to masterfully implement these learnings in order to improve myself and make this information accessible to others.
      
7/8 - Here is the updated version of my Numerology script (numerology.py).  I managed to cut the code from over 300 lines down to around 150 lines of code.  There are a few things I still plan on streamlining and cleaning up such as the functions.  I'm happy with how elegant the calculations turned out after trying it many different ways and learning a lot.  I still need to add descriptions for all the numbers, coming soon.

7/10 - Typed up some of the Numerology meanings, I am mostly done with the general meanings.  I'm going to have to summarize some things so it doesn't become 
      too much information.  It should be enough information to get the point across but not too much to confuse the person looking for answers about their inner self.

---

To Do List:

[ ]  Order number results so that the most important (life path) is displayed first, and so on (instead of numerical order)
[ ]  Add in text descriptions for :       [ ]   Expression
                                          [ ]   Soul Urge
                                          [ ]   Birthday


Stay tuned, I'm looking forward to working on this more.

Thank you!
