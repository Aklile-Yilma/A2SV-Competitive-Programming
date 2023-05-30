<h2><a href="https://leetcode.com/problems/build-a-matrix-with-conditions/">2392. Build a Matrix With Conditions</a></h2><h3>Hard</h3><hr><div style="user-select: text;"><p style="user-select: text;">You are given a <strong style="user-select: text;">positive</strong> integer <code style="user-select: text;">k</code>. You are also given:</p>

<ul style="user-select: text;">
	<li style="user-select: text;">a 2D integer array <code style="user-select: text;">rowConditions</code> of size <code style="user-select: text;">n</code> where <code style="user-select: text;">rowConditions[i] = [above<sub style="user-select: text;">i</sub>, below<sub style="user-select: text;">i</sub>]</code>, and</li>
	<li style="user-select: text;">a 2D integer array <code style="user-select: text;">colConditions</code> of size <code style="user-select: text;">m</code> where <code style="user-select: text;">colConditions[i] = [left<sub style="user-select: text;">i</sub>, right<sub style="user-select: text;">i</sub>]</code>.</li>
</ul>

<p style="user-select: text;">The two arrays contain integers from <code style="user-select: text;">1</code> to <code style="user-select: text;">k</code>.</p>

<p style="user-select: text;">You have to build a <code style="user-select: text;">k x k</code> matrix that contains each of the numbers from <code style="user-select: text;">1</code> to <code style="user-select: text;">k</code> <strong style="user-select: text;">exactly once</strong>. The remaining cells should have the value <code style="user-select: text;">0</code>.</p>

<p style="user-select: text;">The matrix should also satisfy the following conditions:</p>

<ul style="user-select: text;">
	<li style="user-select: text;">The number <code style="user-select: text;">above<sub style="user-select: text;">i</sub></code> should appear in a <strong style="user-select: text;">row</strong> that is strictly <strong style="user-select: text;">above</strong> the row at which the number <code style="user-select: text;">below<sub style="user-select: text;">i</sub></code> appears for all <code style="user-select: text;">i</code> from <code style="user-select: text;">0</code> to <code style="user-select: text;">n - 1</code>.</li>
	<li style="user-select: text;">The number <code style="user-select: text;">left<sub style="user-select: text;">i</sub></code> should appear in a <strong style="user-select: text;">column</strong> that is strictly <strong style="user-select: text;">left</strong> of the column at which the number <code style="user-select: text;">right<sub style="user-select: text;">i</sub></code> appears for all <code style="user-select: text;">i</code> from <code style="user-select: text;">0</code> to <code style="user-select: text;">m - 1</code>.</li>
</ul>

<p style="user-select: text;">Return <em style="user-select: text;"><strong style="user-select: text;">any</strong> matrix that satisfies the conditions</em>. If no answer exists, return an empty matrix.</p>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png" style="width: 211px; height: 211px; user-select: text;">
<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
<strong style="user-select: text;">Output:</strong> [[3,0,0],[0,0,1],[0,2,0]]
<strong style="user-select: text;">Explanation:</strong> The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row <u style="user-select: text;">1</u>, and number 2 is in row <u style="user-select: text;">2</u>, so 1 is above 2 in the matrix.
- Number 3 is in row <u style="user-select: text;">0</u>, and number 2 is in row <u style="user-select: text;">2</u>, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column <u style="user-select: text;">1</u>, and number 1 is in column <u style="user-select: text;">2</u>, so 2 is left of 1 in the matrix.
- Number 3 is in column <u style="user-select: text;">0</u>, and number 2 is in column <u style="user-select: text;">1</u>, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
</pre>

<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 2:</strong></p>

<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
<strong style="user-select: text;">Output:</strong> []
<strong style="user-select: text;">Explanation:</strong> From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
</pre>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong style="user-select: text;">Constraints:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">2 &lt;= k &lt;= 400</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= rowConditions.length, colConditions.length &lt;= 10<sup style="user-select: text;">4</sup></code></li>
	<li style="user-select: text;"><code style="user-select: text;">rowConditions[i].length == colConditions[i].length == 2</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= above<sub style="user-select: text;">i</sub>, below<sub style="user-select: text;">i</sub>, left<sub style="user-select: text;">i</sub>, right<sub style="user-select: text;">i</sub> &lt;= k</code></li>
	<li style="user-select: text;"><code style="user-select: text;">above<sub style="user-select: text;">i</sub> != below<sub style="user-select: text;">i</sub></code></li>
	<li style="user-select: text;"><code style="user-select: text;">left<sub style="user-select: text;">i</sub> != right<sub style="user-select: text;">i</sub></code></li>
</ul>
</div>