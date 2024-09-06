# Feedback on your portfolio

Only four commits; it seems as though you have committed all the files in one big flow. I am also missing a `.gitignore`-file (e.g. for `__pychache__`-directories). Your work is nicely divided in several directories and you have given a small description of all the elaborations in your readme.

## ex1

Nice enough elaboration; please see my comments in the individual files.

## ex2

Nice elaboration. I would have preferred a markdown-file instead of a text-file, as that allows for some typographical information. But still ok; good that you have provided an extensive class diagram. You could have made this better if you had provided some statistical analysis, e.g. the average number of lines per method, or the number of classes, etc. 


## ex3

Good elaboration; not much to comment on. Just one small thing in the code itself.

## ex4

Very nice elaboration, with a comparison of MP and non-MP. Also good that you did not put your credentials in the repo. 

## final

Nice elaboration. I like the architecture of creating and saving the model if it is not already present. Please see my comments in the individual classes. The main problem is that you keep on creating new instances of classes (all over the place) and I don't actually know how watchdog will handle these (if they are re-used or garbage-collected). 