# Experiments 2 - 4: analysis

(*This is a permanent version of this page. The latest version of this page can be found under Revision Notes, at the end.*)

See [[experiments 2 3 4 - visualisers]]

## Early experiments: 2-3
These were early experiments, before I had really thought through what I was testing, and it shows - for example:

* Collection 2 had 420 resources in it: when I tried feeding all the notes into ChatGPT manually to create the "AllNotes" version of the collection, ChatGPT told me it was too long; chances are the S-0 summaries were too. 
* I only use Summariser 0
 
Nevertheless, I'm analysing here their results to better design experiment 4. 

### Experiment 2
The single most used tag in the collection was psychology (68 resources), yet this was not mentioned as a theme or subtheme. This may be because there was too much content for ChatGPT to consume, of course.

What of the Experiment 2 mindmap: **c-2-s-0-response-p2-mindmap.jpeg**? [[C-2-S-0-response-p2-mindmap1.jpeg]] 

While ChatGPT identified 8 toplevel themes, the mindmap only displays 4. Not good!
### Experiment 3
Did we do better with a collection of only 10 resources? 

Even with only 10 resources, it's a lot of work for me to evaluate the appropriateness of all 6 themes and 27 subthemes ChatGPT found within them (see [[c-3_s-0-response-p-2]]. At first glance the 6 themes look right, but a moment's thought and research reveals:

* themes like "The brain's decision-making processes and susceptibility to misinformation" and "The importance of understanding cognitive biases and psychological factors in information processing" are pretty much saying the same thing
* for the subtheme "Predictive coding and interpretation of sensory information", only one item in the collection mentioned "Predictive coding", and none of them mentioned "interpretation of sensory information"
* for the subtheme "Reconstruction of memories and misattribution of information" I found no mention of "Reconstruction", although I found one (again, just one) mention of "misattribution" 

Moreover, when I asked it to identify subthemes which appear in more than one theme, it started making things up: the subtheme "Impact of media literacy education and fact-checking efforts" does *not* appear in the theme of "the need for effective communication, dialogue, and understanding in addressing misinformation and promoting accurate information", simply because that theme does not exist.

The mindmap **([[C-3-S-0-response-p2-mindmap2.png]])** on the other hand, is a lot better than in Experiment 2: [[C-3-S-0-response-p2-mindmap2.png]]. 

All top-level themes are present and it's easier to read. But some subthemes are missing:

* The use of explicit warnings and counterarguments to inoculate against misinformation 
* Exposing individuals to a little bit of science denial to counter science denial  
* Discrepancy between elite media commentators and grassroots groups/independent media outlets  
* Distracting focus from systemic threats and the problem of "fake news"  
* Finding ways to discuss politically polarizing information without challenging worldviews or forcing action
* Debunking the myth of online echo chambers  
* Changing buttons from "like" to "agree," "disagree," "suspect," and "trust"

Remark: 5 of these 7 subthemes were the last subtheme listed under their theme. 

Also, while ChatGPT identified "Difficulty in changing beliefs and susceptibility to ideologically motivated cognition" as belonging in two themes, on the mindmap it appears to be linked to five - almost all of the 7 themes. 

### Summary
Using S-0 and Prompt 2, ChatGPT invented themes that were not there and ignored themes that were, and then misrepresented its (wrong) findings when visualising them.

## Experiment 4 (underway)

Experiment 4 is an evolution of Experiments 2 & 3 in that the same collection and summariser was used, and one of the end goals is a visualisation of a Collection's main themes.

### New goal
However, I'm aiming for a different goal, reflecting the problems discovered earlier:

* Hallucinations
	* In all experiments, ChatGPT hallucinates *credibly* - while it makes stuff up, it's believable stuff. 
	* Moreover, the hallucinations took some finding: I had to dig back into the original texts to spot where it made stuff up
* If [Charts can lie](https://albertocairo.com/), ChatGPT visualisations are **magician-level misleading**
	* Visualisations (almost) always generate a "Wow" factor, and hide the data behind it. This can blind the user to problems in  data or presentation method
	* So while ChatGPT's hallucinations are a major problem at any time, they're doubly so when they generate visualisations
* As is so often the case with knowledge visualisations, the initial Wow I got from viewing the vislualisations in Experiments 2 & 3 was  followed by a "So What?". What use are they, particularly when you have to double check everything for hallucinations? 
* And while on the subject, what use are they even if they *don't* hallucinate? After all, a min dmap's centralised focus shows a central node connecting to themes, which connected to subthemes. **The resources are not actually shown.**

So rather than trying to get an accurate visualisation of a Collection, I'm now more interested in getting a *provocative* one - something that will make me think by spotting potential new connections, even if those connections were not themselves present in the collection.

For this, a different mindmap is required, showing both the articles and the themes. 
### Prompt2b
Hence [[prompt 2b - themes visualised]]. However:

* I fed precisely the same prompt and collection to ChatGPT and got two completely different responses - see the themes identified by ChatGPT in [[c-3_allnotes-response-p-2b-1]] and  [[c-3_allnotes-response-p-2b-2]]
* Moreover, Mermaid doesnt seem able to create a concept map which is *not* a centralised mindmap. 

### Prompt2c for a new visualisation engine 
So I turned to a new mapping tool ([Graphviz](https://graphviz.org/Gallery/neato/ER.html)) and its 
[[test neato visualisation]], and a new prompt ([[prompt 2c - themes and resources visualised]]) to take advantage of it.   

#### Prompt2c - version 1: learning graphviz
In [[c-3_allnotes-response-p-2c]] I started with **"version 1" of Prompt2c**, trying to get a useful visualisation of the same content ([[c-3_allnotes]]) using Graphviz. The result wasn't great to say the least (**c-3_allnotes-response-p-2c-a-1.png**): 

[[c-3_allnotes-response-p-2c-1.png]] 

The conversation therefore continued as I tried tweaking node size, shape and colour; introduced line breaks into the texts so they'd fit inside the nodes; and tried to make the whole thing more compact.

Near the end I made the most progress by simply telling ChatGPT what I wanted, but the struggles beforehand taught me a lot about Graphviz. It will be interesting to see whether in the future I'll simply default to "ask ChatGPT" *without* all that the struggle... and learning.

Eventually I had something (**c-3_allnotes-response-p-2c-a-12.png**) that I can actually make sense of: [[c-3_allnotes-response-p-2c-12.png]] 
#### Prompt2c - version 2
So I asked my last question of the conversation: "compose a prompt combining these characteristics so that I can generate concept maps like this quicker". I then took that, incorporated everything I learnt from [[c-3_allnotes-response-p-2c]], and created **"version 2"** of [[prompt 2c - themes and resources visualised|Prompt2c]]. 

This I then tested *using the same collection* to create [[c-3_allnotes-response-p-2d]], resulting in the **c-3_allnotes-response-p-2c-b.jpeg** concept map: [[c-3_allnotes-response-p-2d-1.jpeg]].

##### Different themes & interconnection density

Although the content analysed in the collection is identical and the prompts very similar, the resulting concept maps are very different, with far more interconnections in the concept map resulting from the earlier conversation (2c-a-12) than in  (2c-b), when I tried to distil everything into a single prompt:

* in 2c-b, the average article is linked to 1 theme, while in 2c-a-12, the figure is 1.7, with one theme (*Misinformation and Cognitive Biases*) ("Several resources discuss the phenomenon of fake news, misinformation, and their impact on society, examining how cognitive biases play a role in the spread of false information and its consequences. This theme encompasses both the nature of misinformation and the cognitive processes that influence its reception and propagation") connected to 5 articles.
	* note that the *Misinformation and Cognitive Biases* theme is the one ChatGPT created after I asked it to combine two themes. 
	* However I also had ChatGPT merge two themes in 2c-b, creating *Confirmation Bias and Cognitive Influences* ("Merging the influence of personal biases, identity, and various cognitive biases in shaping our belief systems and decision-making processes"). This theme, however, is not more central than anything else in 2c-b.
* interesting edge case: 
	* in 2c-b ChatGPT correctly placed the "100 articles on Fake news" article off to the side, disconnected, as my notes on it were almost empty ("A library, organised by topic") as it was my own post, which I tend to only describe, not annotate. 
	* in 2c-a-12, however, this article is linked to the Media Literacy theme.

One obvious possible reason for the difference in connection density is the **difference in themes**. The two experiments show - not for the first time - that when asked to identify themes in the same content, ChatGPT will identify different themes each time. 

However it is also possible that the key driver here is the *length* of the conversations: 2c-a-12 was the result of an 18-response conversation as I wrestled with graphviz, whereas 2c-b had only 3 responses. It doesn't necessarily make sense - the content, after all, is the same - but ChatGPT often doesn't.
##### Abbreviated titles

Examining the graphs I noticed that 2c-a-12 has abbreviated resource titles. At a late stage of the conversation in [[c-3_allnotes-response-p-2c]] I asked it to "make the entire thing more compact", and I see now that ChatGPT turned "I read 100-and-counting articles on Fake News so you don’t have to" into "Reading 100+ Articles on Fake News". 

This didn't happen in [[c-3_allnotes-response-p-2d]], as the prompt didn't give ChatGPT much leeway, simply asking it to "Reduce node separation to make the concept map compact".

##### What's useful?

I find the figures constantly forcing me to ask questions like *why is article X not connected to Theme Y, when article Z is*?  For example:

* in 2c-b: Why is *How Your Brain Decides Without You* ***not*** linked to *Confirmation Bias and Cognitive Influences?*
* in 2c-a-12: Why is *Why facts dont change our minds* not connected to *Communication Strategies*?

But these are not the best questions. They come from comparing just resource and theme *titles*, while the links themselves come from ChatGPT's underlying analysis of my notes rather than the full resource. Even without hallucinations, in other words, they're not that informative.

Rather than "*is this correct*", the question should be "*what does that make me think of?*" 

**And there is a quantitative difference here between the 2 concept maps.** 2c-b is so sparse I nothing interesting jumps out to grab my attention, whereas the centrality of the *Misinformation and Cognitive Biases* theme in 2c-a-12 (linked to 5 resources) gives me something to work with - for example:

* what do the 3 resources relevant to Communication Strategies say when developing a communication strategy to counter disinformation? Focus specifically on where they agree and disagree.
* how would you rearrange this picture - without changing the contents - so that it presents a framework for understanding political polarisation and misinformation? I want to see a clear "cause and effect" movement from left to right, showing how the different phenomena interact to give us the world we see today. Include and identify solutions in one part of the framework if relevant and available
* Develop the theme of "Media literacy" into an overview of the four articles linked to it, with a particular focus on how media literacy either helps cause and/or solve the issues set out in "vaccination standoffs"
* Suggest between 5 and 10 feasible ways the knowledge and ideas set out in these articles could help combat misinformation about the European Union

##### Other ideas

* finalise prompt2c: get the  connection density seen in 2c-a-12 from a single prompt
* continue 2c-a-12 conversation based on the concept map artefact: how does a conversation between me and a visualisation look like?
* include tags in resource nodes? One line theme summaries in theme nodes?
* visit resource URLs and recalculate
	* combine original resource content with my notes
	* give my notes 4x weight
	* generate your own tags, compare with mine, suggest missing 
	* check token limit


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- version control
    - this is version: 1
    - here is the current version: [[experiments 2 3 4 _ analysis]]
    - previous version: n/a
