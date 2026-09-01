# Instructor Guide

## 1. Explore the repository

```bash
git status
git branch
git log --oneline --graph --all
```

## 2. Basic branch exercise

```bash
git switch feature/add-birds
git diff main..feature/add-birds
git switch main
git merge feature/add-birds
```

Explain that this merge may be a fast-forward if no new commits were created on `main` after the branch point.

## 3. Independent feature

```bash
git switch feature/status-summary
git diff main..feature/status-summary
```

Students can inspect the Python change and merge it later.

## 4. Conflict exercise

Start from one conflict branch and merge the other:

```bash
git switch conflict/cat-description
git merge conflict/dog-description
```

`docs/notes.md` should conflict because both branches modify the same section differently.

Inspect:

```bash
git status
```

Resolve the file manually, then:

```bash
git add docs/notes.md
git commit
```

## 5. Rebase exercise

First update `main` if desired, then:

```bash
git switch exercise/rebase-demo
git rebase main
git log --oneline --graph --all
```

Explain that the rebase rewrites the branch commit on top of the current `main`.

## 6. Stash exercise

Make an uncommitted edit:

```bash
echo "Temporary classroom note" >> docs/notes.md
git status
git stash
git status
git stash list
git stash pop
```

## 7. Diff exercise

```bash
git diff
git diff main..feature/status-summary
git show HEAD
```

## 8. Revert exercise

Create a harmless commit, then revert it:

```bash
echo "Temporary line" >> README.md
git add README.md
git commit -m "Add temporary line"
git revert HEAD
```

Discuss why `revert` is safer than rewriting history on shared branches.

## Suggested sequence

1. Repository anatomy
2. status / add / commit
3. log / diff
4. branches
5. merge
6. conflicts
7. stash
8. revert
9. rebase
