# Practicing with Git and Github

This assignment will walk you through forking the respository for this 
program, cloning your forked copy to your local machine, and some of the 
Git commands discussed in lecture. Similar to the Unix assignment, this 
assignment will be fairly brief, as familiarity with Git and Github will 
come over time as you interact with them more and more. 

1. Open up your browser and navigate to this program's repository on 
[Github](https://github.com/zipfian/DSI-evening-prep). 

2. Fork a copy of this repository, making sure to fork it to your Github
account (usually it forks to your Github account by default, so if you're not
prompted, then you should be fine). The button to `Fork` should be up in the 
top right of the page: 

 ![Github Forking](imgs/github_fork.png)

3. Now navigate to your own Github repository, and grab the URL for your 
fork so that you can clone it to your local machine. You should be able 
to find the URL in the top middle of the page: 

 ![Clone Fork](imgs/clone_fork.png)

4. In the terminal on your local, use the URL you just copied to clone 
your Fork of this program's repository. Make sure that you are in a directory
where you are okay storing this repository. 

 ```bash 
git clone URL # Insert the URL you copied here in place of URL. 
```

5. Navigate into the repository, and create a file called `test_git_file.txt`.
This will require some of the Unix commands that we have previously discussed. 

 ```bash 
cd DSI-evening-prep
touch test_git_file.txt
```

6. Add this file to the .git index (we're now back to using Git commands). 

 ```bash 
git add test_git_file.txt
```

7. Commit this file, and then push it to your forked copy of the repository 
on Github. Navigate to your forked version of the repository on Github, and 
check to make sure that the `test_git_file.txt` is present there. 

 ```bash 
git commit -m 'Add test_git_file.txt`
git push
```

8. Back in your terminal on your local, remove `test_git_file.txt` from 
the repository. 

 `rm test_git_file.txt`

9. Add, commit, and push this change. 

 ```bash
git add test_git_file.txt
git commit -m 'Remove test_git_file.txt'
git push
```

10. Navigate back to your forked version of the repository on Github, where
you should see that the `test_git_file.txt` is no longer there. 
