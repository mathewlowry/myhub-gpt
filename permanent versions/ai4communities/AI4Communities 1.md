# AI4Communities: a model for a self-sustaining, user-owned public sphere

**Model collapse may provide the funding for accelerating decentralised collective intelligence. What needs to happen next?** 

*The version you're reading now is an early draft: I am publishing this using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e) - where I publish a string of versions as I develop my thoughts - because I'm hoping constructive reactions to early drafts like these will help me answer my questions and so finish the post. Links to the latest and previous versions, if any, are in the footer.*

---

In my last post I highlighted how the authors of the [model collapse paper](https://www.nature.com/articles/s41586-024-07566-y) in _Nature_ pointed out that in the future any data stemming from “_genuine human interactions … will be increasingly valuable_” for training the next generation of LLMs. Online, there’s nothing more genuinely human than the interactions in a well-managed digital community, so:

> “after greed and short-sightedness floods the commons with AI-generated content, poisoning the well for the next generation of LLMs, **well-managed online communities of actual human beings may be the only place where AIs can innovate and thrive**”  
>  — [How Model Collapse could revive authentic human communities](https://mathewlowry.medium.com/how-model-collapse-could-revive-authentic-human-communities-e723d8048ef3) 

This supports the **AI4Communities** idea, first outlined in [four January 2023 collective intelligence “manifesto posts”](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), which envisions tomorrow’s online denizens thriving in a wide range of “[_small is beautiful Fediverse communities, supported by AIs which the communities themselves own, train and monetise_](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4)", rather than putting up with whatever Meta’s or X’s global, “one size fits all” algorithms inflict on them to turn a profit.

So if model collapse has suddenly made AI4Communities more likely, **what is it exactly, how do we get there, and is anyone building it?**

### Why is small beautiful?

Via the [Three Legged Stool manifesto](https://publicinfrastructure.org/2023/03/29/the-three-legged-stool/), “Very Small Online Platforms” are _“social networks created for a very specific purpose, with rules, norms and affordances appropriate to that community”_ ([A social network taxonomy](https://newpublic.substack.com/p/a-social-network-taxonomy)). 

While they’re obviously having fun with the EU’s regulatory term for “[Very Large Online Platforms](https://ec.europa.eu/commission/presscorner/detail/en/IP_23_2413)”, they see VSOPs as separate from federated servers(1), which combine the benefits of small size while enjoying large reach via federation. 

But for the purposes of this post I’ll call them all “cozyweb”, partly to keep things simple, but mainly because AI4Communities should work for both, and because they all have one thing in common: their manageable size makes it easier for their inhabitants to establish and enforce community norms, making community management actually possible:

> “it’s fundamentally impossible to do good content moderation or conversation at a scale of billions… A town square operates at a certain size, not at a global scale” - [Could social media support healthy online conversations?](https://www.niemanlab.org/2024/07/could-social-media-support-healthy-online-conversations-new_public-is-working-on-it) 

**Which is not to say they’re all isolated**: while each cozyweb community has its own content moderation policies tuned to its needs, they can be networked together without sacrificing independence.

So while each cozyweb can be a village — “_small, most people know each other and you all share a common interest in keeping the sidewalks tidy_” — each can choose, if they wish, to build federated roads to many other servers, including bigger ones “_crowded with people, plenty of them sleazy and more than the occasional sidewalk madman… But you’ll always discover something or someone new there. Every second person’s selling something, but one in 20 is selling what you need. Besides, you’re selling too…_” (from [Welcome to the Fediverse, starry-eyed noob](https://mathewlowry.medium.com/welcome-to-the-fediverse-starry-eyed-noob-twittermigration-day-3-57b99350414)).

### Your AI at the gates, on your side

Today, _building_ a road between two servers is a question of federating them, while the actual traffic _travelling_ the road depends on whether the inhabitants follow each other.

Tomorrow, AI4Communities foresees each village with its own AIs. And they’ll be busy:

#### Content discovery: Your Own “For You”

T**oday,** Fediverse villages provide each inhabitant with three feeds: 

- Home: a reverse chrono feed of everyone you follow, wherever they are*
- Local: a reverse chrono feed of everyone in your village
- Federated: a reverse chrono feed of everyone followed by at least one person in your village, wherever they are*

And that’s it (* note: noone in your village can follow anyone from a village which your village does not federate with, which is a feature, not a bug).

The other protocols offer other affordances, so I’ll covre them below. 

T**omorrow, your village’s AI** could proactively pull in and surface content from across the Fediverse (again, excluding un-federated servers) of interest to each village inhabitant. These customisable “For You” feeds will be driven by **relevance and trust**, as explored earlier:

[![](https://cdn-images-1.medium.com/max/1600/1*uDYUKBayeAMIplXG1m-4KA.png)](https://mathewlowry.medium.com/building-collective-intelligence-from-social-knowledge-graphs-e3a465852e8b)

Concentric trust circles of collective intelligence, from [Building collective intelligence from social knowledge graphs](https://mathewlowry.medium.com/building-collective-intelligence-from-social-knowledge-graphs-e3a465852e8b)

**So how is this any different to X, Threads et al?** Two reasons:

F**acebook’s AI knows** what you do on Meta’s properties, plus whatever it gleans from spying on you as you browse the web and use apps.

That’s a lot, but think about what happens when you combine publishing tools (blogs, social posts) with bookmarking _and_ personal knowledge management, and then network them together across the Fediverse, all supported by a personal AI. That AI can learn from:

- what you do on the Fediverse
- your private knowledge library
- every article you bookmark or Hub (and so find really, really useful) 
- the notes you make about it as you curate it (which tells the AI exactly _what_ you find useful about it) 
- and everything else (blog posts and professional references, mainly) which you publish alongside them.

That’s a _shedload_ of tightly interconnected knowledge, all reflecting your interests and expertise. Any AI sourcing a knowledgebase like that will perform content discovery superbly well for you. And as we’ll see later, it’s also extremely valuable AI training data, due to the _authentically human curation and creation_ processes that went into making it.

But one thing’s _not_ there: your village AI doesn’t spy on you and sell your profile to help advertisers target you. Because of the second reason:

Y**our village’s algorithm works for you**, not the platform’s owners and advertisers. Don’t want it to optimise your feed for enragement? Tell it not to. Don’t like engagement bait, NSFW comedy or culture war memes? Tell it so. Only interested in a few topics? Let it know.

> your village’s algorithm works for you

And if your tastes don’t match the village’s algorithms, move to a village that does. Balancing an individual’s feed parameters with the village’s content moderation rulebook should be a fun problem to tackle, but far from insuperable, as each village can find its own balance. I’ll get to content moderation soon, but first I want to dig deeper into what happens when the same AI also supports online collaborations.

#### Collaboration support

**Chatting with strangers and making friends on a social media platform solves only a small part of the collective intelligence problem.** 

If you want to take things further and co-create something together with a group, you have a problem — hardly any social media platform offers integrated collaboration tools (exception: Reddit’s community wikis).

Which is why you need to agree, _as a group_, on a collaborative tool everyone is comfortable with (TL:DR; it doesn’t exist for groups larger than 4), and then co-create on one platform while chatting on the other.

I’m not sure why this is so. Work-oriented collaboration platforms offer reasonably seamless chat and collaboration environments. In the public realm, however, there’s a stubborn divide separating wikis and other groupware from blogging and social media.

I explored one solution almost 4 years ago in [Thinking and writing in a decentralised collective intelligence ecosystem](https://mathewlowry.medium.com/thinking-and-writing-in-a-decentralised-collective-intelligence-ecosystem-16dd2b1893cc). This video introduces the idea before exploring massive.wiki, an early example of what the collaborative part of the overall technology stack might look like:

A social ecosystem where users can seamlessly collaborate is a worthy goal in itself. Moreover, that collaborative work can be supported by your village’s AI (given consent from the group), which means these collaborations become _another_ source of high-value AI training data.

#### Content moderation and Governance

Enforcing any online space’s rules on content moderation is a thankless and sometimes hideous task, so the major platforms have already invested fortunes into AI-supported moderation. Open-source LLMs now make it possible to develop something similar for cozyweb spaces.

Each village’s moderation AI could intervene in many different ways, from nudging members to rephrase a specific post to outright banning another for life. It would also intervene at several stages of content development, from before a member clicks the “Post” button through to the moment a conversation starts overheating.

Most of all, of course, the AI will constantly learn from the village’s inhabitants what they like and dislike.

The key to success will be **effective community co-ownership of the village rulebook** which the AI enforces. After all, if you no longer agree with your village’s rules you can move to another one easily, so ensuring everyone has a say in defining its rules is essential for any village to thrive.

> a community working together to train their village AI

This raises the truly fascinating possibility of a community working together to train their village AI. Obviously, any member should be able to contest a decision — the conversations around these edge cases are then used to fine-tune the rulebook. The AI should take an active role in these conversations, effectively being coached by the community on norms and practices. I suspect the coaching will be bidirectional much of the time.

### Who pays?

The Fediverse has been around in one form or another almost as long as Twitter and Facebook (Evan Prodromou launched Identi.ca in 2008). But although they are growing now (see below), Fediverse spaces haven’t thrived compared to their closed counterparts, at least partly because they lack a business model, as I found out almost a year ago:

> “Social infrastructure needs to deliver content as a basic minimum. And running that infrastructure takes time, money and professionalism” — [All my toots gone](https://mathewlowry.medium.com/all-my-toots-gone-e844f7c5f255) 

#### Diverse business models

The Three Legged Stool authors believe “_many VSOPs will likely receive most of their revenue from the communities they serve, similar to how a local newspaper or nonprofit is funded_”, and I hope they’re right. Today, however, only a small fraction of most Mastodon users currently donate to cover their server’s costs (anecodotal).

People may pay more for a better experience. An AI owned by the community, which reflects their preferences and adds value in many ways could provide that experience.

Moreover, as I pointed out [when I launched myhub.ai](https://myhub.ai/items/faq-how-is-myhubai-free-and-without-ads-what-is-your-business-model), each community could also act as a **data union**: rather than just paying to use AI to help manage their community, they could [**own, train and _monetise_ the resulting algorithm**](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b) to at least help cover the costs of running the village.

> **training data** created by well-managed Fediverse spaces… may be valuable enough to drive growth.

While I shelved this idea when ChatGPT appeared, the model collapse paper now suggests that it’s the **training data** created by well-managed Fediverse spaces, not the AIs they use and train, which may be valuable enough to drive growth. Perhaps both.

Of course, forming a data union is just one model: someone else could set up a for-profit instance, a third could let users choose between paying a subscription fee or seeing ads, and so on.

![](https://cdn-images-1.medium.com/max/1600/1*3WBzTFfnFM1bgbiQsV3T3A.png)

Different cozyweb communities offering users different experiences, including AI services sourced from multiple AI marketplaces and individual suppliers.

We need to create an environment in which such experiments can flourish.

### Early inspiration: Brave

There is already evidence for this strategy in a parallel field. In May 2023 Brave Software, creators of the privacy-first Brave browser and search engine, released [Brave Search API](https://brave.com/ai/using-brave-search-api). Via this service, AI developers can access the training dataset Brave developed through both Brave Search and their [Web Discovery Project](https://support.brave.com/hc/en-us/articles/4409406835469-What-is-the-Web-Discovery-Project), which allows Brave browser users to contribute anonymous data about the pages they’re actually visiting.

As a result, Brave’s training data “_is much more representative of the Web people actually care about_”, without the huge morass of “_junk sites — spam, dead links, duplicates, and more_” one finds when crawling the Web at large. And that was written _before_ the Web started filling up with AI-generated content, which is even worse for training AI.

#AI4Communities is the social media equivalent of Brave’s approach to search. Both revolve around **authenticity-driven data quality:** 

- People do not actually spend a lot of time browsing junk content, so Brave’s dataset doesn’t have any, and so is of higher quality
- People in well-run communities do not curate, share and collaborate on rubbish content, so the data they create will be valuable, too.

### Counting chicken, hatching eggs

**So how do we get there?** 

This is probably a chicken-end-egg problem:

- AI services may not emerge until cozyweb spaces exist which are ready to use them
- those spaces won’t appear before there are AI services to use.

This is a well-known type of problem, but so is the solution: provide some of the missing pieces to demonstrate value, and let competition drive innovation. And fortunately there are potential cozyweb spaces everywhere, with the Fediverse full of Very Small Online Platforms, all able to talk to each other if they choose to:

![](https://cdn-images-1.medium.com/max/1600/1*WokoW7AeAA3PbqH9AfkrrQ.png)

According to [https://fedidb.org/](https://fedidb.org/), there are almost 30000 Fediverse servers, just under half of which were launched in the last two years.

And while most are small, these figures presumably also include [Threads](https://engineering.fb.com/2024/03/21/networking-traffic/threads-has-entered-the-fediverse/), [Flipboard](https://about.flipboard.com/business/publisher-federation-flipboard/), and at least some sites built with [Ghost](https://activitypub.ghost.org/) or [Wordpress](https://wordpress.com/support/enter-the-fediverse/).

So the content and people are already there. To help them pilot #ai4communities, we need to trigger a virtuous circle by:

- creating **ActivityPub-based plugins** to allow these instances to access what the Three Legged Stool manifesto calls a **”Friendly Neighborhood Algorithm Store**” — an AI service marketplace for cozyweb villages
- launching that Store using open protocols, stocked with some first-generation AI services like the ones explored above.

Early adopter Fediverse communities can then start roadtesting the first AI services. Assuming these add value, more people will join those communities. As revenue starts flowing into them from both subscriptions and data monetisation, other Fediverse communities will follow suit. 

> The winners in this competition are the most active, best-managed communities

Seeing a business opportunity, other AI services will appear, attracting more communities, creating more data, growing the pie further. Competition and innovation will do the rest, with the emphasis on open source meaning anyone can not only add an AI service to existing Stores, they can market their services independently or set up Stores of their own.

What sets this vision apart is **who wins in this environment - the most active and best-managed communities**, as they will be an excellent source of AI training data once model collapse has stymied LLM growth.

---

#### Followups & Notes

The content behind this article is, of course, tagged #[ai4community](https://myhub.ai/@mathewlowry/?tags=ai4communities) on my Hub. My next posts will include, inter alia, how I’d like to develop myhub.ai to support the above ideas. Subscribe to my newsletter via my [About page](https://myhub.ai/@mathewlowry/about/) if you want to see that post _and_ the best articles I’m reading as I do my research (all editions [tagged #newsletter](https://myhub.ai/@mathewlowry/?tags=newsletter)).

(1) I refer to federated servers because I want to be technology agnostic, and avoid flamewars over the relative benefits of ActivityPub, AT Protocol, Nostr, etc. However some of this post reflects my greater familiarity with ActivityPub than the other protocols. Sorry about that.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- version control
    - this is version: 1
    - this is the current version: [[AI4Communities intro]]
    - here is the previous version: n/a

