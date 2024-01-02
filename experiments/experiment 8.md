# experiment 8

Like [[experiment 7]], here I'm riffing off a second extract from a #ZNLive interview I did with ZN  (see the [full interview on linkedin](https://www.linkedin.com/events/7138431781808107520/)).

One of my main goals was to see how much difference there is in the quality of responses between:

* a conversation using the current  [[pilot MyHub ChatGPT integration]], with the inbuilt "Summariser 0" 
* using the full notes.

Unfortunately, the collection I chose was too long for the "full notes" approach, so I used only the best resources. Still makes for an interesting comparison.

## Files

* [a 2m07 chat on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7140976711302545408/) on alternative social media and their implications for communication strategies. 
* **Collection 8**: there are actually 2 collections in this experiment:
	* Collection 8-1 (URL): [everything tagged #fediverse](https://myhub.ai/@mathewlowry/?tags=fediverse&types=like&types=do&types=think&timeframe=anytime&quality=all)(42 resources), processed via Summariser 0 using [[pilot MyHub ChatGPT integration]]
	* [[C-8-2-allnotes]]: as the entire notes of all 42 resources was too long for ChatGPT's context window to even summarise them, this collection was created by putting the rss feed of [ the 17 *best* resources tagged #fediverse](https://myhub.ai/@mathewlowry/?quality=best&types=like&types=do&types=think&tags=fediverse&timeframe=anytime) through [[rss to clean notes prompt]].
* prompt: a custom prompt: "I am interested in the possibilities offered by the "fediverse" - open, decentralised social media networks. I will give you some resources, I want you to suggest ways that organisations can use these networks to build online communities on their own websites, deeply interconnected with the wider Fediverse. Here are the resources:"
* **response**s:  
	* feeding C-8-1 directly into ChatGPT integration gave [[C-8-1-S-0-response]] 
	* feeding C-8-2 back into ChatGPT with similar questions gave [[C-8-2-allnotes-response]]
* **analysis**: *full analysis to be done*, here are some bullets as I read both responses side-by-side:
	* in both cases, ChatGPT's initial response was pretty beside the point, so I used my followup to refocus, and used an old technique of mine to get clients to "get concrete" about what it is they want to achieve from their website ("Please write the website's "About this site" page, including several FAQs to guide new visitors"). While the followups were almost identical, they were customised to reflect the initial responses: C-8-1 focused on the "stream/garden" metaphor, for example, while C-8-2 preferred 'Online Parks'.
	* Their "About pages" were equally bland, although C-8-2 at least came up with a name for the site ("GreenFieldsEU")
	* The first 3 FAQs were pretty identical, while the last 2-3 diverged. None were badly written, and make a convincing case for their platforms. I can easily imagine this sort of content appearing relatively convincing in, say, a tender document
	* I then asked a series of more and more specific questions, to force ChatGPT away from making vague statements. In [[C-8-1-S-0-response]] ChatGPT pushed the gardening metaphor amusingly far ("Planting Seeds", "Growing and Tending", "Weeding and Pruning", etc.), while [[C-8-2-allnotes-response]] was more ambitious for the site, including the full kitchen sink of functionalities, echoing suggestions I made to the EU's CORDIS site around 10 years ago.
	* I then asked to dig into the Fediverse/Community integration, asking ChatGPT to explain how and what would happen in three different scenarios.  [[C-8-2-allnotes-response]] was far more concrete, offering single-sign-on authentication, direct integration, user preferences for sharing, etc.
	* All in all, both responses make a convincing case, but as always need to be checked for hallucinations by a well-qualified software engineer