# Hints — Compare the Triplets

> Only open the next hint if you are truly stuck. Think first.

<details>
<summary>Hint 1 — Big Picture</summary>

You need to compare two lists element by element. How do you visit both lists at the same index simultaneously?

</details>

<details>
<summary>Hint 2 — Structure</summary>

You need two counters — one for Alice, one for Bob. Loop over all 3 positions and update the right counter on each comparison.

</details>

<details>
<summary>Hint 3 — Iteration</summary>

`zip(a, b)` gives you pairs `(a[i], b[i])` without managing an index manually. Try it.

</details>

<details>
<summary>Hint 4 — Almost There</summary>

Return `[alice, bob]` as a list. The boilerplate prints it with `' '.join(map(str, result))`.

</details>
