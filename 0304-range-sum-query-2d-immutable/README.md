<h2><a href="https://leetcode.com/problems/range-sum-query-2d-immutable/">304. Range Sum Query 2D - Immutable</a></h2><h3>Medium</h3><hr><div style="user-select: text;"><p style="user-select: text;">Given a 2D matrix <code style="user-select: text;">matrix</code>, handle multiple queries of the following type:</p>

<ul style="user-select: text;">
	<li style="user-select: text;">Calculate the <strong style="user-select: text;">sum</strong> of the elements of <code style="user-select: text;">matrix</code> inside the rectangle defined by its <strong style="user-select: text;">upper left corner</strong> <code style="user-select: text;">(row1, col1)</code> and <strong style="user-select: text;">lower right corner</strong> <code style="user-select: text;">(row2, col2)</code>.</li>
</ul>

<p style="user-select: text;">Implement the <code style="user-select: text;">NumMatrix</code> class:</p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code style="user-select: text;">matrix</code>.</li>
	<li style="user-select: text;"><code style="user-select: text;">int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the <strong style="user-select: text;">sum</strong> of the elements of <code style="user-select: text;">matrix</code> inside the rectangle defined by its <strong style="user-select: text;">upper left corner</strong> <code style="user-select: text;">(row1, col1)</code> and <strong style="user-select: text;">lower right corner</strong> <code style="user-select: text;">(row2, col2)</code>.</li>
</ul>

<p style="user-select: text;">You must design an algorithm where <code style="user-select: text;">sumRegion</code> works on <code style="user-select: text;">O(1)</code> time complexity.</p>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg" style="width: 415px; height: 415px; user-select: text;">
<pre style="user-select: text;"><strong style="user-select: text;">Input</strong>
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
<strong style="user-select: text;">Output</strong>
[null, 8, 11, 12]

<strong style="user-select: text;">Explanation</strong>
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
</pre>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong style="user-select: text;">Constraints:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">m == matrix.length</code></li>
	<li style="user-select: text;"><code style="user-select: text;">n == matrix[i].length</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= m, n &lt;= 200</code></li>
	<li style="user-select: text;"><code style="user-select: text;">-10<sup style="user-select: text;">4</sup> &lt;= matrix[i][j] &lt;= 10<sup style="user-select: text;">4</sup></code></li>
	<li style="user-select: text;"><code style="user-select: text;">0 &lt;= row1 &lt;= row2 &lt; m</code></li>
	<li style="user-select: text;"><code style="user-select: text;">0 &lt;= col1 &lt;= col2 &lt; n</code></li>
	<li style="user-select: text;">At most <code style="user-select: text;">10<sup style="user-select: text;">4</sup></code> calls will be made to <code style="user-select: text;">sumRegion</code>.</li>
</ul>
</div>