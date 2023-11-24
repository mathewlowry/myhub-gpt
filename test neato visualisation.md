#### test neato visualisation
![[neato-example.png]]
The above image was drawn in http://magjac.com/graphviz-visual-editor/ using the following code:
``` 
graph ER {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	layout=neato
	node [shape=box]; theme1; "theme 2"; theme3;
	node [shape=ellipse]; resource1; "resource 2"; "resource 3"; "resource 4"; 

	theme1 -- resource1;
	theme1 -- "resource 2";
	theme3 -- "resource 2";
	theme1 -- "resource 3";
	"theme 2" -- "resource 2";
	"theme 2" -- "resource 4";	
	
	theme3 -- resource1;
	theme3 -- "resource 4";	
	
	label = "\n\nEntity Relation Diagram\ndrawn by NEATO";
	fontsize=20;
} ``` 
```
