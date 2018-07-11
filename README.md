# filename-vc-to-git
Converts filename based version/source control to a git repo.

## Notes
- original intent was to convert a large set of old projects that were managed without proper version control (save file with new name for each version) into a managable git repo 
- see below for argument documentation
- uses pip for module management in venv
- uses str.startswith($pattern)
- warning: if a file version changes (test1.1.txt and test1.2.txt) exist but their contents are identical, then git/sh/pbs will fail out
- warning: if a nested folder of $path_to_scan/working/ already exists, it will be initialized or re-initialized as a git repo!  This could result in minor corruption of git repos.

## Argument Documentation
Expected commandline: 
```
pipenv run python main.py <dir_to_scan> <pattern> <new_file_name>
```

Example (on Windows, untested on other envs):
```
pipenv run python main.py '/c/my_stuff' 'testfile_' 'test_project.py'
```

- after creating the git repo(s), see the following [link](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)