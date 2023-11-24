# Experiments 2 - 4: analysis

See [[experiments 2 3 4 - visualisers]]

## Early experiments: 2-3
These were early experiments, before I had really thought through what I was testing, and it shows - for example:

* Collection 2 had 420 resources in it: when I tried feeding all the notes into ChatGPT manually to create the "AllNotes" version of the collection, ChatGPT told me it was too long; chances are the S-0 summaries were too. 
* I only use Summariser 0
 
Nevertheless, I'm analysing here their results to better design experiment 4. 

### Experiment 2
The single most used tag in the collection was psychology (68 resources), yet this was not mentioned as a theme or subtheme. This may be because there was too much content for ChatGPT to consume, of course.

What of the Experiment 2 mindmap?
[[c-2-s-0-response-p2-mindmap.jpeg]] 
While ChatGPT identified 8 toplevel themes, the mindmap only displays 4. Not good.
### Experiment 3
Did we do better with a collection of only 10 resources? 

Even with only 10 resources, it's a lot of work for me to evaluate the appropriateness of all 6 themes and 27 subthemes ChatGPT found within them (see [[c-3_s-0-response-p-2]]. At first glance the 6 themes look right, but a moment's thought and research reveals:

* themes like "The brain's decision-making processes and susceptibility to misinformation" and "The importance of understanding cognitive biases and psychological factors in information processing" are pretty much saying the same thing
* for the subtheme "Predictive coding and interpretation of sensory information", only one item in the collection mentioned "Predictive coding", and none of them mentioned "interpretation of sensory information"
* for the subtheme "Reconstruction of memories and misattribution of information" I found no mention of "Reconstruction", although I found one (again, just one) mention of "misattribution" 

Moreover, when I asked it to identify subthemes which appear in more than one theme, it started making things up: the subtheme "Impact of media literacy education and fact-checking efforts" does *not* appear in the theme of "the need for effective communication, dialogue, and understanding in addressing misinformation and promoting accurate information", simply because that theme does not exist.

The mindmap on the other hand, is a lot better than in Experiment 2. 

[[c-3-s-0-response-p2-mindmap.png]]

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
In [[c-3_allnotes-response-p-2c-a]] I started with **"version 1" of Prompt2c**, trying to get a useful visualisation of the same content ([[c-3_allnotes]]) using Graphviz. It wasn't great to say the least ([[c-3_allnotes-response-p-2c-1.png]]), so the conversation continued as I tried tweaking node size, shape and colour; introduced line breaks into the texts so they'd fit inside the nodes; and tried to make the whole thing more compact.

Near the end I made the most progress by simply telling ChatGPT what I wanted, but the struggles beforehand taught me a lot about Graphviz. It will be interesting to see whether in the future I'll simply default to "ask ChatGPT" *without* all that the struggle... and learning.

Once I had something looking OK ([[c-3_allnotes-response-p-2c-12.png]]) I asked my last question of the conversation: "compose a prompt combining these characteristics so that I can generate concept maps like this quicker".

#### Prompt2c - version 2
I incorporated everything I learnt from  [[c-3_allnotes-response-p-2c-a]] into **"version 2"** of Prompt2c, which I tested in [[c-3_allnotes-response-p-2c-b]], generating for the first time something that looks somewhat useful:

![[c-3_allnotes-response-p-2c-b.jpeg]]

At last something that I can actually look at and assess: is it accurate, or provocative, or both? Most importantly, is it useful?