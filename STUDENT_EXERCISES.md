# Student Exercises

## Exercise 1 — Inspect history

Run:

```bash
git log --oneline --graph --all
```

Questions:

- How many branches can you identify?
- Which commits exist only on a feature branch?
- Which branch appears to be ahead of `main`?

## Exercise 2 — Create your own branch

Create:

```bash
git switch -c feature/add-turtle
```

Add a new turtle to `data/animals.csv`.

Then:

```bash
git status
git diff
git add data/animals.csv
git commit -m "Add turtle record"
```

## Exercise 3 — Merge a feature

Merge your new branch into `main`.

## Exercise 4 — Resolve a conflict

Try merging:

- `conflict/cat-description`
- `conflict/dog-description`

Resolve `docs/notes.md` so that both animals are mentioned.

## Exercise 5 — Stash

Modify a file without committing, stash the change, switch branches, then restore it.

## Exercise 6 — Rebase

Rebase `exercise/rebase-demo` onto the current `main`.

Compare the history before and after with:

```bash
git log --oneline --graph --all
```

## Challenge

Create two branches that both modify the same animal record in different ways and intentionally produce a new merge conflict.
