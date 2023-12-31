# Prompt 2e - framework
## Goal

Given a set of elements, usually composing a strategy, or set of themes emerging from content analysis, provide Graphviz visualisation code for a framework, showing labelled interrelationships.

## Prompt

I want Graphviz code for a compact Entity-Relation Data Model concept map representing *insert content purpose here*. This is composed of *XX* elements - please use Graphviz to visualise how these elements would work together.

All elements' titles should fit snugly within their nodes' boundaries, and ideally all have the same font size. If a title is long, include a label for the node. Each label should be the same as the title, except that you should insert a linebreak ("\n") just before any hyphens, or just after any commas or full stops. If there are no such punctuation marks, insert a linebreak ("\n") after every 4 or 5 words. Remove any line breaks at the end of the labels.

All edges connecting two elements should have arrowheads and a label to explain the relationship between the elements. Wherever you use an arrowhead, use the following syntax: "element 1" -- "element 2" [label="edge label", dir=forward];

Here are the elements I want to visualise: CONTEXT

