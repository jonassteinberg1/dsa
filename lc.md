* **Time-box each attempt:** Work 20–30 minutes; if there’s no new progress after ~10 minutes, take one tiny hint; if still stuck by ~30, read the solution, close it, and immediately re-implement from scratch. When studying the solution it is critical to understand why the solution works, as well as the code.
* **Retrieval over review:** Always solve from a blank start without looking; name the pattern before you begin and state the invariant you’ll rely on.
* **One-line note per problem:** Record just (a) the pattern, (b) the key invariant/idea, (c) edge cases, and (d) one sentence on what you missed.
* **Spaced re-dos:** Re-implement from scratch the next day (D+1) and again a week later (D+7); if you can do it cleanly, retire it.
* **Keep a small “canon”:** Maintain ~20–30 representative problems; only add a new one if it teaches a genuinely new pattern or trick.
* **Daily cadence:** 2–3 new problems with the loop above, plus 2–4 quick re-dos (these should be fast).
* **Interleave patterns:** Mix related categories (e.g., trees, graphs, two-pointers) and vary constraints/edge cases to generalize.
* **Handle outliers separately:** Keep one exemplar for rare “trick” problems (like LC 2040), refresh briefly, and don’t stockpile near-duplicates.

Use a **canon filter**: only add a problem if it gives you a *new invariant/trick*, plugs a *recurring weakness*, or is *high-yield* (common across variants).

######################
#    Two Pointers    #
######################

* two pointers

1. Sorted 2-sum (opposite ends): Maintain i<j and the target lies within [i, j]; if sum<target advance i, else decrement j.
   Two Sum II – Input Array Is Sorted (167), Sum of Square Numbers (633), Two Sum Less Than K (1099)

2. 3-sum / k-sum after sort: Maintain fixed prefix + 2-sum window with duplicates skipped; move the inner pointer that steers the sum toward target.
   3Sum (15), 3Sum Closest (16), 4Sum (18)

3. Palindrome check (filtered): Maintain all characters outside (i, j) already match; keep i ≤ j; skip non-alphanumerics as needed.
   Valid Palindrome (125), Valid Palindrome II (680), Reverse Only Letters (917)

4. Container With Most Water: Maintain best area so far and the rule that only moving the shorter line can increase area.
   Container With Most Water (11), Trapping Rain Water (42)

5. Remove duplicates in sorted array: Maintain nums[:slow] is deduplicated while fast scans; when nums[fast] ≠ nums[slow−1], copy to slow.
   Remove Duplicates from Sorted Array (26), Remove Duplicates from Sorted Array II (80)

6. Squares of a sorted array: Maintain ans filled from the end; place the larger absolute value next and move that side.
   Squares of a Sorted Array (977), Sort Transformed Array (360)

7. Merge two sorted arrays/lists: Maintain merged[:k] is globally sorted; always take the smaller head.
   Merge Sorted Array (88), Merge Two Sorted Lists (21), Interval List Intersections (986)

8. Intersection of two sorted arrays: Maintain processed prefixes fully compared; advance the pointer with the smaller value; emit on equality.
   Intersection of Two Arrays (349), Intersection of Two Arrays II (350)

9. Backspace string compare (from ends): Maintain i and j at the next valid characters after accounting for backspaces.
   Backspace String Compare (844), Removing Stars From a String (2390)

10. Is subsequence: Maintain s[:i] matched within t[:j]; advance j each step and i only on a match.
    Is Subsequence (392), Number of Matching Subsequences (792), Minimum Window Subsequence (727)

11. Partition by predicate (e.g., move zeros): Maintain left partition satisfies the predicate’s negation and right is unprocessed; swap/advance to grow the correct partition.
    Move Zeroes (283), Remove Element (27), Sort Array By Parity (905)


########################
#    Sliding Window    #
########################

* Sliding Window

1. No-repeat window (Longest Substring Without Repeating): Maintain all character counts ≤ 1 in [l, r); on duplicate, move l past the last occurrence until the invariant holds.
   Longest Substring Without Repeating Characters (3), Maximum Erasure Value (1695), Substrings of Size Three with Distinct Characters (1876)

2. At most K distinct (Fruit Into Baskets): Maintain distinctCount ≤ K using a freq map; shrink from l while distinctCount > K.
   Fruit Into Baskets (904), Longest Substring with At Most K Distinct Characters (340), Longest Substring with At Most Two Distinct Characters (159)

3. Replacement ≤ k (Longest Repeating Character Replacement): Maintain windowSize − maxFreqInWindow ≤ k; if violated, advance l to restore.
   Longest Repeating Character Replacement (424), Maximize the Confusion of an Exam (2024)

4. Fixed-size anagram scan (Find All Anagrams / Permutation in String): For window length len(p), maintain mismatchCount == 0 between window counts and target counts; slide by updating counts for the outgoing and incoming chars.
   Find All Anagrams in a String (438), Permutation in String (567)

5. Minimum Window Substring: Maintain have[c] ≥ need[c] for all required chars to mark a valid window; while valid, move l to minimize until the first deficit appears.
   Minimum Window Substring (76), Number of Substrings Containing All Three Characters (1358)

6. Fixed-length stats (Max Avg / Max Sum of size k): Maintain runningSum = sum(nums[l..r)) for window size k via +nums[r] − nums[l]; each step preserves the exact sum for the current window.
   Maximum Average Subarray I (643), Maximum Number of Vowels in a Substring of Given Length (1456), Maximum Sum of Distinct Subarrays With Length K (2461)

7. Positive numbers, min length with sum ≥ target: With nonnegative nums, maintain sum(window) ≥ target ⇒ try to shrink; otherwise expand.
   Minimum Size Subarray Sum (209), Minimum Operations to Reduce X to Zero (1658)

8. Subarray product < k (positives): Maintain prod(window) < k; when prod ≥ k, divide by nums[l] and advance l until the invariant holds.
   Subarray Product Less Than K (713), Count Subarrays With Score Less Than K (2302)

9. Binary/0-1 window with flips (Longest Ones after K flips): Maintain zerosInWindow ≤ K; if exceeded, move l right, decrementing zerosInWindow on each zero passed.
   Max Consecutive Ones III (1004), Longest Subarray of 1’s After Deleting One Element (1493), Max Consecutive Ones II (487)

10. Two-strings cover check (covering all chars of pattern): Maintain missing = totalNeeded − satisfied, and missing == 0 iff the window covers the pattern; sliding updates missing in O(1) per move.
    Permutation in String (567), Find All Anagrams in a String (438), Minimum Window Substring (76)


#######################
#    Binary Search    #
#######################

* binary search

1. Lower bound / first true: Maintain answer ∈ [lo, hi); predicate is monotone; if pred(mid) is true set hi=mid else lo=mid+1; returns first index where pred is true.
   Search Insert Position (35), Find First and Last Position of Element in Sorted Array — first index via lower_bound (34), Find Right Interval (436)

2. Upper bound / first greater: Maintain answer ∈ [lo, hi); use predicate (a[mid] > target); if true set hi=mid else lo=mid+1; last occurrence = upper_bound−1.
   Find First and Last Position of Element in Sorted Array — last index via upper_bound−1 (34), Find Smallest Letter Greater Than Target (744), Heaters — locate nearest heater via upper_bound/lower_bound (475)

3. First bad version (good/bad split): Maintain lo is last known good, hi is first known bad; shrink with mid so that invariant (good…bad) never breaks; hi ends at first bad.
   First Bad Version (278), Kth Missing Positive Number — first index where missing≥k (1539)

4. Search in rotated sorted array: Maintain target ∈ [lo, hi] if present and **one half is sorted**; shrink to the half that is both sorted and contains target (else take the other half).
   Search in Rotated Sorted Array (33), Search in Rotated Sorted Array II (81)

5. Minimum in rotated array: Maintain the minimum lies in [lo, hi] and compare a[mid] vs a[hi]; if a[mid] > a[hi], min ∈ (mid+1..hi], else min ∈ [lo..mid]; hi ends at min.
   Find Minimum in Rotated Sorted Array (153), Find Minimum in Rotated Sorted Array II (154)

6. Peak / unimodal (mountain) array: Maintain there exists a peak in [lo, hi]; compare nums[mid] to neighbor to move toward the uphill side; the chosen half still contains a peak.
   Find Peak Element (162), Peak Index in a Mountain Array (852), Find in Mountain Array (1095)

7. Binary search on answer (parametric): Maintain infeasible/feasible boundary on value domain; mid is feasible ⇒ hi=mid, else lo=mid+1; returns minimal feasible value.
   Koko Eating Bananas (875), Capacity To Ship Packages Within D Days (1011), Minimum Number of Days to Make m Bouquets (1482), Magnetic Force Between Two Balls (1552)

8. k-th smallest in sorted matrix (value-domain): Maintain domain [minVal, maxVal] and **count(≤mid)** is monotone in mid; shrink by comparing count to k.
   Kth Smallest Element in a Sorted Matrix (378), Kth Smallest Number in Multiplication Table (668), Find K-th Smallest Pair Distance (719)

9. Median of two sorted arrays (partition): Maintain partitions i,j with i+j=(m+n+1)//2 and ensure maxLeftA ≤ minRightB and maxLeftB ≤ minRightA; binary search i until both inequalities hold.
   Median of Two Sorted Arrays (4), (Generalized follow-up) Find K-th in Two Sorted Arrays — same partition method applied to k

10. Real-valued search (e.g., sqrt): Maintain interval [lo, hi] with monotone f; shrink by mid while preserving f(lo)≤target≤f(hi) (or vice versa) and stop when hi−lo ≤ ε.
    Sqrt(x) (69), Minimize Max Distance to Gas Station (774)

################
#    Stacks    #
################

* stacks

1. Valid parentheses: Stack holds unmatched opens for the processed prefix and never goes negative; empty stack at end ⇒ valid.
   Valid Parentheses (20), Minimum Remove to Make Valid Parentheses (1249), Remove Outermost Parentheses (1021)

2. Min Stack: Each push stores (val, currentMin) or a parallel min-stack so top’s min equals the minimum of all elements in the main stack.
   Min Stack (155), Min Stack — LCCI 03.02

3. Next Greater Element: Maintain a monotonically decreasing stack of indices; when current value exceeds stack top’s value, pop and assign its next greater.
   Next Greater Element I (496), Next Greater Element II (503), Next Greater Node in Linked List (1019)

4. Daily Temperatures / Stock Span: Monotonically decreasing stack of indices; popping continues until the stack’s top is strictly greater, yielding wait/span lengths.
   Daily Temperatures (739), Online Stock Span (901)

5. Largest Rectangle in Histogram: Monotonically increasing stack of bar indices; on a shorter bar (or sentinel), pop to compute areas with width spanning to the new stack top.
   Largest Rectangle in Histogram (84), Maximal Rectangle (85)

6. Evaluate RPN: Operand stack where each operator pops two operands (second popped is left), pushes the result; stack reflects partial expression value at each step.
   Evaluate Reverse Polish Notation (150), Design an Expression Tree With Evaluate Function (1628)

7. Basic Calculator (with parentheses): Number stack and sign/operator handling maintain that the sum of the stack equals the value of the processed prefix under current sign context.
   Basic Calculator (224), Basic Calculator II (227), Basic Calculator III (772)

8. Remove Duplicate Letters / Smallest Subsequence: Monotonic lexicographic stack with inStack flags; while top > current and top appears later, pop to keep minimal sequence with all letters.
   Remove Duplicate Letters (316), Smallest Subsequence of Distinct Characters (1081)

9. Decode String k[...]: Two stacks (counts, strings) maintain current repeat multiplier and accumulated string; on ‘]’ pop and append repeated block to the previous frame.
   Decode String (394), Number of Atoms (726)

10. Asteroid Collision: Stack of right-moving asteroids; when a left-mover arrives, repeatedly resolve collisions with the top until no opposing pair remains, leaving only stable survivors.
    Asteroid Collision (735), Count Collisions on a Road (2211)


##############
#    Heaps   #
##############

* Heaps

1. Kth largest via min-heap: Maintain a min-heap of size ≤ k containing the k largest seen; any element outside has value ≤ heap[0].
   Kth Largest Element in an Array (215), Kth Largest Element in a Stream (703)

2. Top-K frequent elements/words: Maintain a min-heap of size ≤ k keyed by frequency (and tie-breaks for words); any item outside has freq ≤ heap min.
   Top K Frequent Elements (347), Top K Frequent Words (692), Sort Characters By Frequency (451)

3. K closest points: Maintain a max-heap of size ≤ k keyed by distance; any point outside has distance ≥ heap max.
   K Closest Points to Origin (973), Find K Closest Elements (658)

4. Merge k sorted lists/arrays: Maintain a min-heap of current heads (one per list); popping yields the next output in global order, then push that list’s next node.
   Merge k Sorted Lists (23), Kth Smallest Element in a Sorted Matrix — k-way merge by rows (378)

5. Smallest range covering k lists: Maintain a min-heap of current heads plus the current maximum among them; [min(heap), currentMax] always covers one from each list, advance the list that owned the min.
   Smallest Range Covering Elements from K Lists (632), Minimum Deviation in Array — analogous heap+extreme tracking to shrink range (1675)

6. Median of data stream (two heaps): Maintain max-heap left and min-heap right with all left ≤ all right and |sizes| ≤ 1; median is top(s); re-balance after inserts.
   Find Median from Data Stream (295), Sliding Window Median — same two-heap core without deletions yet (480)

7. Sliding window median (dual heap with lazy deletion): Maintain the same two-heap partition plus delayed-deletion maps; remove outdated elements only when they surface at heap tops while keeping sizes balanced.
   Sliding Window Median (480), Finding MK Average — sliding window with heap partitions and lazy removals (1825)

8. Reorganize string / task scheduler with cooldown: Maintain a max-heap of available counts and a hold/cooldown queue; never pick the same item twice in a row and only reinsert when ready time passes.
   Reorganize String (767), Task Scheduler (621), Rearrange Barcodes (1054)

9. IPO (maximize capital): Maintain a min-heap of projects by required capital and a max-heap of feasible projects by profit; move all affordable into the max-heap, pick the highest profit, update capital, repeat up to k.
   IPO / Find Maximized Capital (502), Most Profit Assigning Work — sort by difficulty and push feasible jobs into a max-heap (826), Maximum Performance of a Team — maintain a min-heap to keep best k by quality while scanning (1383)

10. K pairs with smallest sums: Maintain a min-heap of frontier pairs (smallest unseen sums) and a visited set; popping (i,j) pushes its next neighbors while preserving global ascending order of sums.
    Find K Pairs with Smallest Sums (373), Find the Kth Smallest Sum of a Matrix With Sorted Rows (1439)

###################
#    Intervals    #
###################

* intervals

1. Merge Intervals: After sorting by start, maintain a current merged [s,e] that covers all processed intervals; if next.start ≤ e, set e = max(e, next.end), else output [s,e] and start a new block.
   Merge Intervals (56), Add Bold Tag in String — merge overlapping matches (616)

2. Insert Interval: Sweep existing intervals; those ending before new.start are output unchanged, those starting after new.end come after; all overlapping ones are absorbed into new = [min, max], preserving that left/right sides remain untouched.
   Insert Interval (57), Range Module — add/remove/merge intervals (715)

3. Interval Intersections (two lists): With pointers i,j on sorted lists, emit overlap when max(a[i].start, b[j].start) ≤ min(a[i].end, b[j].end); advance the one with the smaller end so no intersection is skipped.
   Interval List Intersections (986), Meeting Scheduler — intersect availability slots (1229)

4. Meeting Rooms I (can attend all): Sort starts and ends separately; maintain active = starts_seen − ends_seen and ensure active ≤ 1 at every step.
   Meeting Rooms (252), Non-overlapping Intervals — feasibility is “no overlaps” (435)

5. Meeting Rooms II (min rooms): Min-heap of end times for active meetings; heap holds exactly the meetings in progress, so heap size = rooms needed; pop while heap_min ≤ current start, then push current end.
   Meeting Rooms II (253), My Calendar III — maximum concurrent bookings (732)

6. Non-overlapping Intervals / Erase Overlap: Greedy by earliest finish; maintain the end of the last kept interval, and on overlap keep the one with the smaller end (minimizes future conflicts) while counting removals.
   Non-overlapping Intervals (435), Remove Covered Intervals (1288)

7. Minimum Arrows to Burst Balloons: Sort by end; maintain current arrow at `end_curr`; if next.start ≤ end_curr it’s covered, else shoot a new arrow and set end_curr = next.end.
   Minimum Number of Arrows to Burst Balloons (452), Set Intersection Size At Least Two — choose minimum points to hit all intervals (757)

8. Car Pooling / Calendar Sweep: Maintain a difference map of events (+passengers at start, −passengers at end) and a running sum over time that must never exceed capacity.
   Car Pooling (1094), Corporate Flight Bookings — range additions + prefix sums (1109)

9. Employee Free Time: After merging all busy intervals across employees (via sort or k-way heap), maintain `cur_end` of the merged busy block; any gap where next.start > cur_end is shared free time, then update cur_end = max(cur_end, next.end).
   Employee Free Time (759), Meeting Scheduler — find common slot via advancing the earlier end (1229)

10. My Calendar I/II/III (booking): Maintain an ordered map of boundary deltas and a running active count; validity requires active ≤ 1 (I) or ≤ 2 (II), while III returns the maximum active seen during the sweep.
    My Calendar I (729), My Calendar II (731), My Calendar III (732)

11. Minimum to Add/Remove to Cover Line (covering intervals): Greedy by earliest finishing coverage; maintain the furthest covered point and choose the interval that extends coverage the most among those starting ≤ current point.
    Video Stitching (1024), Minimum Number of Taps to Open to Water a Garden (1326)


#######################
#    Prefix/Suffix    #
#######################

1. Range sum query (immutable): Build prefixSum with prefixSum[0]=0; invariant: sum(l..r)=prefixSum[r+1]−prefixSum[l] remains valid for all queries.
   Range Sum Query – Immutable (303), XOR Queries of a Subarray (1310)

2. Subarray sum equals K: Maintain a map of seen prefix sums; at index i, #subarrays ending at i with sum K equals count[prefixSum[i]−K].
   Subarray Sum Equals K (560), Binary Subarrays With Sum (930), Count Number of Nice Subarrays (1248)

3. Continuous subarray sum multiple of k: Track first index for each prefixSum%k; if the same remainder reappears with gap ≥2, the in-between sum is a multiple of k.
   Continuous Subarray Sum (523), Subarray Sums Divisible by K (974)

4. Balanced subarray (equal 0/1): Treat 0 as −1; invariant: longest subarray with sum 0 found by storing first index of each prefix sum.
   Contiguous Array (525), Find the Longest Substring Containing Vowels in Even Counts (1371)

5. Shortest subarray with sum ≥ K: Maintain a **monotonic increasing deque of prefix sums**; while currPS−deque.frontPS ≥ K, update answer and pop front; pop back while currPS ≤ backPS.
   Shortest Subarray with Sum at Least K (862), Constrained Subsequence Sum (1425)

6. Product of array except self: left[i]=∏A[0..i−1]; sweep from right with rightProduct; invariant: ans[i]=left[i]·rightProduct after each step (O(1) extra space ignoring output).
   Product of Array Except Self (238), Product of the Last K Numbers (1352)

7. Trapping rain water (prefix/suffix maxima): Precompute leftMax[i], rightMax[i]; invariant: water at i = max(0, min(leftMax[i], rightMax[i])−height[i]).
   Trapping Rain Water (42), Trapping Rain Water II (407)

8. 2D prefix sums (range sum query): ps2D[r+1][c+1] stores sum of rectangle (0,0)→(r,c); invariant: sum of any sub-rectangle via inclusion–exclusion of four ps2D entries.
   Range Sum Query 2D – Immutable (304), Matrix Block Sum (1314), Kth Largest XOR Coordinate Value (1738)

9. Submatrix sum equals target: Fix top/bottom rows, collapse to 1D column sums, then apply “subarray sum equals K” on the collapsed array.
   Number of Submatrices That Sum to Target (1074), Max Sum of Rectangle No Larger Than K (363)

10. Pivot index: Maintain leftSum while total is fixed; invariant: at pivot i, leftSum == total − leftSum − nums[i].
    Find Pivot Index (724), Find the Middle Index in Array (1991), Find the Pivot Integer (2485)


###############
#    Trees    #
###############

* Trees

1. DFS traversals: Preorder does work before children; inorder visits left, then node, then right; postorder ensures both subtrees are fully processed before using the node’s result.
   Binary Tree Preorder Traversal (144), Binary Tree Inorder Traversal (94), Binary Tree Postorder Traversal (145)

2. Level-order (BFS): The queue always contains exactly the nodes of the current frontier; popping all of them produces the next level.
   Binary Tree Level Order Traversal (102), Binary Tree Zigzag Level Order Traversal (103), Average of Levels in Binary Tree (637)

3. LCA (postorder combine): Each call returns either the LCA, one target node, or None; if two non-None values arise among (left, right, self-match), this node is the LCA.
   Lowest Common Ancestor of a Binary Tree (236), Lowest Common Ancestor of a Binary Tree II (1644), Lowest Common Ancestor of a Binary Tree IV (1676)
  - dng
  - D+1: 11/04/2025
    - did not make due to submission to SRECON26
    - completing on 11/05/2026
    - was able to recall but doesn't really count because I was using gippity extensively beforehand
    - 11/06/2025
      - had gippity create me an augmenting problem; it came up with one that was a classic LCA problem
        but given targets may or may not exist
    - next step is to have it give me another problem
    - 11/092025
      - had gippity give me another problem: "at least two targets", but was unable to solve
        and still feel I have many definitions it uses to define tree recursion solution
        features to understand
    - 11/10/2025
      - worked on 426 which is inorder sorting of a BST to produce a sorted circular doubly linked list
        - the critical insights are that since the linked list needs to be sorted, and inorder dfs of a bst emits a sorted list, AND each subtree's leftmost and rightmost children are the min and max of that subtree, respectively, if you
          use inorder dfs and make the inorder logic the list linkage, you produce a sorted circular doubly linked list; at the end you finally
          link global minimum (head) and global maximum (tail)
  - D+7: 11/11/2025

  notes:
    - postorder, at least in this case, is recursing root down the tree each time; it seems like
      "root" is staying the same because we're used to seeing the variable name "root", which seems
      static, but in fact the "root" we compare in conditional cases is the parametric root -- so when
      we make recursive calls and pass in root.left and root.right, respectively, we are able to
      compare them as root and root is being reassigned with each recursive call.

4. BST validation (bounds): For every node with value v, the invariant low < v < high holds; recurse left with (low, v) and right with (v, high).
   Validate Binary Search Tree (98), Construct Binary Search Tree from Preorder Traversal — maintain bounds as you consume preorder (1008)

5. Kth smallest in BST (inorder): Inorder traversal yields a strictly increasing sequence; decrement k on each visit and stop when k==0.
   Kth Smallest Element in a BST (230), Binary Search Tree Iterator — inorder generates next-k elements (173)

6. Build tree from preorder + inorder: Preorder’s next element is the root of the current subtree; inorder index splits exact left/right sizes, and indices never overlap across recursive calls.
   Construct Binary Tree from Preorder and Inorder Traversal (105), Construct Binary Tree from Inorder and Postorder Traversal (106)

7. Maximum path sum: Each call returns the max one-side gain (≥0) to parent; a global best tracks leftGain + node + rightGain.
   Binary Tree Maximum Path Sum (124), Maximum Sum BST in Binary Tree — same postorder “gain + global best” idea with BST checks (1373)

8. Diameter of binary tree: Each call returns height=1+max(leftH,rightH); a global best tracks max(best, leftH+rightH).
   Diameter of Binary Tree (543), Longest Univalue Path — identical “return one-side height, track global” pattern (687)

9. Balanced binary tree: Each call returns subtree height or a sentinel (e.g., −1) for unbalanced; once unbalanced is flagged, propagate it upward unchanged.
   Balanced Binary Tree (110), Check Balanced (LCCI 04.04)

10. Invert binary tree: Postorder ensures both children are already inverted when you swap them; after return, the subtree is a mirror of the original.
    Invert Binary Tree (226), Binary Tree Upside Down — pointer flips done bottom-up (156)

11. Root-to-leaf path sum: Maintain runningSum for the current path; at a leaf, runningSum==target implies success, and backtracking restores runningSum.
    Path Sum (112), Path Sum II (113), Sum Root to Leaf Numbers (129)

12. Serialize/deserialize (preorder with nulls): Serialization emits nodes and null markers in a fixed order; deserialization consumes tokens in the same order to reconstruct exactly one tree.
    Serialize and Deserialize Binary Tree (297), Serialize and Deserialize BST — preorder with value bounds (449)

13. Right side view: For DFS, the first node visited at each depth (right-first) becomes the view; for BFS, the last node popped per level is the view.
    Binary Tree Right Side View (199), Find Bottom Left Tree Value — analogous “one visible per level” capture using level order (513)

14. Maximum width: For each level, track (index, node) where indices reflect heap-like positions; width = lastIndex − firstIndex + 1 while indices remain relative within each level.
    Maximum Width of Binary Tree (662), Find Nearest Right Node in Binary Tree — level-indexing/BFS frontier bookkeeping (1602)


################
#    Graphs    #
################

1. BFS shortest path (unweighted): The queue holds the current frontier in nondecreasing distance; when a node is dequeued, its recorded distance is minimal.
   Word Ladder (127), Open the Lock (752), Shortest Path in Binary Matrix (1091)

2. DFS traversal / components: The visited set contains exactly nodes whose exploration has begun or finished; starting DFS from each unvisited node counts components.
   Number of Connected Components in an Undirected Graph (323), Number of Provinces (547), Keys and Rooms (841)

3. Undirected cycle detection: In DFS, if you see a visited neighbor that is not the parent, a cycle exists; otherwise the DFS tree is acyclic.
   Redundant Connection (684), Graph Valid Tree (261), Detect Cycles in 2D Grid (1559)

4. Directed cycle detection: With colors (WHITE/GRAY/BLACK), any edge to a GRAY node indicates a back-edge and thus a cycle; BLACK nodes are fully processed.
   Course Schedule (207), Course Schedule II (210), Minimum Semesters to Complete Courses (1136)

5. Topological sort (Kahn’s): The queue always contains nodes with indegree 0; removing one and decrementing neighbors’ indegrees preserves correctness; processed count == N iff DAG.
   Course Schedule II (210), Alien Dictionary (269), Sort Items by Groups Respecting Dependencies (1203)

6. Topological sort (DFS postorder): When a node finishes (postorder), all its descendants are already placed; reversing finish order yields a valid topo order in a DAG.
   Course Schedule (207), Course Schedule II (210), Alien Dictionary (269)

7. Union–Find (DSU): Parent pointers form disjoint-set forests; find(x) returns a stable representative, and union by rank/size plus path compression keeps trees shallow.
   Accounts Merge (721), Most Stones Removed with Same Row or Column (947), Number of Operations to Make Network Connected (1319)

8. Clone graph: Maintain a bijection map old→new; each original node is cloned exactly once and edges are added as neighbors are discovered.
   Clone Graph (133), Clone Binary Tree With Random Pointer (1485)

9. Grid “islands” flood fill: Visiting a land cell marks its entire connected component; no marked cell is revisited, so each component is counted exactly once.
   Number of Islands (200), Max Area of Island (695), Count Sub Islands (1905)

10. Multi-source BFS (e.g., spread/rotting): The initial queue contains all sources with time 0; the first time a node is reached is its minimal time.
    Rotting Oranges (994), 01 Matrix (542), As Far from Land as Possible (1162)

11. Bipartite check: A valid 2-coloring means no edge connects same-colored nodes; encountering a same-color edge during BFS/DFS proves non-bipartiteness.
    Is Graph Bipartite? (785), Possible Bipartition (886)

12. Dijkstra (nonnegative weights): The node popped from the min-heap has finalized shortest distance; relaxing its edges can only lower tentative distances of neighbors.
    Network Delay Time (743), Path With Minimum Effort (1631), Swim in Rising Water (778)

13. Longest Increasing Path in matrix (DAG + memo): Direct edges from lower to higher values create a DAG; dp[u] = 1 + max(dp[v]) over outgoing edges, memoized so each cell computes once.
    Longest Increasing Path in a Matrix (329), Number of Increasing Paths in a Grid (2328)

######################
#    Backtracking    #
######################

1. Permutations (distinct): Path is a permutation prefix using each element at most once; used[i] guards reuse.
   Permutations (46), Beautiful Arrangement (526)

2. Permutations (with duplicates): Array sorted; at a given depth, skip nums[i] if nums[i]==nums[i-1] and !used[i-1] to avoid duplicate branches.
   Permutations II (47), Letter Tile Possibilities (1079)

3. Combinations (choose k): Path contains elements with strictly increasing indices; next start index ensures no duplicates.
   Combinations (77), Combination Sum III (216)

4. Subsets (power set): Path equals a subset of the processed prefix; include/skip each item while maintaining nondecreasing indices; for duplicates, apply the same skip rule as above.
   Subsets (78), Subsets II (90)

5. Combination Sum (reuse allowed): Maintain sum ≤ target; indices never decrease so reuse is allowed; prune immediately on sum > target.
   Combination Sum (39), Factor Combinations (254)

6. Combination Sum II (no reuse, duplicates present): Sorted input; each index used at most once; skip equal numbers at the same depth to avoid duplicate sets.
   Combination Sum II (40), Combination Sum III (216)

7. Generate Parentheses: Maintain 0 ≤ open ≤ n, 0 ≤ close ≤ open; only add ')' if close < open; complete when length == 2n.
   Generate Parentheses (22), Parenthesis — LCCI 08.09

8. N-Queens: Maintain conflict-free sets for columns and diagonals (col, r−c, r+c); a placement preserves all three invariants; backtrack restores them.
   N-Queens (51), N-Queens II (52)

9. Sudoku Solver: Partial grid always respects row/col/box constraints; choose next empty (often MRV) and try only feasible digits; backtrack reverts constraints.
   Sudoku Solver (37), Valid Sudoku (36)

10. Word Search (board DFS): Path uses each cell at most once (visited); quit early if current character mismatches; for Word Search II, prune by trie prefix absence.
    Word Search (79), Word Search II (212)

11. Palindrome Partitioning: Every chosen segment is a palindrome; advance start index; optional isPal[l][r] precomputed for O(1) checks.
    Palindrome Partitioning (131), Palindrome Partitioning II (132)

12. Partition to K Equal Sum Subsets: Each bucket sum never exceeds target; fill buckets in descending element order; skip identical-empty-bucket symmetry to avoid redundant states.
    Partition to K Equal Sum Subsets (698), Matchsticks to Square (473)

###############
#    Tries    #
###############

1. Basic insert/search: after consuming prefix p, the current node’s subtree corresponds exactly to all words starting with p; a missing edge means no such word/prefix.
   Implement Trie (Prefix Tree) (208), Implement Trie II (Prefix Tree) (1804)

2. Word termination: `isWord` is true only at ends of inserted words, so “art” and “artist” are distinguished by `isWord` on the shorter path.
   Longest Word in Dictionary (720), Implement Trie (Prefix Tree) (208)

3. Wildcard ‘.’ search: DFS maintains that the explored path matches the query prefix; on ‘.’ branch to all children, otherwise follow only the matching edge.
   Design Add and Search Words Data Structure (211), Implement Magic Dictionary (676)

4. Prefix counts / MapSum: each node stores an aggregate (count or sum) of all words in its subtree; updates propagate a delta along the path to preserve totals.
   Map Sum Pairs (677), Implement Trie II (Prefix Tree) (1804)

5. Replace Words: while scanning a sentence word, the first node with `isWord` on its path yields the minimal root; stop immediately to preserve minimality.
   Replace Words (648), Stream of Characters — stop-on-first-match variant via reversed trie (1032)

6. Word Search II (board + trie): backtracking only proceeds while the current path exists in the trie; if no child edge, prune instantly; found words toggle/consume `isWord` to avoid duplicates.
   Word Search II (212), Word Squares — trie-pruned backtracking on prefixes (425)

7. Search Suggestions: after reaching the prefix node, enumerations are produced in lexicographic order (sorted children or ordered traversal) and capped at k suggestions.
   Search Suggestions System (1268), Design Search Autocomplete System (642)

8. Longest Word in Dictionary: traversal only descends through nodes with `isWord == true`; any candidate word has all prefixes present as words.
   Longest Word in Dictionary (720), Longest Word With All Prefixes (1858)

9. Maximum XOR (bitwise trie): at bit b, prefer the opposite-bit child if it exists to maximize XOR; the chosen path length equals the fixed bit-width.
   Maximum XOR of Two Numbers in an Array (421), Maximum XOR With an Element From Array (1707), Count Pairs With XOR in a Range (1803)

10. Palindrome Pairs: reversed-word trie stores indices (and optionally “palindrome remainder” lists); while scanning word w, if remaining suffix is palindrome and node has a word index, that forms a pair.
    Palindrome Pairs (336), Longest Palindrome by Concatenating Two Letter Words — solvable by the same pair-checking idea (2131)

11. Prefix+Suffix Search: encode queries as “suffix#prefix” (single trie) or use two tries; traversal preserves that matches must share the given prefix and suffix simultaneously.
    Prefix and Suffix Search / Word Filter (745), Encrypt and Decrypt Strings — trie-backed dictionary matching for prefix/suffix-like queries (2227)

#############################
#    Dynamic Programming    #
#############################

* Dynamic Programming

1. Fibonacci/Climbing stairs (1D): dp[i] equals the total ways/optimal value up to i, using only dp[i−1], dp[i−2]; each step preserves that all prefixes are solved.
   Climbing Stairs (70), Min Cost Climbing Stairs (746), N-th Tribonacci Number (1137)

2. House Robber (linear): dp[i] = max(dp[i−1], dp[i−2] + val[i]); at i, we either take i and skip i−1 or skip i while preserving optimality for prefix ≤ i.
   House Robber (198), House Robber II (213), Delete and Earn (740)

3. Kadane (max subarray): curr = max(nums[i], curr + nums[i]) and best = max(best, curr); curr always equals the best subarray sum ending at i.
   Maximum Subarray (53), Maximum Sum Circular Subarray (918)

4. 0/1 Knapsack / Subset Sum (no reuse): For weight w descending, dp[w] reflects items considered so far at most once; reverse w iteration preserves non-reuse.
   Partition Equal Subset Sum (416), Ones and Zeroes (474), Last Stone Weight II (1049)

5. Unbounded Knapsack / Coin Change (min coins): For amount a ascending, dp[a] = min(dp[a], 1 + dp[a−coin]); ascending a preserves unlimited reuse.
   Coin Change (322), Perfect Squares (279)

6. Coin Change II (count combinations): For each coin, iterate amounts ascending and accumulate ways; dp[a] counts combinations without order duplication.
   Coin Change II (518), Coin — LCCI 08.11

7. Edit Distance: dp[i][j] is min edits to transform A[:i]→B[:j]; transitions (insert/delete/replace) preserve optimal substructure of shorter prefixes.
   Edit Distance (72), Delete Operation for Two Strings (583), Minimum ASCII Delete Sum for Two Strings (712)

8. Longest Common Subsequence: dp[i][j] = LCS(A[:i], B[:j]); if A[i−1]==B[j−1], extend dp[i−1][j−1], else take max of dp[i−1][j], dp[i][j−1].
   Longest Common Subsequence (1143), Uncrossed Lines (1035), Shortest Common Supersequence (1092)

9. LIS (patience/tails): tails[k] stores the minimum possible tail of an increasing subsequence of length k+1; tails remains sorted, and its length equals LIS.
   Longest Increasing Subsequence (300), Russian Doll Envelopes (354)

10. Grid paths / min path sum: dp[r][c] depends only on solved neighbors (top/left); processing row/column order keeps prerequisites computed.
    Minimum Path Sum (64), Unique Paths (62), Unique Paths II (63)

11. Palindromic substring/subsequence DP: For substrings, dp[l][r] true/optimal only if endpoints match and inner dp[l+1][r−1] holds; compute by increasing length to ensure inner states exist.
    Longest Palindromic Substring (5), Palindromic Substrings (647), Longest Palindromic Subsequence (516)

12. Decode Ways: dp[i] equals ways to decode s[:i]; dp[i] accumulates valid 1-digit and 2-digit extensions, with zeros allowed only in valid “10/20” pairs.
    Decode Ways (91), Decode Ways II (639)

################
#    Greedy    # 
################

1. Jump Game I (reachability): Maintain furthestReach for processed prefix; if i ever exceeds furthestReach, fail, else update furthestReach = max(furthestReach, i + nums[i]).
   Jump Game (55), Jump Game VII (1871)

2. Jump Game II (min jumps): Maintain currentEnd (end of current jump range) and farthest; when i hits currentEnd, take one jump and set currentEnd = farthest.
   Jump Game II (45), Video Stitching (1024), Minimum Number of Taps to Open to Water a Garden (1326)

3. Gas Station: Global sum(gas−cost) must be ≥ 0; maintain running tank from a candidate start and reset start when tank < 0 (discarding impossible prefixes).
   Gas Station (134), Maximum Subarray (53)

4. Candy: Two passes enforce neighbors: left→right ensures ratings[i]>ratings[i−1] ⇒ candies[i]=candies[i−1]+1; right→left ensures the symmetric constraint via max.
   Candy (135), Push Dominoes (838)

5. Partition Labels: Track last occurrence of each char; maintain window [start..end] where end = max(last[c]) over window—when i==end, cut a partition.
   Partition Labels (763), Max Chunks To Make Sorted (769), Max Chunks To Make Sorted II (768)

6. Non-overlapping Intervals (erase overlap): After sorting by end, maintain lastEnd of kept interval; keep an interval iff start ≥ lastEnd, else drop the one with larger end.
   Non-overlapping Intervals (435), Maximum Length of Pair Chain (646)

7. Minimum Arrows to Burst Balloons: Sort by end; maintain current arrow at endCurr covering all with start ≤ endCurr; when start > endCurr, shoot a new arrow and set endCurr = that end.
   Minimum Number of Arrows to Burst Balloons (452), Set Intersection Size At Least Two (757)

8. Assign Cookies: Sort greed and cookies; maintain pointers so each child gets the smallest cookie that satisfies them, maximizing the count satisfied.
   Assign Cookies (455), Boats to Save People (881)

9. Reconstruct Queue by Height: Sort by (height desc, k asc); insert each person at index k—partial queue remains valid for all processed (taller-first) people.
   Queue Reconstruction by Height (406), Create Target Array in the Given Order (1389)

10. Advantage Shuffle: Sort A and B (keep B’s indices); assign largest A that beats current largest B, else sacrifice smallest A; maintains feasibility while minimizing waste.
    Advantage Shuffle (870), DI String Match (942)

11. Task Scheduler (Least Interval): Let maxFreq be the highest task count; minimal time respects lower bound (maxFreq−1)*(n+1)+numMax by greedily spacing max-frequency tasks and filling gaps.
    Task Scheduler (621), Rearrange String k Distance Apart (358), Reorganize String (767)

12. Monotone Increasing Digits: Scan left-to-right; when a digit drops below its left neighbor, decrement the left neighbor and set the suffix to 9s, preserving a maximal valid prefix.
    Monotone Increasing Digits (738), Remove K Digits (402)

###############
#    Canon    #
###############


##################
#    D+1, D+7    #
##################

236: 11/05/2025
236: 11/11/2025
236 Augmentation: 11/07/2025
236 Augmentation: 11/12/2025
426: 11/11/2025
426: 11/18/2025
