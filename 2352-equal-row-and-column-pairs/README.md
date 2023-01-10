<h2><a href="https://leetcode.com/problems/equal-row-and-column-pairs/">2352. Equal Row and Column Pairs</a></h2><h3>Medium</h3><hr><div style="user-select: text;"><p style="user-select: text;">Given a <strong style="user-select: text;">0-indexed</strong> <code style="user-select: text;">n x n</code> integer matrix <code style="user-select: text;">grid</code>, <em style="user-select: text;">return the number of pairs </em><code style="user-select: text;">(r<sub style="user-select: text;">i</sub>, c<sub style="user-select: text;">j</sub>)</code><em style="user-select: text;"> such that row </em><code style="user-select: text;">r<sub style="user-select: text;">i</sub></code><em style="user-select: text;"> and column </em><code style="user-select: text;">c<sub style="user-select: text;">j</sub></code><em style="user-select: text;"> are equal</em>.</p>

<p style="user-select: text;">A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).</p>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg" style="width: 150px; height: 153px; user-select: text;">
<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> grid = [[3,2,1],[1,7,6],[2,7,7]]
<strong style="user-select: text;">Output:</strong> 1
<strong style="user-select: text;">Explanation:</strong> There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
</pre>

<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg" style="width: 200px; height: 209px; user-select: text;">
<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
<strong style="user-select: text;">Output:</strong> 3
<strong style="user-select: text;">Explanation:</strong> There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
</pre>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong style="user-select: text;">Constraints:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">n == grid.length == grid[i].length</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= n &lt;= 200</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= grid[i][j] &lt;= 10<sup style="user-select: text;">5</sup></code></li>
</ul>
</div>