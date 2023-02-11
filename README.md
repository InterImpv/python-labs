Doing an assignment for uni.

At this point:

1. Created and initialized new repo `lab_git` with ```git init lab_git```
2. Switched to the working directory with ```cd lab_git```
3. Created files `README.md` & `.gitignore` using ```touch README.md``` & ```touch .gitignore```
4. Copypasted `gitignore` from [here](https://github.com/github/gitignore/blob/main/Python.gitignore)
5. Added everything to the staging area using ```git add README.md .gitignore``` & commited everything with ```git commit -m "feat: added a basic description & a gitignore for python"```
6. Created a new branch `first_branch` & switched to it by ```git checkout -b first_branch```
7. Modified this file adding step-by-step description of how the tasks were done
8. Displayed the state of the working directory and the staging area with ```git status```
9. Will commit current changes
10. Switched to `master` branch using `git checkout master`
11. Modified `README.md`
12. Will commit everything in a moment
13. Displayed project history using ```git log``` & ```git log --pretty=oneline```:

```console
krypton@argon:$ git log
commit e6ef1fcf02b78b7b1baa85c632c6bde748e17b01 (HEAD -> master)
Author: InterImpv <chaoticchloride@gmail.com>
Date:   Wed Feb 8 17:11:19 2023 +0200

    feat: added a basic description & a gitignore for python
```

```console
krypton@argon:$ git log --pretty=oneline 
e6ef1fcf02b78b7b1baa85c632c6bde748e17b01 (HEAD -> master) feat: added a basic description & a gitignore for python
```

14. Merged `first_branch` into `master` using ```git merge master first_branch``` & resolved a conflict
15. Commited all the changes
16. Displayed current project history with ```git log --pretty=oneline``` for simplicity:

```console
krypton@argon:$ git log --pretty=oneline 
386c5f7e2e2a070aba59a2761c448ef4d67e9787 (HEAD -> master) merge: branch 'first_branch' into 'master'
74acd19938b1000d5f19301d2463debdbd22f7ee feat: new cool things in README.md
0093ccac88c028d31167db017f89863ea4a1757f (first_branch) feat: new cool stuff in README.md
e6ef1fcf02b78b7b1baa85c632c6bde748e17b01 feat: added a basic description & a gitignore for python
```

17. Added one *lightweight* tag & one *annotated* tag with ```git tag v0.1 e6ef1fcf``` & ```git tag -a v0.2 cf9c345a -m "This is an annotated tag."``` respectively