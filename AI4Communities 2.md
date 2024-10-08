# AI4Communities: a model for a self-sustaining, user-owned public sphere

**Model collapse may provide the funding for accelerating decentralised collective intelligence. What needs to happen next?** 

*The version you're reading now is an early draft: I am publishing this using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e) - where I publish a string of versions as I develop my thoughts - because I'm hoping constructive reactions to early drafts like these will help me answer my questions and so finish the post. Links to the latest and previous versions, if any, are in the footer.*

In my last post I highlighted how the authors of the [model collapse paper](https://www.nature.com/articles/s41586-024-07566-y) in _Nature_ pointed out that in the future any data stemming from “_genuine human interactions … will be increasingly valuable_” for training the next generation of LLMs. Online, there’s nothing more genuinely human than the interactions in a well-managed digital community, so “_after greed and short-sightedness floods the commons with low-grade AI content…_ **_well-managed online communities of actual human beings [may be] the only place able to provide the sort of data tomorrow’s LLMs will need” (_**[How Model Collapse could revive authentic human communities](https://mathewlowry.medium.com/how-model-collapse-could-revive-authentic-human-communities-e723d8048ef3)).

This supports the **AI4Communities** idea, first outlined in [A Minimum Viable Ecosystem for collective intelligence](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4) in January 2023, which envisions tomorrow’s online denizens thriving in a wide range of _“_[**_small is beautiful communities_**_, supported by AIs which the communities themselves own, train and monetise_](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4)_”_, rather than putting up with whatever Meta’s or X’s global, “one size fits all” algorithms inflict on them to turn a profit.

If model collapse has made AI4Communities more feasible, what is it exactly, how do we get there, and who’s building it? But first, why care?

### What is the Cozyweb, and why is Small Beautiful?

According to the [Three Legged Stool manifesto](https://publicinfrastructure.org/2023/03/29/the-three-legged-stool/), **“Very Small Online Platforms (VSOPs)”** are _“social networks created for a very specific purpose, with rules, norms and affordances appropriate to that community”_ ([A social network taxonomy](https://newpublic.substack.com/p/a-social-network-taxonomy)).

While they’re obviously playing with the EU’s term for “[Very Large Online Platforms](https://ec.europa.eu/commission/presscorner/detail/en/IP_23_2413)”, they see VSOPs as separate from **federated servers**, which combine small size and large reach thanks to protocols like ActivityPub (the Fediverse), AT Protocol (Bluesky) and Nostr.

**But for the purposes of this post I’ll call them all “cozyweb”,** partly to keep things simple, but mainly because:

- AI4Communities need to works for everyone as it needs scale — something it currently lacks, as explored below;
- they have something very singnificant in common: their manageable size and/or federated structure makes it easier for inhabitants to establish and enforce community norms, making community management possible, as _“it’s fundamentally impossible to do good content moderation or conversation at a scale of billions… A town square operates at a certain size, not at a global scale” (_[Could social media support healthy online conversations?](https://www.niemanlab.org/2024/07/could-social-media-support-healthy-online-conversations-new_public-is-working-on-it))

#### Small doesn’t mean insular

Which is not to say they’re isolated: while each cozyweb community has its own content moderation policies tuned to its needs, most can be networked together without sacrificing independence.

So while each cozyweb can be a village — “_small, most people know each other and you all share a common interest in keeping the sidewalks tidy_” — each can build federated roads to many others, including bigger ones “_crowded with people, plenty of them sleazy and more than the occasional sidewalk madman… But you’ll always discover something or someone new there. Every second person’s selling something, but one in 20 is selling what you need. Besides, you’re selling too…_” ([Welcome to the Fediverse, starry-eyed noob](https://mathewlowry.medium.com/welcome-to-the-fediverse-starry-eyed-noob-twittermigration-day-3-57b99350414)).

Just as each Cozyweb community chooses its own “village rules”, with AI4Communities it manages its own AIs to support the community: some help users with content discovery while guarding the village gates against trolls and trash, for example, while others support community moderation and collaboration processes. 

So if small _is_ beautiful, why is everyone trapping each other on a few massive, genuinely awful platforms? 

### Who pays?

#### Must small be poor?

Decentralised, federated networks have been around almost as long as Twitter and Facebook (Evan Prodromou’s Identi.ca launched in 2008, while linkbacks, invented to knit blogging conversations together, came even earlier). But although they are growing now, they haven’t thrived at all compared to their closed counterparts, at least partly because — unlike the closed gardens of surveillance capitalism — they lack a business model and so funding, as I found out the hard way almost a year ago:

> “Social infrastructure needs to deliver content as a basic minimum. And running that infrastructure takes time, money and professionalism” — [All my toots gone](https://mathewlowry.medium.com/all-my-toots-gone-e844f7c5f255)

The Three Legged Stool authors believe “_many VSOPs will likely receive most of their revenue from the communities they serve, similar to how a local newspaper or nonprofit is funded_”, and I hope they’re right. Today, however, only a small fraction of most Mastodon users currently donate to cover their server’s costs (anecodotal).

#### AI4Communities: when community monetises AI (not vice versa)

People may pay more for a better experience. An AI owned by the community, which reflects their preferences and adds value in many ways (as explored below) could provide that experience.

Moreover, as I [pointed out](https://myhub.ai/items/faq-how-is-myhubai-free-and-without-ads-what-is-your-business-model) in 2020 when I launched myhub.ai, each community could act as a **data union**: rather than just paying for an AI to support their community, they could [**own, train and _monetise_ the resulting algorithm**](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b) to at least help cover the costs of running the community.

> training data created by well-managed communities … may be valuable enough to drive growth

These communities therefore need access to what the Three Legged Stool manifesto calls a “**Friendly Neighborhood Algorithm Store**” — a marketplace where cozyweb villages can purchase AI services.

While I shelved this idea when ChatGPT appeared, the model collapse paper now suggests that it’s the **training data** created by well-managed communities, not the actual AIs they use and train, which may be valuable enough to drive growth. 

Forming a data union is just one model: someone else could set up a for-profit instance, a third could let users choose between paying a subscription fee or seeing ads, and so on.

![](https://cdn-images-1.medium.com/max/1600/1*3WBzTFfnFM1bgbiQsV3T3A.png)

Different Fediverse communities offering users different experiences, including AI services sourced from multiple AI marketplaces and individual suppliers.

**The above figure is Fediverse-specific**. Bluesky and Nostr are built differently, so their AI4Communities-powered ecosystems would be structured differently. However both _already_ support algorithm marketplaces, so the underlying idea will be the same. Ideally, the marketplaces would be able to serve all protocols seamlessly, helping create the scale required. 

**Because scale is currently missing.** The Fediverse has around 12 million active accounts, Bluesky a little less, with Nostr a very distant third. Most users in these ecosystems are using Twitter and Facebook clones. 

The key question is therefore: would 20–30 million users, using such superficial applications, create enough high-quality training data?

### Deeper apps, better data

**What social applications will be both popular and generate valuable AI training data?**

For AI4Communities to work we need social apps which people want to use _and_ which generate high-quality training data. So what services could these “cozyweb AIs” provide, and within what apps? 

#### Content discovery services

Content discovery is what happens when content you like or needed to see is presented to you. Bluesky and Nostr already provide algorithmic choice in a decentralised environment, so let’s start with the Fediverse, where users only get three reverse chronological feeds: from everyone you follow; from everyone in your village; and from everyone followed by at least one person in your village. None of these feeds, of course, include content from villages which your village does not federate with (a feature, not a bug).

If AI4Communities is to benefit the Fediverse, each instance must be able to access an AI which can proactively pull in and surface content from across the Fediverse (excluding un-federated servers) of interest to each village inhabitant. These customisable “For You” feeds will be driven by **relevance and trust**, as explored earlier:

[![](https://cdn-images-1.medium.com/max/1600/1*uDYUKBayeAMIplXG1m-4KA.png)](https://mathewlowry.medium.com/building-collective-intelligence-from-social-knowledge-graphs-e3a465852e8b)

Concentric trust circles of collective intelligence, from [Building collective intelligence from social knowledge graphs](https://mathewlowry.medium.com/building-collective-intelligence-from-social-knowledge-graphs-e3a465852e8b)

So **how is this any different to X, Threads _et al_? Simple: your village’s algorithm works for you**, not the platform’s owners and advertisers. Don’t want it to optimise your feed for enragement? Tell it not to. Don’t like engagement bait, NSFW comedy or culture war memes? Tell it so. Only interested in a few topics? Let it know.

> your village’s algorithm works for you

And if your tastes don’t match the village’s, move to another village. Balancing an individual’s feed parameters with the village’s content moderation rulebook should be a fun problem to tackle, but far from insuperable, as each village can find its own balance. Which brings me to…

#### Content moderation and Governance services

Enforcing any online space’s rules on content moderation is a thankless and sometimes hideous task, so the major platforms have already invested fortunes into AI-supported moderation. Open-source LLMs now make it possible to develop something similar for cozyweb spaces.

Each village’s moderation AI could intervene in many different ways, from nudging members to rephrase a specific post to outright banning another for life. It would also intervene at several stages of content development, from before a member clicks the “Post” button through to the moment a conversation starts overheating.

Most of all, of course, the AI will constantly learn from the village’s inhabitants what they like and dislike.

The key to success will be **effective community co-ownership of the village rulebook** which the AI enforces. After all, if you no longer agree with your village’s rules you can move to another one easily, so ensuring everyone has a say in defining its rules is essential for any village to thrive.

> a community working together to train their village AI

This raises the truly fascinating possibility of a community working together to train their village AI. Obviously, any member would ideally be able to contest decisions — the conversations around these edge cases could then help fine-tune the rulebook. The AI should take an active role in these conversations, effectively being coached by the community on norms and practices. I suspect the coaching will be bidirectional much of the time.

Well-run large communities will therefore develop effective content moderator AIs reflecting the community’s values. The data used to create these AI will be valuable, as will the AIs themselves.

#### Collaboration support services

**Chatting with strangers and making friends on a social media platform solves only a small part of the collective intelligence problem.**

If you want to take things further and co-create something together with a group, you have a problem — hardly any social media platform offers integrated collaboration tools (exception: Reddit’s community wikis).

Which is why you need to agree, _as a group_, on a collaborative tool everyone is comfortable with (TL:DR; it doesn’t exist for groups larger than 4), and then co-create on one platform while chatting on the other.

I’m not sure why this is so. Work-oriented collaboration platforms offer reasonably seamless chat and collaboration environments. In the public realm, however, there’s a stubborn divide separating wikis and other groupware from blogging and social media.

I explored one solution almost 4 years ago in [Thinking and writing in a decentralised collective intelligence ecosystem](https://mathewlowry.medium.com/thinking-and-writing-in-a-decentralised-collective-intelligence-ecosystem-16dd2b1893cc). This video introduces the idea before exploring massive.wiki, an early example of what the collaborative part of the overall technology stack might look like:

A social ecosystem where users can seamlessly collaborate is a worthy goal in itself. 

> A social ecosystem where users can seamlessly collaborate

Moreover, that collaborative work can be supported by your village’s AI (given consent from the group), which means these collaborations become _another_ source of high-value AI training data.

#### **Better apps**

As mentioned above, Bluesky and Nostr already offer some elements of the infrastructure required for this: one of my favourite Bluesky feeds, for example, is “[Science](https://bsky.app/profile/bossett.social/feed/for-science)”, developed by [Dani cRabaiotti](https://bsky.app/profile/danirabaiotti.bsky.social), a zoologist and data scientist working at the Zoological Society in London. I’m less familiar with Nostr, but I know that Jack Dorsey, its founder and the guy who launched Bluesky when he ran Twitter, definitely [believes in algorithmic choice](https://cointelegraph.com/magazine/algorithm-choice-can-fix-social-media-but-only-on-decentralized-platforms/).

But Bluesky, as well as most of the Nostr and Fediverse apps, are Twitter look-alikes. My gut feeling is that for AI4communities to work in decentralised, privacy-first spaces like these, the apps people use will need to be less superficial in nature to generate higher-quality training data. After all, there’s only so much value in short status updates.

> there’s only so much value in short status updates

Which brings me back to [A Minimum Viable Ecosystem for collective intelligence](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), which suggests combining **publishing tools** (blogs, social posts), **social bookmarking** and **personal knowledge management**, and networking them together across **federated networks**, all supported by your personal AI. Because then your AI will be able to can learn from:

- what you do on your social network(s)
- every article you bookmark or Hub (and so find really, really useful)
- the notes you make about it as you curate it (which tells the AI exactly _what_ you find useful about it)
- everything else (blog posts and professional references, mainly) which you publish alongside them
- and everything else in your private knowledge library you make accessible to it.

That’s a _lot_ of tightly interconnected knowledge, all reflecting your interests and expertise. Any AI sourcing that sort of knowledgebase will perform content discovery superbly well for you. And that AI is also being trained by everyone else in your village, with whom you presumably share some interests and values. Together the community will generate extremely valuable AI training data, due to the **authentically human curation and creation** processes involved in making it.

#### A Brave, early inspiration

There is already evidence for this strategy in a parallel field. In May 2023 Brave Software, creators of the privacy-first eponymous browser and search engine, released [Brave Search API](https://brave.com/ai/using-brave-search-api). Via this service, AI developers can access the training dataset Brave developed through both Brave Search and their [Web Discovery Project](https://support.brave.com/hc/en-us/articles/4409406835469-What-is-the-Web-Discovery-Project), which allows Brave browser users to contribute anonymous data about the pages they’re actually visiting.

As a result, Brave’s training data “_is much more representative of the Web people actually care about_”, without the huge morass of “_junk sites — spam, dead links, duplicates, and more_” one finds when crawling the Web at large. And that was written _before_ the Web started filling up with AI-generated content, which is even worse for training AI.

#AI4Communities is the social media equivalent of Brave’s approach to search. Both revolve around **authenticity-driven data quality:**

- People do not actually spend a lot of time browsing junk content, so Brave’s dataset doesn’t have any, and so is of higher quality
- People in well-run communities do not curate, share and collaborate on rubbish content, so the data they create will be valuable, too.

### Conclusions

Looking back over this post, I can see that it’s been skewed by my greater familiarity with the Fediverse than Bluesky or Nostr. I’m not an expert in social protocols — it’s quite possible that the latter, more modern protocols already support everything I’m hoping to see, while ActivityPub never will.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version
	- reordered main chapters
- version control
    - this is version: 2
    - this is the current version: [[AI4Communities post]]
    - here is the previous version: [[AI4Communities 1]]

