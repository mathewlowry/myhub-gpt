# Prompt 2c themes & resources visualised

## Goal

Create a visualisation of how the various resources in a collection relate to the themes identified within them, using http://magjac.com/graphviz-visual-editor/ visualisation. 

## History

* [[experiments 2 3 4 - visualisers]]: I started with v1, below. In the resulting conversation (see [[c-3_allnotes-response-p-2c-1]]) chatgpt helped me improve the code, resulting in v2, which I tested on the same content:  
* 

## v1
### Prompt 
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