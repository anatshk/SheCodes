
import re
text="""This http://www.foo.com/gag.txt is a web URL. This other one HTTP://WWW.UPPERCASE.COM is too.
on the other hand httl://www.google.com/index.html and mailto:fooman@foo.com are not.
http://spaz.info/31415.html is quite OK too. http:///www.cnn.com is messed up."""

webURLregex=r"(http|HTTP)://([^\s/]*)" #have to start somewhere
groups = re.findall(webURLregex,text)
print(groups)               #what did you match
thirdGroup=groups[2]       #which group is this one?
output=thirdGroup[1]       #you can do this differently
print(output)