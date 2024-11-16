# AI4Communities: a model for a self-sustaining, user-owned public sphere

**Model collapse may provide the funding for accelerating decentralised collective intelligence. What needs to happen next?** 

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

In my last post I highlighted how the authors of the [model collapse paper](https://www.nature.com/articles/s41586-024-07566-y) in _Nature_ pointed out that in the future any data stemming from “_genuine human interactions … will be increasingly valuable_” for training the next generation of LLMs. Online, there’s nothing more genuinely human than the interactions in a well-managed digital community, so “_after greed and short-sightedness floods the commons with low-grade AI content…_ **_well-managed online communities of actual human beings [may be] the only place able to provide the sort of data tomorrow’s LLMs will need” (_**[How Model Collapse could revive authentic human communities](https://mathewlowry.medium.com/how-model-collapse-could-revive-authentic-human-communities-e723d8048ef3)).

This supports the **AI4Communities** idea, first outlined in [A Minimum Viable Ecosystem for collective intelligence](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4) in January 2023, which envisions tomorrow’s online denizens thriving in a diverse landscape of _“_[**_small is beautiful communities_**_, supported by AIs which the communities themselves own, train and monetise_](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4)_”_, rather than putting up with whatever Meta’s or X’s global, “one size fits all” algorithms inflict on them to turn a profit.

If model collapse has made AI4Communities more feasible, what is it exactly, how do we get there, and who’s building it? But first, why care?

### What is the Cozyweb?

#### Why is Small Beautiful?

According to the [Three Legged Stool manifesto](https://publicinfrastructure.org/2023/03/29/the-three-legged-stool/), **“Very Small Online Platforms (VSOPs)”** are _“social networks created for a very specific purpose, with rules, norms and affordances appropriate to that community”_ ([A social network taxonomy](https://newpublic.substack.com/p/a-social-network-taxonomy)). While they’re obviously playing with the EU’s term for “[Very Large Online Platforms](https://ec.europa.eu/commission/presscorner/detail/en/IP_23_2413)”, they see VSOPs as separate from **federated servers**, which combine small size and large reach thanks to protocols like ActivityPub (the Fediverse), AT Protocol (Bluesky) and Nostr.

**But for the purposes of this post I’ll call them all “cozyweb”,** partly to keep things simple, but mainly because:

- AI4Communities need to works for everyone, because it needs scale — something it currently lacks, as explored below;
- they have something very significant in common: their manageable size and/or federated structure makes it easier for inhabitants to establish and enforce community norms, making community management possible, as _“it’s fundamentally impossible to do good content moderation or conversation at a scale of billions… A town square operates at a certain size, not at a global scale” (_[Could social media support healthy online conversations?](https://www.niemanlab.org/2024/07/could-social-media-support-healthy-online-conversations-new_public-is-working-on-it))

#### Small doesn’t mean insular

Which is not to say they’re isolated: while each cozyweb community has its own content moderation policies tuned to its needs, most can be networked together without sacrificing independence.

So while each cozyweb can be a village — “_small, most people know each other and you all share a common interest in keeping the sidewalks tidy_” — each can build federated roads to many others, including bigger ones “_crowded with people, plenty of them sleazy and more than the occasional sidewalk madman… But you’ll always discover something or someone new there. Every second person’s selling something, but one in 20 is selling what you need. Besides, you’re selling too…_” ([Welcome to the Fediverse, starry-eyed noob](https://mathewlowry.medium.com/welcome-to-the-fediverse-starry-eyed-noob-twittermigration-day-3-57b99350414)).

Just as each Cozyweb community chooses its own “village rules”, with AI4Communities it manages its own AIs to support the community: some help users with content discovery while guarding the village gates against trolls and trash, for example, while others support community moderation and collaboration processes. 

So if small _is_ beautiful, why is everyone trapping each other on a few massive, genuinely awful platforms? 
#### Must small be poor?

Decentralised, federated networks have been around almost as long as Twitter and Facebook (Evan Prodromou’s Identi.ca launched in 2008, while linkbacks, invented to knit blogging conversations together, came much earlier). But although they are growing now, they are tiny compared to the closed gardens of surveillance capitalism, at least partly because — unlike their closed counterparts — they lack a business model, and hence revenue, as I found out the hard way almost a year ago:

> “Social infrastructure needs to deliver content as a basic minimum. And running that infrastructure takes time, money and professionalism” — [All my toots gone](https://mathewlowry.medium.com/all-my-toots-gone-e844f7c5f255)

The Three Legged Stool authors believe “_many VSOPs will likely receive most of their revenue from the communities they serve, similar to how a local newspaper or nonprofit is funded_”, and I hope they’re right. Today, however, only a small fraction of Mastodon users currently donate to cover their server’s costs (anecodotal).

## AI4Communities: when community monetises AI (not vice versa)

**People may pay more for a better experience.** An AI owned by the community, which reflects their preferences and adds value in many ways (as explored below) could provide that experience.

These communities therefore need access to what the Three Legged Stool manifesto calls a “**Friendly Neighborhood Algorithm Store**”.  Many of the AI services available there will support individuals (cf Bluesky users subscribing to custom feeds and block lists) but other services could support communities, and can be configured and fine-tuned by the village to ensure it reflects their interests and preferences.

Moreover, as I [pointed out](https://myhub.ai/items/faq-how-is-myhubai-free-and-without-ads-what-is-your-business-model) in 2020 when I launched myhub.ai, each community could act as a **data union**: rather than just buying or renting an AI to support their community, they could [monetise the resulting algorithm](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b) to at least help cover the costs of running the community. While I shelved this idea when ChatGPT appeared, the model collapse paper now suggests that the **training data** created by well-managed communities could be the new currency of collective intelligence. 

> training data created by well-managed communities could be the new currency of collective intelligence

Ideally, the marketplaces would be able to serve all protocols seamlessly, helping create the scale required. 

**Because scale is currently missing.** The Fediverse has around 12 million active accounts, Bluesky around the same (***check***), with Nostr a very distant third. Most users in these ecosystems are using Twitter and Facebook clones ***(check)***, which consist of sharing very short messages, albeit often with multimedia and/or URLs. 

One key question is therefore: would 20–30 million users, using such superficial applications, create enough high-quality training data?

But before we can address that, we need a framework for understanding what AI services can offer communities on decentralised social networks.

## AI service framework

**What services could these “cozyweb AIs” provide, and within what sort of apps?**
### Content discovery services

**Content discovery is what happens when content you like or needed to see is presented to you.** 

The basic idea is simple: use AI trained by the community to find content of interest to the community, whether the community is connected to the author or not. These “For You” feeds will be driven by **relevance and trust**, as explored earlier:

![[concentric circles.jpg]]
(caption) *Concentric trust circles of collective intelligence, from [Building collective intelligence from social knowledge graphs](https://mathewlowry.medium.com/building-collective-intelligence-from-social-knowledge-graphs-e3a465852e8b)*

So **how is this any different to X, Threads _et al_?** After all, these platforms all have content discovery algorithms. 

Simple: your village’s algorithm works for you, not the platform’s owners and advertisers. 

> your village’s algorithm works for you

Don’t want it to optimise your feed for enragement? Tell it not to. Don’t like engagement bait, NSFW comedy or culture war memes? Tell it so. Only interested in a few topics? Let it know.

This will of course vary from platform to platform:

* This will probably require a lot of work on the Fediverse, but could offer that ecosystem just as much. Moreover, the collective knowledge shared by the village's inhabitants could make good training data for the collecting AI - see [[AI4Communities on the Fediverse]]
* Bluesky already offers the possibility of 3rd party services to provide custom feeds to users, so there are interesting possibilities there, as yet underexploited - see [[AI4Communities on Bluesky]]
* Nostr - tbd


### Content moderation and Governance services

Enforcing any online space’s rules on content moderation is a thankless and sometimes hideous task, so the major platforms have already invested fortunes into AI-supported moderation. Open-source LLMs now make it possible to develop something similar for cozyweb spaces.

Depending on the protocol, these AIs could intervene in many different ways, from nudging members to rephrase a specific post to outright banning another for life. It would also intervene at several stages of content development, from before a member clicks the “Post” button through to the moment a conversation starts overheating.

Most of all, of course, the AI will constantly learn from the village’s inhabitants what they like and dislike.

The key to success will be **effective community co-ownership of the village rulebook** which the AI enforces. After all, in any decentralised network, if you no longer agree with your village’s rules you can move to another one easily, so ensuring everyone has a say in defining its rules is essential for any village to thrive.

> a community working together to train their village AI

This raises the fascinating possibility of a community working together to train their village AI. Obviously, any member would ideally be able to contest decisions — the conversations around these edge cases could then help fine-tune the rulebook. The AI should take an active role in these conversations, effectively being coached by the community on norms and practices. I suspect the coaching will be bidirectional much of the time.

Well-run large communities will therefore develop effective content moderator AIs reflecting the community’s values, attracting more members with matching values. The data used to create these AI will be valuable, as will the AIs themselves.

Again, the details will vary according to the platform:

* If the above content discovery services become possible on the Fediverse, they will almost certainly also provide *external* content moderation services, making sure bad content is not brought into the commuity's instance. *Internally* facing content moderation and governance AIs would focus their attention on the instance's Local feed, making it more valuable, interesting and safer - see  [[AI4Communities on the Fediverse]]
* Bluesky already offers the possibility of 3rd party services to provide labellers, to which users can subscribe. Ideally, labellers could be AI-driven, and trainable by their subscriber - see [[AI4Communities on Bluesky]]
* Nostr - tbd


### Centaur services for individuals...

**Chatting with strangers and making friends on a social media platform is only a small part of collective intelligence. How should AI help members of a cozyweb community be more creative and productive, maximising their human potential?** 

I think everyone is familiar with the idea of the concept of "centaurs" (myhub: [#centaur](https://myhub.ai/@mathewlowry/?tags=centaur&types=like&types=do&types=think&timeframe=anytime&quality=all)), but the key role of "centaur services" is to *avoid* us humans becoming "reverse centaurs" - human beings turned into[ "OK-button-mashing automatons"](https://doctorow.medium.com/what-kind-of-bubble-is-ai-d02040b5573a) by the requirement (often driven by regulation or marketing) to keep a human in the loop.

Research in this field tends to result in prompt libraries and frameworks for using LLMs - for example:

* [AI And The Decline Of Human Intelligence](https://medium.com/the-generator/ai-and-the-decline-of-human-intelligence-eca8d9e651d5) points out that “_Our brain is a muscle; it needs to be exercised_,” which is a problem given how easy it is to outsource our skills to AI. So it provides a number of useful-looking prompt frameworks (Socratic Method, Feynman Method, Debate Partner, etc.) to help you treat AI “_as a tutor or consultant, guiding us like a teacher_”. 
* This echoes [ChatGPT as muse, not oracle](https://www.geoffreylitt.com/2023/02/26/llm-as-muse-not-oracle.html), from February 2023, but still well worth reading.
* [AI as Extraherics: Fostering Higher-order Thinking Skills in Human-AI Interaction](https://arxiv.org/abs/2409.09218) is an academic paper with a similar goal, proposing an AI usage framework called “extraheric AI” which “_fosters users’ higher-order thinking … creativity, critical thinking, and problem-solving… by posing questions or providing alternative perspectives … promoting a balanced partnership between humans and AI_”.

So rather than provide a generic "send this to an LLM" system, as is currently the case on myhub.ai (see [How to chat with ChatGPT about your content](https://myhub.ai/items/how-to-chat-with-chatgpt-about-your-content-v1)) and dozens of other apps, AI services provided to cozyweb communities should provide AI-powered *process agents* which "lift up" our thinking and help us learn, rather than *product agents* which focus on turning us into reverse centaurs, mindlessly OKing whatever product the AI provides.

The content created with the support of these process agents should be a high-quality source of AI training data - after all, the AI knows exactly what was were created by AI, what was created by human inspiration, and what the AI did to help. 

>the AI knows exactly what was created by AI, what was were created by human inspiration, and what the AI did to help. 

How exactly these services would look, of course, would depend on the client application: an AI service supporting users exchanging short status updates will look very different from an integrated thinking and longform publishing tool like myhub.ai in the future.

### ... and collective intelligence

**Things get even more interesting when you create agents to help a community collaborate and produce something together.**

So the above point about client applications becomes central if you want to take things further and co-create something together with a group, Because you have a problem: hardly any social media platform offers integrated collaboration tools (exception: Reddit offers community wikis). So you need to agree, _as a group_, on a collaborative tool everyone is comfortable with (TL:DR; it doesn’t exist for groups larger than 4), and then co-create on one platform while chatting on the other (which, frankly, sucks).

I’m not sure why this is so. Work-oriented collaboration platforms offer reasonably seamless chat and collaboration environments. In the public realm, however, there seems to be a stubborn divide separating wikis and other groupware from blogging and social media.

> A social ecosystem where users can seamlessly collaborate

So picturing how AI services could help social groups collaborate is hamstrung by the lack of existing client apps where such collaboration already takes place. I explored one scenario almost 4 years ago in [Thinking and writing in a decentralised collective intelligence ecosystem](https://mathewlowry.medium.com/thinking-and-writing-in-a-decentralised-collective-intelligence-ecosystem-16dd2b1893cc) , and followed it with [this video](https://www.youtube.com/watch?v=qfYl3SiZJWU), which introduces the idea and then explores massive.wiki, an early example of how the collaborative part of the overall technology stack might look (and the tool I use to manage and publish this content).

However that content was light on details. Some framing ideas on how AI-supported collaboration can be found in [How to Use AI to Build Your Company’s Collective Intelligence](https://hbr.org/2024/10/how-to-use-ai-to-build-your-companys-collective-intelligence), which explores how AI can help “increase the collective intelligence of the entire organization… through boosting collective memory, collective attention, and collective reasoning”. However, this article also identifies some risks: for example, bringing an AI voice assistant into a collaborative effort created **groupthink**, reducing “intellectual diversity … Through a form of a**lgorithmic monoculture**” ([see comments](https://www.linkedin.com/posts/mathewlowry_how-to-use-ai-to-build-your-companys-collective-activity-7254411450264305664-eas9?utm_source=share&utm_medium=member_desktop)).

The AI services marketed to cozyweb communities to support collaboration, in other words, must not only help the individual members boost their creativity, but will also have to reinforce the positive and dampen the negative dynamics of groups. The most successful agents will probably have as many psychologists, facilitation and negotiation experts behind them as data scientists.

Finally, if any collaborative work is to be supported by any group’s AI, the members would obviously need to give their consent. Which in turn means that these collaborations become _another_ source of high-value AI training data. 

## Deeper apps, better data

**For AI4Communities to work we need social apps which people want to use _and_ which generate high-quality training data.** 

One thing that bothers me is that almost everyone on Bluesky, as well as (I think!) most of the users on Nostr and the Fediverse, are using Twitter look-alike apps. 

My gut feeling is that for AI4communities to work in **privacy-first** spaces like these, the apps people use will need to be less superficial to generate higher-quality training data. After all, there’s only so much value in short status updates, and noone's proposing following users around the web, siphoning up their data to sell to marketers as Facebook *et al* do. 

> there’s only so much value in short status updates

This is perhaps why the only example of AI4communities I've come across to date is in the adjacent sector of search - see [[Brave example]]. AI4Communities is the social media equivalent of Brave’s approach to search. Both revolve around **authenticity-driven data quality:**

- People do not actually spend a lot of time browsing junk content, so Brave’s dataset doesn’t have any, and so is of higher quality
- People in well-run communities do not curate, share and collaborate on rubbish content, so the data they create will be valuable, too.

For one example of how that could look, [A Minimum Viable Ecosystem for collective intelligence](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4) suggests combining **publishing tools** (blogs, social posts), **social bookmarking** and **personal knowledge management**, and networking them together across **federated networks**, all supported by your personal AI. 
[![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hhPR3ipH50_ttWR6dCtATA.png)](https://mathewlowry.medium.com/social-knowledge-graphs-for-collective-intelligence-75c436889320)
*(caption) From [Social knowledge graphs for collective intelligence](https://mathewlowry.medium.com/social-knowledge-graphs-for-collective-intelligence-75c436889320) (January 2023)*

Because then your AI will be able to can learn from:

- what you do on your social network(s)
- every article you bookmark or Hub (and so find really, really useful)
- the notes you make about it as you curate it (which tells the AI exactly _what_ you find useful about it)
- everything else (blog posts and professional references, mainly) which you publish alongside them
- and everything else in your private knowledge library you make accessible to it.

That’s a _lot_ of tightly interconnected knowledge, all reflecting your interests and expertise. Any AI sourcing that sort of knowledgebase will perform content discovery superbly well for you. And that AI is also being trained by everyone else in your village, with whom you presumably share some interests and values, and with whom you may also be collaborating (see below). Together, your community will generate extremely valuable AI training data, due to the **authentically human curation and creation** processes involved in making it.

## AI4Communities per protocol

**How would this look on each decentralised social network?** 

Above I've set out a framework for categorising AI services in an AI4Communities ecosystem, but the details of these services will vary on different protocols. This is a feature, not a bug: "protocol competition" might drive innovation and growth in much the same way that platform competition in the telecommunications industry helped accelerate broadband rollout.

--- 

*Subfiles to be developed:*

* [[AI4Communities on the Fediverse]], 
* [[AI4Communities on Bluesky]] 
* [[AI4Communities on Nostr]], *next.*

---
## Conclusions (todo)



---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- 2024-11-15: 
		- moved more content into the subfiles, including a new one ([[Brave example]])
		- reorganised structure: AI service framework
- version control
    - this is version: current
    - this is the current version: [[AI4Communities post]]
    - here is the previous version: [[AI4Communities post v5]]

