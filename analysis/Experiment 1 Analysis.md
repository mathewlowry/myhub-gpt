# MyHub/GPT integration - experiment 1 (newsletter)

**The first results from my series of experiments to identify the most valuable MyHub Agent prompts are promising and confusing in equal measure.**

As explained in [[Introduction]] I'm sharing the results of my research into integrating MyHub.ai with an LLM as they happen. 

## Executive summaries
### My first draft exec summary
*My first exec summary, after doing the analysis manually (below):* 

There was no clear "winner" - evaluated using 8 different parameters, each output had wins for some, losses for others. If I was looking for a first draft I could most efficiently edit into a newsletter, for example, the S-1-150 version was the closest in length and had all links integrated into its body, while the S-0 version highlighted the common themes a little more effectively, and AllNotes gave the least-worst title and article summaries of the least-wrong length.

But most, possibly all, of any efficiency gains from using ChatGPT to write this newsletter could be lost in the necessary accuracy check. While checking the accuracy of each version's thoroughly would take more time than I have, every time I looked I found inaccurate hallucinations, misrepresenting the articles summarised.

Those hallucinations, however, could be valuable if I wasn't trying to write a newsletter summarising 14 articles.

### ChatGPT's exec summary
Then I asked ChatGPT's opinion: "*I will provide you an analysis of an experiment into the best way of using ChatGPT to create a newsletter summarising the content of 14 different articles, You will write an executive summary of the analysis of no longer than 400 words. Here is the original analysis, in markdown format:*"

Its full response is [[Experiment 1 Aanalysis chatgpt execsumm]] (425 words), but the final section is worth embedding here:
![[Experiment 1 Aanalysis chatgpt execsumm#Lessons and Recommendations]]

### Final executive summary
What I wrote initially still stands, but bringing in ChatGPT to help write this executive summary helped me see better what I should be doing in the next experiment(s).

Rather than evaluating different versions and word lengths of S-1 (ie, S-1-250, S-2-100...), I think I'll focus first on varying the prompt: rather than asking for a nice summary of Hubbed resources in newsletter format, I'll explore Prompts which, as ChatGPT puts it, "*Use ChatGPT outputs as idea generators rather than sources of literal truth*".

---
## Outputs being evaluated
Experiment 1's full title is C-1-S-1-150-P-1, so the three outputs to compare are:
- [[C-1-AllNotes-response-P-1]]: what I get back from ChatGPT  
	- when I send it the entirety of the contents of the 14 Hubbed notes in Collection 1 ("[All the Stuff I Like about Everything tagged #creativity & #innovation, Anytime](https://myhub.ai/@mathewlowry/?tags=creativity&types=like&timeframe=anytime&quality=all&tags=innovation)") 
	- and ask [[Prompt 1 - newsletter A]] (500 word editorial summarising the main themes & brief summaries of each article)
- [[C-1-S-0-response-P-1.md]]: what ChatGPT returns when sent "Summariser 0" summaries of the posts in Collection 1, with Prompt 1
- [[C-1-S-1-150-response-P-1.md]]: what ChatGPT returns when sent "Summariser 1" summaries, set to a maximum length of 150 words, of the posts in Collection 1, with Prompt 1.

See [[ChatGPT Experiment log#^56fa46]] for all files, and [[Introduction]] for a full explanation of the experimental method.
## Remarks on the inputs
If you check out the original Collection and input files, you+ll see that for many Notes there wasn't a huge difference between the AllNotes and S-1-150 versons sent to ChatGPT.

That's due to the way I've changed how I Hub resources, creating the notes which are usually summarised before being sent to ChatGPT. For many years many of my Hubbed notes were more like bookmarks, providing a quick summary of why I thought a resource was worth reading, but not summarising what I learnt from it. It was only a few years ago, after reading [Sonke Ahren's "How to write smart notes"](https://www.soenkeahrens.de/de/takesmartnotes), that I more consistently spent more time summarising in my own words what I found valuable in the resources I Hubbed ([example](https://myhub.ai/items/ai-is-life)).

---
And now for some analysis:

Sent the same prompt [[Prompt 1 - newsletter A]], the differences between ChatGPT's proposed newsletters are striking.
## Title and opening drivel
* **title** (winner: AllNotes): personally I find the AllNotes version ("Unveiling the Dynamics of Innovation, Creativity, and Collaboration") as least worse, as the other two had glaring clunkers ("Persistent Efforts", "Diverse Perspectives") which have no place in any title. In any case I'd almost certainly rewrite the title after editing the Editorial, so this is only a minor "win" for AllNotes.
* **opening drivel** (winner: S-1-150): this bullet was going to be "opening paragraph", but in all cases the opening paragraph - so important to an article like this - were great examples of "reversion to the mean", where the mean has been defined by New Grub Street marketing hacks over the last decades of a decaying civilisation. I detest all of them and refuse to pick a "winner", although the S-1-150 version is the one I'd rewrite as it provides more concrete ideas to work with.

## Editorial length (winner: S-1-150)
In none of the cases ChatGPT respected the 500 word limit for the editorial: 
* it came closest with the S-1-150 summaries (576 words long), forgivable
* S-0 summaries generated a 656 word long editorial, reasonably easy to shorten
* but sending ChatGPT the AllNotes input generated an editorial just under 1000 words long - twice the set limit!

WTF, ChatGPT?

## Links in Editorial to articles (winner: S-1-150?) ^4fc4d4
* I started this experiment by sending the S-1-150 summaries to ChatGPT with a simpler version of Prompt 1, which is why the S-1-150 response ([[C-1-S-1-150-response-P-1]]) has two "attempts". When I saw that my first attempt hadn't linked the article titles to their URLs, I replied with: *"You forgot to make the articles link to the provided URLs. Provide the same content but in markdown format, with each article title linked to the URL provided with it"* , creating attempt 2, which has links throughout the editorial, as requested.
* I then included this instruction in Prompt 1 *before* applying it to the other inputs. Despite this, neither included the links in the editorial. Perhaps asking ChatGPT twice simply gets a better result? Something to explore in [[Experiment 2]].

## Editorial Form (winner: S-0)
The AllNotes response is easy to "Fail": it provides 14 (admittedly good) summaries of 14 articles, but draws no links between them, as ChatGPT was specifically instructed. The other two responses did better, providing paragraphs drawing on multiple articles. 

**In S-1-150,** for example, we find 5 paragraphs like this:
* *Central to nurturing creativity is the ability to reframe problems. The article ["Three Ways To Reframe A Problem To Find An Innovative Solution"](http://www.fastcompany.com/3050265/hit-the-ground-running/three-ways-to-reframe-a-problem-to-find-innovative-solution) highlights how adopting different perspectives can lead to breakthrough ideas. This concept is further reinforced in [the article "Ideation: List and Paint your Ideas"](https://medium.com/@krystacurtis/paint-by-idea-81dcd2f5d34e), which encourages the playful and creative generation of ideas. Building on this, ["What I Wish I Knew About Creativity When I Was 20"](https://open.bufferapp.com/creativity-advice/) underscores the significance of collaboration and the confluence of ideas in fostering innovation. Embracing this confluence is [the article "Build a Culture of Innovation: Kill Mediocrity"](http://weblog.mediatemple.net/tips/how-to-build-a-culture-of-innovation-by-killing-mediocrity-1), which advocates for dismantling complacency and hierarchy to create a culture of open idea-sharing.* 

**The S-0 version** does something similar, but covers the ground in 7 sections (and 8o more words). As it gives each section a subtitle, it  highlights the common themes identified, as requested - for example:
* ***Reframing Problems for Innovation**
  Problem-solving lies at the core of innovation. "Three Ways To Reframe A Problem To Find An Innovative Solution" from Fast Company emphasizes the importance of tackling problems from novel angles. Techniques like imagination, creativity, and entrepreneurship are highlighted to transform challenges into opportunities. Similarly, "The Discipline of Creativity" underscores the need to link creative ideas with actionable steps. The proposed integrative process involves understanding problems deeply, generating tangible ideas, and translating them into action.*

Here we are just evaluating the *form*, so S-0's subtitles wins this round.
## Editorial Content 
**This aspect takes the most effort to judge but is, of course, the most important, as when I ask ChatGPT to "*highlight themes common to several articles*" I can't stop it from simply making stuff up.**

For example, consider the above paragraph from the S-1-150 response, starting with "*Central to nurturing creativity*": 
	* [my notes]( https://myhub.ai/items/what-i-wish-i-knew-about-creativity-when-i-was-2) about  "What I Wish I Knew About Creativity When I Was 20" may mention confluence but they do *not* mention collaboration;
	* that's because while [the actual article](https://buffer.com/resources/creativity-advice/) mentions collaboration twice, **in neither case was it saying that collaboration is important to fostering innovation or creativity;**
	* nevertheless, collaboration is introduced by ChatGPT in the S-1-150 summary ("*Creative advice includes valuing persistence and embracing diverse perspectives through collaboration, as confluence of ideas often leads to innovation*")

So while ChatGPT's editorial, based on ChatGPT's summary of an article, says that the article"*underscores the significance of collaboration and the confluence of ideas in fostering innovation*", that idea simply isn't present in the article. **ChatGPT's editorial is false.**

***But is it not also true in a larger sense?*** While the article doesn't say that collaboration helps foster innovation, maybe it could have. After all, ChatGPT's logic(1) is as follows:
* the article says that confluence ("*two things flowing together*") is important to innovation
* one way to make confluence happen is to collaborate with others
* so collaboration is significant to fostering innovation.

(1) Note that I used the word "logic" loosely. ChatGPT did not "think this through", as I just did in the above bullet points. Instead, it connected the concepts "collaborate" with "confluence" because (I assume) these words are well-connected in its training corpus. 

**ChatGPT's hallucination, in other words, was a connection that the author did not make. While that makes it a false summary of the author's work, that doesn't mean that it's wrong as a stand alone statement. But it also doesn't mean that it's right.** 

Lessons: 
* if you're looking for literal truth, doublecheck everything carefully
* doublechecking everything carefully will consume a lot of the time you were probably hoping to save by using an LLM
* so perhaps don't use ChatGPT to generate literal truth - instead, use its outputs (correct or otherwise) as a springboard for your own ideas - to explore in Experiments 2+.

## Article lists
Finally, how did the different inputs affect the quality of the article list, following the Editorial?
### Lengths (winner: AllNotes)
Prompt-1 asked for 80-word summaries of each article:
* S-0: most summaries in the response ranged from 20-50 words, although one was over 100. In total it was only ~4% shorter than the (already very short) S-0 inputs 
* S-1-150: summaries in the response ranged 8-22 words; total length 42% lower than the S-1-150 inputs
* AllNotes: the summaries were almost all identical in length (18-23 words each), some 70% shorter in total than the AllNotes input.

AllNotes' consistency reduces the editorial polishing time, and so wins this particular comparison. But I asked for 80 word summaries, not ~20 word summaries.

### Article list content
This obviously subjective comparison is made more difficult by the above length differences. 

For example, [[C-1-S-0-response-P-1#[The downside of diversity](http //archive.boston.com/news/globe/ideas/articles/2007/08/05/the_downside_of_diversity/?page=full)|the summary of "The downside of diversity" based on the S-0 input]] provides more information, while the [[C-1-S-1-150-response-P-1#^2ca69e|S-1-150]] and [[C-1-AllNotes-response-P-1#^52bbb1|AllNotes]] versions benefit from their pithiness. Which is "best"? 
* Given I wanted summaries of 80, not 18, words in length, S-0 wins by being closer to the target length.
* If I'd valued pithiness, the S-1-150 captures the essence of the article better than the AllNotes version, which misses the "pros and cons" argument entirely, despite being longer and *despite [[C-1-AllNotes-response-P-1#*The downside of diversity*|capturing it perfectly well in its Editorial!]].*

Think about that for a moment: sent Prompt 1 and asked to work with the *shortest* summary (S-O) of my notes about an article, ChatGPT created a richer and longer summary than when it worked from a *longer* summary (S-1-150). Moreover, *both were more accurate than when ChatGPT was working from my raw, **unsummarised** notes.*

Another example: when given the S-0 summary of my notes about ["The idea that creative people are different from everyone else is a myth"](http://timkastelle.org/blog/2013/10/best-organisational-structure-creativity/), ChatGPT gave an accurate summary in the newsletter's article list:
"*The article challenges the myth that creative people are different from others and highlights the organizational structure of the company that invented Gore-Tex, which operates in small teams and has minimal layers of management despite its large size.*""

However, when given S-1-150 and my (very brief) notes in full, ChatGPT invented: neither the article nor my notes mention "diverse perspectives", "collaboration" or "diverse teams", but according to these versions of the newsletter, the article does. 

What do we learn from this? **ChatGPT doesn't always summarise when asked.** The above quote from the article list is 38 words long, and was generated when I asked ChatGPT to summarise the S-0 summary of my notes. But:
* the summary in the article list and the S-0 summary are identical: when sent Prompt 1 and the S-0 summaries, **ChatGPT just reproduced the S-0 summaries in the article list**
	* there were two exceptions: when treating the S-0 summaries of "Build a Culture of Innovation: Kill Mediocrity" and "The Discipline of Creativity", ChatGPT trimmed the last sentence when preparing the article list, despite the fact that both were under half the requested word limit in length
* my notes are *shorter* (31 words) than the S-0 "summary" - when Summariser 0 "summarised" my notes, it **added 22% more words**.

