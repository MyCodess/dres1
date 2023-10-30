CommonMark example-1
=====================================================

Headings (Style-1, two levels):
-------------------------------------------------

A first-level heading
===================================
A second-level heading
---------------------------
________________________________________________________________________________________


Headings (Style-2):
-------------------------------------------------
# A first-level heading
## A second-level heading
### A third-level heading
#### A 4.-level heading
##### A 5.-level heading
###### A 6.-level heading
________________________________________________________________________________________


Formatting: chars/fonts/..., inline formattings :
------------------------------------------------------------------

--- inline formattings:
- _italic-text_ , *italic-text*
- __bold-text__ , **bold-text**
- ___bold + italic text___  ,  ***bold + italic text***
- __bold and then _italic_ text__  ,  **bold and then *italic* text**
- ~~strikethrough~~
- <sub>subscript text</sub>
- horizontal rule : three or more hyphens (-), asterisks (*), or underscores (_).
- ESC / escaping chars with backslash, as:  \* , \` , \_ , etc.
<!-- CommonMark examples-ref-1 -->

--- inline formattings unparsed/source (as above):

    - _italic-text_ , *italic-text*
    - __bold-text__ , **bold-text**
    - ___bold + italic text___  ,  ***bold + italic text***
    - __bold and then _italic_ text__  ,  **bold and then *italic* text**
    - ~~strikethrough~~
    - <sub>subscript text</sub>
    <!-- CommonMark examples-ref-1 -->

--- **Hard line breaks** (as in html:  BR) :

preserved line-breaks in normal/inline-text-blocks (in code-blocks are line breaks anyway preserved!):\
either two-spaces /OR a backslash `\` at the end of the line, as:

aa bb\
cc dd

aa bb   
cc dd
________________________________________________________________________________________


Blockquotes (Citations) ">" :
-------------------------------------------------
- You represent any blockquote/citation by preceding the first line of the block quote with a greater-than sign or angle bracket (>).

Text that is not a quote

>  Text that is a quote
    and gon on here!

>  and further ...
________________________________________________________________________________________


codes-inline , code-blocks:
-------------------------------------------------
--- **inline code**  with **backtick**  as: `git commit -a -m`

--- **Indented code blocks** :

    code line-1
    code line-2 <...>
    code line-3

- An indented code block is composed of one or more indented chunks separated by blank lines:
- basically: simply indentation, but outside any listings/enumerations/...! so **standalone**-indentation will be parsed as it is (line breaks preserved,...)!

--- **Fenced code blocks** : A code fence is a sequence of at least three consecutive backtick characters (`) or tildes (~):
```
git status
git add
git commit
```

---- **code-blocks** with **syntax highlighting** per lang (GitHub-MD !):
- **code-blocks** with **syntax highlighting** per lang:
- use ```<lang> for highlighting, as:

```javascript
if (isAwesome){
 return true
}
```

________________________________________________________________________________________


Links:
------------------------------------
- web-links:  This site was built using [GitHub Pages](https://pages.github.com/)
- relative links (own repo):  Links starting with / will be relative to the repository root. You can use all relative link operands, such as ./ and ../.
- images-inserting:  ![img1](../images/img1.png)  ##-:NO-space-between-link-parts!
________________________________________________________________________________________


lists:
------------------------------------
##### --- unordered list:
- preceding one or more lines of text with -, \*, or + (but NOT-mixing them!) , as:
- item
- item
- item
________________________________________________________________________________________
##### --- ordered list:
- use just [No.] ... 
- only the FIRST item number is relevant for numbering! subsequent numbers are ignored!, as:
4. item
1. item
1. item
________________________________________________________________________________________
##### --- nested list:
1. First list item
   - First nested list item
     - Second nested list item
2. First list item
    - First nested list item
    - Second nested list item
________________________________________________________________________________________
##### --- task list (GitHub_MD):
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
________________________________________________________________________________________

