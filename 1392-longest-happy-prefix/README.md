<h2><a href="https://leetcode.com/problems/longest-happy-prefix/">1392. Longest Happy Prefix</a></h2><h3>Hard</h3><hr><div style="user-select: text;"><p style="user-select: text;">A string is called a <strong style="user-select: text;">happy prefix</strong> if is a <strong style="user-select: text;">non-empty</strong> prefix which is also a suffix (excluding itself).</p>

<p style="user-select: text;">Given a string <code style="user-select: text;">s</code>, return <em style="user-select: text;">the <strong style="user-select: text;">longest happy prefix</strong> of</em> <code style="user-select: text;">s</code>. Return an empty string <code style="user-select: text;">""</code> if no such prefix exists.</p>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 1:</strong></p>

<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> s = "level"
<strong style="user-select: text;">Output:</strong> "l"
<strong style="user-select: text;">Explanation:</strong> s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
</pre>

<p style="user-select: text;"><strong class="example" style="user-select: text;">Example 2:</strong></p>

<pre style="user-select: text;"><strong style="user-select: text;">Input:</strong> s = "ababab"
<strong style="user-select: text;">Output:</strong> "abab"
<strong style="user-select: text;">Explanation:</strong> "abab" is the largest prefix which is also suffix. They can overlap in the original string.
</pre>

<p style="user-select: text;">&nbsp;</p>
<p style="user-select: text;"><strong style="user-select: text;">Constraints:</strong></p>

<ul style="user-select: text;">
	<li style="user-select: text;"><code style="user-select: text;">1 &lt;= s.length &lt;= 10<sup style="user-select: text;">5</sup></code></li>
	<li style="user-select: text;"><code style="user-select: text;">s</code> contains only lowercase English letters.</li>
</ul>
</div>