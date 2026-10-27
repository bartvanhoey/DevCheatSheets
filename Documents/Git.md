## Git and GitHub Tips and Tricks

### Install GitHub CLI

```bash
  winget install --id GitHub.cli
  gh auth login
```

### Switch User in GitHub CLI

```bash
  gh auth switch --user <your-/username>
```

### Howto handle Support for password authentication was removed ... Please use a personal access token instead

```bash
  C:\>git push -u origin main
  Username for 'https://github.com': <your-username>
  Password for 'https://<your-username>@github.com':
  remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/<your-reponame>.git/'
```

#### Solution: Generate Personal Access Token in GitHub

My account - Settings - Developer Settings - Personal Access Token - Generate New Token

admin:repo_hook Full control of repository hooks

* write:repo_hook Write repository hooks [checked]

* read:repo_hook Read repository hooks [checked]

```bash
  git remote set-url origin https://<personal-access-token>@github.com/<github-account>/<repo-name>.git
```

### Howto Clone a Private Repository

Create Personal Access Token first.
Go to your GitHub Repository Settings - Developer Settings - Personal Access Token (classic) - Select scopes: repo - Generate New Token

```bash
  git clone https://<personal-access-token>@github.com/<github-account>/<repo-name>.git
```

### Howto handle Write access to repository not granted

```bash
  remote: Write access to repository not granted.
  fatal: unable to access 'https://github.com/<your-username>/<your-reponame>.git/': The requested URL returned error: 403
```

#### Solution: Remove the remote origin and re-add the remote origin

```bash
  git remote rm origin
  git remote add origin  https://<your-username>:<your-personal-accesstoken>@github.com/username/reponame.git
```

### Howto handle fatal: unable to access - The requested URL returned error: 403

`remote: Permission to <github-account>/<repo-name>.git denied to <user-name>.`
`fatal: unable to access 'https://github.com/<github-account>/<repo-name>.git/': The requested URL returned error: 403`

#### Solution: Generate Personal Access Token in GitHub Account

My account - Settings - Developer Settings - Personal Access Token - Generate New Token

admin:repo_hook Full control of repository hooks

* write:repo_hook Write repository hooks [checked]

* read:repo_hook Read repository hooks [checked]

```bash
  git remote set-url origin https://<personal-access-token>@github.com/<github-account>/<repo-name>.git
```

### Howto check contributions from a git repository

[Whodid](https://www.npmjs.com/package/whodid) is a CLI contribution check tool that counts edited lines from all commits pro author

```bash
  npm install -g whodid
```

### Howto remove old local branches that do not exist on remote repository anymore

There's a neat NPM package that does it for you (and it should work cross-platform).

Install it with:

```bash
  npm install -g git-removed-branches
```

And then git removed-branches will show you all the stale local branches, and git removed-branches --prune to delete them

* Run this command to see which branches will be deleted

```bash
  git removed-branches
```

* Run this command to actually delete these branches

```bash
  git removed-branches --prune
```

* Run this to actually delete these branches (forced)

```bash
  git removed-branches --prune --force
```

### Howto remove old unused branches of a remote repository

* Run this to see which branches will be deleted!

```bash
  git remote prune origin --dry-run
```

* Run this command to delete these branches
  
```bash
  git remote prune origin
 ```

### Howto uncommit last un-pushed git commits without losing changes (~gN N=number of commits)

```csharp
  // KEEP CHANGES
  git reset HEAD~1 --soft
  git log origin/master..HEAD  // view unpushed git commits
```

### Howto uncommit last un-pushed git-commit DELETE CHANGES (~gN N=number of commits)

```csharp
  // DELETE CHANGES
  git reset --hard HEAD~1
```

### Howto stash changes

error: Your local changes to the following files would be overwritten by checkout:
Please commit your changes or stash them before you switch branches.

```csharp
git stash
# Checkout branch and apply stash on the checked out branch
git stash pop
```

### Howto revert all uncommitted changes made to _tracked files_ (i.e. that you have added)

error: Your local changes to the following files would be overwritten by checkout:

`git reset --hard HEAD`

### Howto remove uncommitted _untracked files_ (e.g., new files, generated files)

`git clean -f`

### Howto remove uncommitted _untracked files or directories_ (e.g., new files, generated files)

`git clean -fd`

### Howto add a remote repository

`git remote add origin https://github.com/your-user-name/repo-name.git`

### Howto deal with error: 'fatal: The current branch master has no upstream branch'

`git push --set-upstream origin master`

### Howto deal with error: 'error: failed to push some refs to '<https://github.com/your-username/repository-name.git>'

hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

`git push --force`

> **Prefer `--force-with-lease`** — it refuses to push if the remote has commits you haven't fetched, preventing accidental overwrite of a teammate's work.

`git push --force-with-lease`

### Howto handle fatal: refusing to merge unrelated histories

`git pull origin <branch-name> --allow-unrelated-histories`

### Howto show all local branches

`git branch --list -a`

### Howto delete a local branch

`git branch -d <branch-name>`

### Howto delete a remote branch

`git push origin --delete <branch-name>`

### Howto fix authentication git repository in AzureDevops in VSCode

First get the remote origin.url

```bash
  git config --get remote.origin.url
```

Then set personal-access-Token (Find it in AzureDevops -> User Settings -> Personal access tokens )

```bash
  git remote set-url origin https://<user-name>:<personal-accesstoken>@dev.azure.com/<company-name>/<project-name>/_git/<repo-name>
```

### Howto recover a deleted local branch

```bash
  git reflog
  git checkout -b <branch-name> <sha>
```

### Howto fix Error "Fatal: Not possible to fast-forward, aborting"

```bash
  git pull --rebase
```

### Howto deal with 'error: failed to push some refs to '<https://github.com/your-username/repository-name.git>'

hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

`git pull <remote> <branch>`

### Howto exit git log window

`q`

### Howto revert to a previous commit

`git reset --hard HEAD` — discards uncommitted working tree changes, stays on the same commit

### Howto set your branch to exactly match the remote branch

```bash
git fetch origin
git reset --hard origin/master
# to remove local files
git clean -f 
# to see what files will be removed without removing them
git clean -n -f 
```

### Howto checkout a specific commit

```bash
git checkout <sha>
```

### Howto revert to a specific commit

```bash
git revert --no-commit <sha>..HEAD
git add .
git commit -m "your-commit-message"
git push origin <branch-name>
```

### Howto change an un-pushed commit-message

`git commit --amend`

After updating the message leave VIM editor by pressing

```csharp
Esc
:wq
```

### Howto delete the most recent commit, keeping the work you've done

`git reset --soft HEAD~1`

### Howto Delete the most recent commit, **destroying** the work you've done

`git reset --hard HEAD~1` — moves back one commit; the commit and its changes are permanently gone

### Howto change a pushed commit message (not yet pulled from remote)

`git commit --amend`

After updating the message leave VIM editor by pressing

```csharp
Esc
:wq
```

```bash
git push --force-with-lease <repository> <branch>
```

### Howto turn off **warning: LF will be replaced by CRLF in ...**

warning: LF will be replaced by CRLF in ... The file will have its original line endings in your working directory.

In Unix systems, the end of a line is represented with a line feed (LF). In windows, a line is represented with a carriage return (CR) and a line feed (LF) thus (CRLF). when you get code from git that was uploaded from a Unix system they will only have an LF.

`git config core.autocrlf true`

### Howto add a .gitignore file to a repo after it already has commits

```bash
git rm -r --cached .
git add .
git commit -m ".gitignore is now working"

```

### Howto exit git log or git diff screen

`q + ENTER`

### Howto deal with a message **There is no tracking information for the current branch. Please specify which branch you want to merge with.**

When you are on local branch master and no changes are coming in from remote master after git pull and you see the above message.

`git branch --set-upstream-to=origin/master master`

### Howto show details of a raw commit object (author/committer/date/details/SHA-1 Hash)

`git show --pretty=raw HEAD`

### Howto display references available in a local repository along with the associated commit IDs

`git show-ref`

### Howto get the tree-like view of commits in terminal

`git log --graph --oneline --all`

### Howto deal with message **fatal: Unable to create ... '/../git/index.lock': File exists**

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.

`rm -f ./.git/index.lock`

### Howto create a GitHub Pull Request from the command line

Make sure you have installed the command line tool 'hub'

`hub pull-request -m "your-pull-request-message" -b master -h <local-branch-name>`

### Howto merge a GitHub Pull Request from the command line

Checkout master branch first: `git checkout master`

`hub merge https://github.com/<your-github-account>/<repository-name>/pull/10`

### Howto merge master in your local branch

```bash
git checkout <local-branch-name>
git fetch origin
git merge origin/master
```

### Howto handle error **error: Your local changes to the following files would be overwritten ...** when checking out another branch

```bash
git stash
git checkout <branch-name>
git apply
```

### Howto undo all local changes

```bash
git restore --source=HEAD --staged --worktree -- .
```

### Howto keep a file in a git repo but don't track changes

```bash
git update-index --assume-unchanged <project-name><file-name>
## git update-index --assume-unchanged src/AbpFrameworkProjectName.HttpApi.Host/appsettings.json
```

### Howto to track changes again of an untracked file in a git repo

`git update-index --no-assume-unchanged <project-name><file-name>`

### Howto rename the local and remote branch

```bash
# Rename the local branch to the new name
git branch -m <old_name> <new_name>

# Delete the old branch on remote - where <remote> is, for example, origin
git push <remote> --delete <old_name>

# Or shorter way to delete remote branch [:]
git push <remote> :<old_name>

# Prevent git from using the old name when pushing in the next step.
# Otherwise, git will use the old upstream name instead of <new_name>.
git branch --unset-upstream <old_name>

# Push the new branch to remote
git push <remote> <new_name>

# Reset the upstream branch for the new_name local branch
git push <remote> -u <new_name>
```

### Workflow to create and merge GitHub Pull Request without leaving the terminal in VsCode

```csharp
git add .
git commit -m "your-commit-message"
git push origin <branch-name>
git checkout master
hub pull-request -m "your-pull-request-message" -b master -h <branch-name>
hub merge <pull-request-name>
git push
git push origin --delete <branch-name>
git branch -d <branch>
git checkout -b <new-branch-name>
```

## Howto create global git aliases

I run the following command `git devpull` and it will checkout the dev branch and pull the latest changes from the remote dev branch.

```bash
  git config --global alias.devpull '!git checkout dev && git pull'
```
