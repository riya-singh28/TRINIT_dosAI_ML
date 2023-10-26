# TRINIT_dosAI_ML
Welcome to our crop prediction portal! We are dedicated to helping farmers and agriculture business owners make informed decisions about what crops to grow in their specific locations. Our innovative approach takes into account crucial factors such as soil composition, rainfall patterns, temperature fluctuations, and return on investment to provide farmers with the optimal crop choices.

Gone are the days of trial-and-error farming practices, where farmers spent large amounts of money on fertilizers and other resources only to have limited success. Our cutting-edge technology offers farmers a personalized and data-driven solution, allowing them to make informed decisions and achieve maximum profits.

We understand the importance of sustainable farming practices, and that's why our predictions also take into account the impact on the soil and its natural resources. By avoiding the repetition of growing the same crops in the same areas, farmers can maintain healthy soil and preserve it for future generations.

At our crop prediction company, we believe that the future of agriculture lies in the intersection of technology and sustainability. Join us as we revolutionize the farming industry and lead the way towards a brighter, more profitable, and sustainable future.


# A writeup on git basic functions while working on a repository.

1. Git is a language used for version control system of software. It is used to keep track of various stages of software development. Used are several commands, such as: 
    1. ```git init``` : Used to initialize a directory into a working repository compatible with git. 

    2. ```git clone <Repo_URL>``` : Used to clone an existing repository hosted on github/gitlab locally to your system.

    3. ```git add .```: After working on a repository, you may/may not have added new files. ```git add <files>``` adds the files to the working git tree. The ```.``` is done for all files.

    4. ```git commit -m "commit name"``` : This is kind of like a ```Ctrl+S``` mechanism for git. Your progress is saved and put to the working branch as a commit.

    5.   ```git fetch```: While you are working locally on your system, changes may have been made by other users on the repository hosted. Git fetch makes a request to check whether changes have been done or no.

    6. ```git pull```: While fetch just checks. Pull will pull the changes made into your local repository. Sometimes there may be conflicts, which we will see later.

    7. ```git push```: after making a commit on local machine, you would want to save it on github. for this we do ```git push origin <branch>```. This pushes to the desired branch.

2. Often when we pull changes, changes can have been made to the same file which we have worked and committed on. This makes it difficult for the pull to merge with the commit. We call this merge conflict.
This can be solved two ways. Either by comparing the two changes and working around them to make a new commit, or by forcefully pushing one change over the other. The former is a better practice.

3. When making a git commit, make sure to name it something meaningful, especially if it is a team repository. Do not name your commits random gibberish as it will be very inconvenient to others. In your commit, you will want to summarize what the changes are to your code in one line. Whether you added files, or fixed a bug, or updated README, etc. 

4. When working with a repo, we would want to ignore certain files. For example, suppose I am working on C files. I will find the output files ending with .out to be very cumbersome and annoying as they do not work anyways and are basically useless. For this, I can make a file called ```.gitignore``` in which I specify the files which I want to ignore, in this case ```*.out```. This will conveniently ignore the output files whenever I commit and push.


