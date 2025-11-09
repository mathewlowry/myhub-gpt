# Building resilient social media

**Next week I'll be speaking in Berlin at the launch event of eurosky.social, a satellite event of the high-level "Summit on European Digital Sovereignty".**

I'll post the video (if they record one) as part of my post-event followup, but today I want to publish some first notes on one of the themes emerging as I and the others prepare for the event: what resilience looks like in the social media space.

## Resilience

Firstly, what is resilience? Any dictionary will tell you that something is resilient if it can withstand and bounce back from shocks, rather than fissuring and collapsing. It's one of those ideas that's better communicated graphically, and by comparison to its opposite:

![[Pasted image 20251109111654.png]]
The resilient approach to organising our society's resources, right, is actually the norm. As David Bollier, author of “Think Like a Commoner" and Creative Commons co-creator, explained to Rabble in [a recent Revolution.Social podcast](https://www.youtube.com/watch?v=Z5nZU5cHhC4), "the commons is as old as humanity. It's kind of the default setting for coordination and governance... an estimated 2 billion people [still] depend upon commons of forest, fisheries, irrigation water, wild game... as part of their everyday existence".

Unfortunately, resilient systems can be captured, a process also known as enclosure of the commons. It takes significant resources - venture capital's deep pockets, or a State's heavy hand - but it's happened so much in the Western world these last two centuries that we seem to have almost forgotten that alternatives exist. Which is ironic, given that you're reading this thanks to open-source software, a brilliant example of how noncapitalist methods can create enduringly valuable stuff.

## From Blogosphere to X.com

**Social media today is a great example of what happens when a resilient network is captured by a few monopolists. But it wasn't always so.** 

The original Web2.0 was resilient - a thriving, chaotic, bubbling networks of blogs, using RSS to both sustain cross-network conversations and help everyone follow it.

![[Pasted image 20251109115316.png]]

But while blogs still exist, over the past 15 years the blogosphere has been captured, enclosed, refined, distilled, consolidated and agglomerated until we have something looking more like this:
![[Pasted image 20251108135938.png]]
Image by Gemini, from: "A small number of gigantic monoliths stand separately in a barren desert. Inside these monoliths are users, trapped inside a toxic environment with trolls, bots and lunatics".

It's not hard to see that we have a problem.

## Rebuilding social media resilience
**The answer is not new, it just needs to be rediscovered.** 

Whenever I mention the p-word ("protocol") in Brussels I risk losing half my audience, so let me just point out that the blogosphere, above, thrived because:
* blogs are websites, built on http (**h**yper**t**ext **t**ransfer **p**rotocol)
* they communicate with each other and subscribers using Really Simple Syndication (RSS), the protocol still underpinning podcasting today
* subscribers could also get blog content using email, based on smtp (**s**imple **m**ail **t**ransfer **p**rotocol)

Why is this important? Because if I use protocols I don't need another p-word: "permission". I can build and manage a website and publish it to the world using my phone, and **noone can stop me:** I don't need permission to publish, you don't need permission to read, and there's nothing California billionaires can do about it if I create something new and interesting. 
### Diverse forms, even more diverse apps
**None of the above protocols were designed for social media.**

There are actually hundreds of social media protocols, but only a handful have any traction: ActivityPub, ATproto and Nostr. The same thing has happened on all three, with a hugely diverse array of social media forms emerging as people experiment and try stuff out.

Right now, for example, multiple apps based on the AT protocol are being developed in each category mentioned in the figure, below, but it's the categories which noone's yet thought of that have me really excited:

![[Pasted image 20251109122442.png]]
*Original image by Gemini, post-edited.*

The AT protocol was created by Bluesky for microblogging. Put it and all the other ATproto apps together and you get the **ATmosphere**, which currently looks something like this:

![[Pasted image 20251109133142.png]]
*Original image by Gemini, post-edited.*

Notice that: 
* for some categories there are **multiple "families" (aka "lexicons")** - there are multiple lexicons for longform blogging, for example, each with their own strengths and weaknesses
* each family has **multiple apps** - most people microblog on the ATmosphere using the Bluesky client, for example, but you can use Tweetdeck-inspired deck.blue, the utterly amazing "slow social" Anisota, plus Skywalker and many others
* some lexicon families sit **across boundaries** - after all, anyone can build anything, so there's no reason to pay any attention to the artificial categories I've drawn above
* **apps can interoperate** - for example, if you share a Whitewind blog post in Bluesky, your Bluesky post will appear as a comment on the blogpost, neatly integrating short- and long-form conversations.

But the most important thing about the above picture is what is *not* shown....

### Where are the users?
**In the ATmosphere, users are independent of apps.**

To show this I need to go back to Gemini and ask it to draw in three dimensions:
![[Pasted image 20251109134432.png]]
*Image by Gemini, lightly post-edited*

In the above image:
* users exist independently of the various apps
* each user has one identity, which works on all ATmosphere apps
* users store their data in Personal Data Servers, which are also independent of the apps.

There's much, much more`*1`, but the key point is that social lock-in is impossible.
## This is resilient social media
**Making social lock-in impossible ensures the resilience of protocol-based social media.**

People think advertising is the root cause of social media's problems, but they're wrong: advertising, after all, funded the news industry for decades. **Social lock-in is the original sin of platform-based social media**, trapping users and advertisers in toxic, hate-filled, bot-infested platforms, unable to move away for fear of losing access to their audiences. 

any ATmosphere app which mistreats its users will see them simply move on to a better one, 

On the ATmosphere `*2`, apps do not store "user accounts" or their users' content - instead, users manage these themselves, and can move their content wherever they want without losing friends, followers or posts. 

And that means that **any ATmosphere app which mistreats its users will see them simply move to a better one**, taking their social connections and content with them. 

## This is innovative social media
**With permissionlessness comes innovation, and with innovation comes growth.**

The ATmosphere has a virtuous growth cycle built into its DNA:
* Just as I can build any website I like, I can build any app on the ATmosphere I want
* I will have immediate access to all 40m-and-counting users already there
* My app can interoperate with other apps, helping all of them grow 
* And every person my new app attracts onto the ATmosphere is available to all other apps. 

Contrast that to the monoliths of social media today. Everything you do on X or Meta's various sites is contingent on them letting you - they decide if you can stay, they decide what you see, and whether your friends see you. Moreover, you're utterly limited to the features they give you, because those are the features which make them the most money and ensure you remain trapped. Finally, if you try building on top of their technology, they'll pull the rug out from under your feet.

That fear has given the platforms' owners a terrible sense of impunity, and stifled innovation for over ten years. This impunity must end, both for society's sake and to unleash a new wave of innovative startups.

## Sound too good to be true?
**There's nothing inevitable about protocol-based social media.**

It's easy to be cynical about the prospects. After all, ActivityPub is almost a decade old, and has barely 12m users. ATproto is much newer, but ~99% of the ATmosphere are Bluesky posts, created using the Bluesky app and stored on PDSs supplied by Bluesky Social PBC (the "Bluesky company"). Almost noone I know uses Nostr. And X and Meta are not exactly going to sit on their hands.

While there's nothing inevitable about protocol-based social media going mainstream, it is a future worth fighting for. The question is How.

Eurosky.social's is launching at a satellite event surrounding the Franco-German "Summit on European Digital Sovereignty". If you want European sovereignty in the social media space, you need:
* a global, resilient social media ecosystem where social lock-in is impossible
* and where there can be no single points of failure or control
* where all users can create their own spaces, algorithms and moderation regimes, and can launch companies to provide these to others
* and where each company is regulated according to the laws of their jurisdiction of incorporation.

Everything positive flows from these four characteristics. Miss one of them, and the commons you want to create will be inevitably enclosed.

Unfortunately, noone in Europe seems able to even define what digital sovereignty means. As Caroline de Cock [pointed out recently](https://www.linkedin.com/pulse/digital-sovereignty-europes-favourite-empty-buzzword-xh2me/), the term has so many meanings it has become meaningless, serving as "*a substitute for thinking and precision... used by anarchist collectives to describe self-managed infrastructure and by governments to justify firewalls*".

Applied to social media, digital sovereignty could therefore mean anything from encouraging the global growth of protocol-based social media through to launching protectionist Europrojects designed to create a European Twitter or Facebook.

Resilient systems are not made, they grow

I fear a real risk of the latter, simply because it's the sort of project which bureaucracies are designed to launch. Unfortunately, truly resilient systems, by definition, cannot be designed and created top-down by committees operating within hierarchies. Resilient systems are not made, they grow - we need to think like gardeners rather than architects, and focus on creating the right conditions for innovative startups to invent the future, rather than pouring public funds into replicating winners from the past.