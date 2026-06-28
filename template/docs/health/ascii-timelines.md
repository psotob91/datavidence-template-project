# ASCII timelines & decision diagrams (shared notation)

Plain-text diagrams are the **comprehension gate** for time-based clinical logic: if you
cannot draw the rule, you do not understand it well enough to code it. This file defines one
notation used by both `phenotyping.md` and `routinely-collected-data.md`. Draw the diagram,
get human sign-off, **then** write pseudocode.

Why ASCII (not only Mermaid/ggplot): it lives in the script/prose next to the logic, diffs
cleanly in git, and forces explicit boundaries. Render an exact-geometry version (ggplot /
Python) later for publication if needed.

## Symbols

| Symbol | Meaning |
|---|---|
| `====` | observable / at-risk time |
| `----` | not-at-risk or **non-observable** time (gap, pre-enrollment, post-disenrollment) |
| `\|` | an anchor date (index, entry, exit, split point) |
| `o` | an observed record / event |
| `x` | the index / candidate event |
| `c` | a confirming record (used to classify, not to move time-zero) |
| `!` | the outcome |
| `D` | death |
| `L` | loss to follow-up / disenrollment |
| `?` | unobservable gap (absence here is **not** "no event") |
| `[` `]` | **inclusive** window boundary |
| `(` `)` | **exclusive** window boundary |

Always label the time axis (units + direction) and state date granularity (day vs month).
Use **ISO 8601** dates (YYYY-MM-DD).

## Template form 1 — a timeline with windows

```
time →            (units: days; granularity: day)
observable:   ====================x====================!=========
washout:      [------------------)
index:                           |x
outcome win:                      (--------------------]
status: index valid iff the washout is fully inside observable time
```

## Template form 2 — future confirmation without a time-zero shift

```
observable:   =========x===============c=====================
index:                 |x
confirmation:                          |c          (c classifies; time-zero stays at x)
outcome win:           (-----------------------------------]
```

## Template form 3 — a decision diagram (branches explicit)

```
[Start: evaluate one patient]
        |
        v
  <criterion A met?>
   | yes        | no
   v            v
 [INCLUDE]   <criterion B met?>
              | yes        | no
              v            v
           [INCLUDE]   [EXCLUDE]
```

## Template form 4 — a counting/temporal criterion (e.g. "≥3 events, span > 30 days")

```
weeks:   |-- 1 --|-- 2 --|-- 3 --|-- 4 --|-- 5 --|-- 6 --|
days:        1       8      15      22      29      36
events:    [o]     [o]    [o]     [o]     [o]     [x]
            ^                                       ^
            |________ span(last − first) = 35 d ____|   > 30 d  → criterion met
```

Read the **whole** observed block at once. "≥3" is a floor, not an exact triplet; "span > 1
month" is last-minus-first, **not** a required gap between consecutive events.

See `phenotyping-examples.md` and `indicator-scenarios.md` for fully worked cases, and the
agent-runnable `checklists.md` before coding.
