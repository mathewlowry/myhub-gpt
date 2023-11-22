# Prompt 2c themes & resources visualised

## Goal

Create a visualisation of how the various resources in a collection relate to the themes identified within them, using http://magjac.com/graphviz-visual-editor/ visualisation. 

## History

In [[experiments 2 3 4 - visualisers]] I started with v1, below. In the resulting conversation (see [[c-3_allnotes-response-p-2c-a]]) chatgpt helped me improve the code, resulting in v2, which I tested on the same content. 

## v2
You are a superb organiser and classifier of ideas and content. First identify and briefly summarise the top themes running through some or all of the resources I'm providing you. The most important themes are relevant to the most resources, and should be listed first. Please ensure each theme's title is short, and only provide at most 7 themes to start with. Then ask me if I want you to remove some themes, or generate more, or rename some. Here are the resources: PROMPT.

Now generate  Graphviz code for a compact Entity-Relation Data Model concept map of these resources and themes, where each resources is connected to the relevant themes. The nodes representing the themes should be grey-filled ellipses, with their size adjusted according to their importance: the most important theme should have the largest node, and a correspondingly larger font size. The map's nodes representing the resources should all be yellow-filled rectangles. All Resource titles should fit snugly within their nodes' boundaries. Their texts should ideally all have the same font size, unless the title is very long. As the Resources' titles are often long, include labels for each Resource. Each Resource's label should be the same as the Resource's title, except that you should insert a linebreak ("\n") just before any hyphens, or just after any commas or full stops, and remove any reference to the publisher. If there are no such punctuation marks, insert a linebreak ("\n") after every 4 or 5 words. Remove any line breaks at the end of the Resource labels.

Reduce node separation to make the concept map compact, but avoid overlaps.

I will show you an example of some code for a concept map visualising 4 resources and three themes: 
graph ER {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	layout=neato
	edge [penwidth=1.5];
	overlap=false;
	nodesep=0.1; // Reduced node separation
	ranksep=0.5; // Reduced rank separation
	// Themes with labels and fontsize
	"Theme 1 title" [width=3, height=2, style=filled, fillcolor=lightgrey];
	"Theme 2 title" [width=1.5, height=1, style=filled, fillcolor=lightgrey];
	"Theme 3 title" [width=2, height=1, style=filled, fillcolor=lightgrey];
	// Resources with labels and adjusted width and height
	  "Resource 1 Title needs a linebreak" [shape=box, style=filled, fillcolor=yellow, label="Resource Title 1 \n needs a linebreak", width=2, height=0.8, fontsize=10];
	"Resource 2 Title is very long and so has two linebreaks, a bigger box and a smaller font - New York Times" [shape=box, style=filled, fillcolor=yellow, label="Resource 2 Title is very long \n and so has two linebreaks, a bigger \n box and a smaller font", width=2.5, height=1, fontsize=9];
	"Resource 3 Title is shorter - Nieman Lab" [shape=box, style=filled, fillcolor=yellow, label="Resource 3 Title is short", width=1.5, height=0.8, fontsize=10];
	"Resource 4 Title has - a hyphen" [shape=box, style=filled, fillcolor=yellow, label="Resource 4 Title has \n - a hyphen", width=2, height=1, fontsize=10];

"Theme 1 title" --  "Resource 1 Title needs a linebreak"
"Theme 1 title" -- "Resource 2 Title is very long and so has two linebreaks, a bigger box and a smaller font - New York Times" 
"Theme 1 title" --  "Resource 4 Title has - a hyphen"
"Theme 2 title" --  "Resource 4 Title has - a hyphen"
"Theme 3 title" --  "Resource 3 Title is shorter - Nieman Lab"
"Theme 3 title" --   "Resource 1 Title needs a linebreak"

}

Now provide the same sort of code for the resources and themes we developed earlier.

## v1
You are a superb organiser and classifier of ideas and content. First identify and briefly summarise the top themes running through some or all of the resources I'm providing you. The most important themes are relevant to the most resources, and should be listed first. Please ensure each theme's title is short, and only provide at most 7 themes to start with. Then ask me if I want you to remove some themes, or generate more, or rename some. Here are the resources: PROMPT.

Now you are going to generate the Graphviz code for a Entity-Relation Data Model concept map of these resources and themes, where each resources is connected to the relevant themes. The map's nodes representing the resources should all be squares and have the same size. The nodes representing the themes should be ellipses, and sized according to their importance: the most important theme should have the largest node. 

I will show you an example of some code for a concept map visualising 4 resources and three themes: 
graph ER {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	layout=neato
	node [shape=box]; theme1; "theme 2"; theme3;
	node [shape=ellipse]; resource1; "resource 2"; "resource 3"; "resource 4"; 

	theme1 -- resource1;
	theme1 -- "resource 2";
    theme1 -- "resource 3";
	theme3 -- "resource 2";	
	"theme 2" -- "resource 2";
	theme3 -- resource1;
	theme3 -- "resource 4";	
	"theme 2" -- "resource 4";		
	label = "\n\A concept map\of your resources by theme";
	fontsize=20;
}

Now provide the same sort of code for the resources and themes, using the resource titles and the themes.