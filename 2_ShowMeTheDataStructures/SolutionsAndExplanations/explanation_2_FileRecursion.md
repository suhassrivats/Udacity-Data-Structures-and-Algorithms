# Explanation_2: File Recursion

**Requirement:**

The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

**Summary:**

In order to implement this, I have used `find_files` function which will take `suffix` (file extension) and `path` (directory path where we need to search). In this function, I am recursively searching for a file with a given extension in a parent directory and all its sub-directories. I am storing all these files with a given suffix in a list and returning it.

**Time and Space Complexity:**

*Time Complexity:*

I think the complexity is O(path_elements), where `path_elements` is the total number of files and folders returned by all calls to `os.listdir()`. Consider a folder that has four files in a single directory:

```py
folder
  zip.c
  foo.c
  bar.c
  bas.c
```

So my function calls `os.listdir()`, which returns four files. So `n = 4`. The code then iterates over the list to find folders, of which it finds none, and again to pick out the .c files, which it adds to the list.

The complexity here is O(n) to call `os.listdir()`, O(n) to search for folders, and O(n) to pick out the .c files and add them to the list. Altogether O(3*n), which is O(n).

Now consider this directory tree:

```py
folder
  sub1
    zip.c
    foo.c
  sub2
    bar.c
    bas.c
```

So the first call to `find_files` calls `os.listdir(folder)`, which returns two folders. Each folder makes a recursive call to `find_files`. Altogether there are three calls to `os.listdir()`, and each one returns two files, so the total number of items returned by `os.listdir()` is 6.

Now imagine we had:

```py
folder
  sub0
    sub1
      sub2
        sub3
          ...
            sub30
              file1.c
```

The complexity here is still O(n). In this case, n is 31.

The point I'm trying to make here is that we look at each item returned from `os.listdir()` a constant number of times. Thus, O(n).

Reference: https://stackoverflow.com/questions/61255507/time-and-space-complexity-of-a-file-recursion-algorithm



*Space Complexity:*

1. Input Space

   - suffix (str) - `O(1)`
   - path (str) - `O(1)`
   - Input space for `depth` iterations => `O(depth * Average number of directories in each level)`
   
2. Auxiliary Space

   Recursion uses something called as "call stack". When a function calls itself, that function goes on top of the stack. 

   - In this algorithm, the recursive function is exhausted only if it has traversed every directory. In other words, when it has reached the `depth`. Therefore `O(depth)` space is required in the call stack.

3. Total Space Complexity => Input Space + Auxiliary Space 

   => `O(depth * Average number of directories in each level + depth)` 

   => `O(depth * Average number of directories in each level)`
