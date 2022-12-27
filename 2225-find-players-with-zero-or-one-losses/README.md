<h2><a href="https://leetcode.com/problems/find-players-with-zero-or-one-losses/">2225. Find Players With Zero or One Losses</a></h2><h3>Medium</h3><hr><div style="user-select: text;"><p style="user-select: text;">You are given an integer array <code style="user-select: text;">matches</code> where <code style="user-select: text;">matches[i] = [winner<sub style="user-select: text;">i</sub>, loser<sub style="user-select: text;">i</sub>]</code> indicates that the player <code style="user-select: text;">winner<sub style="user-select: text;">i</sub></code> defeated player <code style="user-select: text;">loser<sub style="user-select: text;">i</sub></code> in a match.</p>

<p style="user-select: text;">Return <em style="user-select: text;">a list </em><code style="user-select: text;">answer</code><em style="user-select: text;"> of size </em><code style="user-select: text;">2</code><em style="user-select: text;"> where:</em></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">answer[0]</code> is a list of all players that have <strong style="user-select: text;">not</strong> lost any matches.</li>
	<li style="user-select: text;"><code style="user-select: text;">answer[1]</code> is a list of all players that have lost exactly <strong style="user-select: text;">one</strong> match.</li>
</ul>

<p style="user-select: text;">The values in the two lists should be returned in <strong style="user-select: text;">increasing</strong> order.</p>

<p style="user-select: text;"><strong style="user-select: text;">Note:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;">You should only consider the players that have played <strong style="user-select: text;">at least one</strong> match.</li>
	<li style="user-select: text;">The testcases will be generated such that <strong style="user-select: text;">no</strong> two matches will have the <strong style="user-select: text;">same</strong> outcome.</li>
</ul>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 1:</strong></p>

<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
<strong style="user-select: text;">Output:</strong> [[1,2,10],[4,5,7,8]]
<strong style="user-select: text;">Explanation:</strong>
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
</pre>

<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 2:</strong></p>

<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> matches = [[2,3],[1,3],[5,4],[6,4]]
<strong style="user-select: text;">Output:</strong> [[1,2,5,6],[]]
<strong style="user-select: text;">Explanation:</strong>
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
</pre>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong style="user-select: text;">Constraints:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= matches.length &lt;= 10<sup style="user-select: text;">5</sup></code></li>
	<li style="user-select: text;"><code style="user-select: text;">matches[i].length == 2</code></li>
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= winner<sub style="user-select: text;">i</sub>, loser<sub style="user-select: text;">i</sub> &lt;= 10<sup style="user-select: text;">5</sup></code></li>
	<li style="user-select: text;"><code style="user-select: text;">winner<sub style="user-select: text;">i</sub> != loser<sub style="user-select: text;">i</sub></code></li>
	<li style="user-select: text;">All <code style="user-select: text;">matches[i]</code> are <strong style="user-select: text;">unique</strong>.</li>
</ul>
</div>