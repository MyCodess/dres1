<!--
github-markdown-example-1
see also  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
-->

Headings:
-------------------------------------------------
- Headings (first variation, two levels):

A first-level heading
========================
A second-level heading
--------
________________________________________________________________________________________
- Headings (second variation, up to 6 sub-levels):
# A first-level heading
## A second-level heading
### A third-level heading
#### A 4.-level heading
##### A 5.-level heading
###### A 6.-level heading
________________________________________________________________________________________

formatting charachters/fonts/paragraphs:
-------------------------------------------------
	_______:  formatted chars:
    - **bold-text**
    - *italic-text*
    - ~~strikethrough~~
    - **bold and then _italic_ text**
    - ***All text bold+italic***
    - <sub>subscript text</sub>

--- and the same as unparsed source/code (just indentation): 

    - **bold-text**
    - *italic-text*
    - ~~strikethrough~~
    - **bold and then _italic_ text**
    - ***All text bold+italic***
    - <sub>subscript text</sub>
________________________________________________________________________________________

Quoted text:
-------------------------------------------------
Text that is not a quote

>  Text that is a quote
    and gon on here!

>  and further ...
________________________________________________________________________________________

code formatted:
-------------------------------------------------
inline code as `git commit -a -m`
or as code block:
```
git status
git add
git commit
```

________________________________________________________________________________________
Links:
------------------------------------
- web-links:  This site was built using [GitHub Pages](https://pages.github.com/)
- relative links (own repo):  Links starting with / will be relative to the repository root. You can use all relative link operands, such as ./ and ../.
________________________________________________________________________________________
lists:
------------------------------------
##### --- unordered list:
- preceding one or more lines of text with -, \*, or + , as:
- item
- item
- item
________________________________________________________________________________________
##### --- ordered list:
1. item
2. item
3. item
________________________________________________________________________________________
##### --- nested list:
1. First list item
   - First nested list item
     - Second nested list item
2. First list item
    - First nested list item
    - Second nested list item
________________________________________________________________________________________
##### --- task list:
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
________________________________________________________________________________________

------------------------------------
