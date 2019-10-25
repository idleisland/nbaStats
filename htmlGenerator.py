from scrape import *

f = open('statpage.html','w')
message = '''
<html>
<head><link rel="stylesheet" href="style.css"></head>
<body><div class="topnav">
  <a class="active" href="#home">Home</a>
  <a href="#about">About</a>
  <div class="search-container">
    <form action="/action_page.php">
      <input type="text" placeholder="Search.." name="search">
      <button type="submit">Submit</button>
    </form>
  </div>
</div></body>
</html>
'''

f.write(message)
f.close()

stats = setUp()
print(getPlayerLine('Stephen Curry', stats))
