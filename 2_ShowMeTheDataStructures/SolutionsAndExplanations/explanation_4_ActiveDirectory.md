# Explanation_4: Active Directory

**Requirement:**

Write a function that provides an efficient look up of whether the user is in a group.

**Summary:**

There is a `Group` class which will perform all the group related operations such as `add_group`, `add_user`, `get_groups`, `get_users`, and `get_name`.

In order to check if a user exists in a particular group or in group's groups (subgroups), I have written a method `is_user_in_group` which takes `user` and `group` parameters.

- First, it will check if a user exists in a given group. If he exists then it returns True.
- If not, it will check for all the subgroups of a given group recursively and return True if he exists in any of the subgroups. Return False otherwise.

**Time and Space Complexity:**

*Time Complexity:*

- `users` is a list of users. To check if a user exists in this list is a linear operation. If `l` is the length of this users list => `O(l)`
- `group_list` is a list of groups at each level. Iteating through this list is also linear => `O(g)`. If there are `k` number of groups (branches) in each level in `depth`, then the total number of groups is `braches^depth`. Let us call this `n`.
- For recursion, time complexity for a tree of n nodes (here groups) is `O(n)` and for each node there is a list of users of length `l` and list of groups of length `g` that we need to search for a user. So the time complexity is `O(n* (l+g))`



*Space Complexity:*

1. Input Space:
   - users => `O(l)`
   - group_list => `O(g)`
   - Input space for one iteration => `O(g+l)`
   - Input space for `depth` iteration => `O( depth * (g+l) )`

2. Auxiliary Space:
   - The recursive function is exhausted only if it has traversed every directory. In other words, when it has reached the `depth`. Therefore `O(depth)` space is required in the call stack.
3. Total Space Complexity = Input Space + Auxiliary Space => `O(depth*(g+l))` + `O(depth)`  => `O(depth*(g+l))`
